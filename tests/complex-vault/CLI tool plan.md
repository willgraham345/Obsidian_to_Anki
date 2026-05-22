
### 1. Project layout
```
obsidian_breadcrumbs_graph/
│   pyproject.toml          # build / dependency declarations
│   README.md
│   LICENSE
│
├── obsidian_breadcrumbs_graph/
│   ├── __init__.py
│   ├── cli.py              # entry‑point, argparse handling
│   ├── scanner.py          # walk vault, read markdown files
│   ├── parser.py           # extract YAML front‑matter, collect link arrays
│   ├── graph.py            # build a networkx DiGraph, apply depth filter
│   ├── exporter.py         # JSON/YAML dump, HTML/SVG rendering
│   └── templates/
│       └── markmap_template.html   # basic HTML wrapper for markmap.js
│
└── tests/
    ├── test_parser.py
    ├── test_graph.py
    └── fixtures/…          # small markdown samples
```

---

### 2. Dependencies
| Purpose | Library |
|--------|---------|
| YAML front‑matter parsing | **ruamel.yaml** (preserves ordering) |
| Markdown file reading | **pathlib**, built‑in |
| Graph representation | **networkx** |
| HTML/SVG rendering (markmap‑style) | **markmap-cli** (npm) **or** embed **markmap.js** in a static HTML template and feed a JSON tree |
| JSON/YAML export | **json**, **ruamel.yaml** |
| CLI handling | **argparse** (standard) |
| Testing | **pytest** |

*Both `networkx` and `ruamel.yaml` are pure‑Python; `markmap-cli` can be invoked as a subprocess (the user will have Node/npm installed).*

---

### 3. Core workflow (high‑level pseudocode)

```python
def main():
    args = parse_cli()
    files = discover_markdown_files(args.root, max_depth=args.max_depth_fs)
    all_nodes = []
    for f in files:
        fm = extract_frontmatter(f)
        node = build_node_from_fm(f, fm, args.key_filter)
        all_nodes.append(node)

    G = merge_nodes_into_graph(all_nodes, depth_limit=args.max_depth_graph)

    # Export
    if args.out_json:
        dump_json(G, args.out_json)
    if args.out_yaml:
        dump_yaml(G, args.out_yaml)

    # Visual
    html_path = render_markmap_html(G, args.out_html or default_path)
    open_in_browser(html_path)   # optional, based on `--view`

```

#### 3.1 CLI (`cli.py`)
Options (using `argparse`):

| Flag | Description |
|------|-------------|
| `root` (positional) | Path to vault root (default `.`) |
| `-k/--keys` | Comma‑separated list of front‑matter keys to include (`concepts,workflows,…`). If omitted, all array keys are used. |
| `-d/--max-depth-graph` | Maximum graph depth (default = 2). |
| `-D/--max-depth-fs` | Max directory recursion depth when walking the vault (default = None → unlimited). |
| `--json <file>` | Write JSON representation to `<file>`. |
| `--yaml <file>` | Write YAML representation to `<file>`. |
| `--html <file>` | Write HTML (markmap) to `<file>` (default = `graph.html`). |
| `--view` | Open generated HTML in the default browser after creation. |
| `--quiet` | Suppress progress printing. |

#### 3.2 File discovery (`scanner.py`)
* Use `pathlib.Path.rglob('*.md')` with a custom depth filter:
```python
def discover_markdown_files(root, max_depth=None):
    root = Path(root).resolve()
    for path in root.rglob('*.md'):
        if max_depth is not None:
            if len(path.relative_to(root).parts) > max_depth:
                continue
        yield path
```

#### 3.3 Front‑matter extraction (`parser.py`)
*Read only the YAML block at the top of the file:*
```python
def extract_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines[0].strip().startswith('---'):
        return {}
    fm_lines = []
    for line in lines[1:]:
        if line.strip().startswith('---'):
            break
        fm_lines.append(line)
    yaml_text = ''.join(fm_lines)
    return ruamel.yaml.YAML().load(yaml_text) or {}
```

*Identify array‑type keys containing wiki‑links:*
```python
def is_link_array(value):
    if not isinstance(value, list):
        return False
    return all(isinstance(v, str) and '[[' in v and ']]' in v for v in value)

def build_node_from_fm(filepath, fm, key_filter):
    node = {
        'file': str(filepath),
        'title': filepath.stem,
        'children': []   # will hold (key, linked_note) pairs
    }
    for key, val in fm.items():
        if key_filter and key not in key_filter:
            continue
        if is_link_array(val):
            for link in val:
                target = link.strip('[]')
                node['children'].append({'key': key, 'target': target})
    return node
```

#### 3.4 Graph construction (`graph.py`)
*Create a directed graph where each front‑matter key is a parent node, and each link is a child leaf.*

```python
def merge_nodes_into_graph(nodes, depth_limit):
    G = nx.DiGraph()
    for n in nodes:
        file_node = f"file:{n['title']}"
        G.add_node(file_node, type='file', label=n['title'])

        for child in n['children']:
            key_node = f"{file_node}:{child['key']}"
            G.add_node(key_node, type='key', label=child['key'])
            G.add_edge(file_node, key_node)

            leaf_node = f"{key_node}:{child['target']}"
            G.add_node(leaf_node, type='link', label=child['target'])
            G.add_edge(key_node, leaf_node)

    # Apply depth limit (BFS from each file node)
    if depth_limit is not None:
        nodes_to_remove = []
        for start in [n for n, d in G.nodes(data=True) if d['type'] == 'file']:
            for node, dist in nx.single_source_shortest_path_length(G, start).items():
                if dist > depth_limit:
                    nodes_to_remove.append(node)
        G.remove_nodes_from(set(nodes_to_remove))

    return G
```

#### 3.5 Exporters (`exporter.py`)

**JSON / YAML**
```python
def dump_json(G, path):
    data = nx.node_link_data(G)   # networkx built‑in format
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def dump_yaml(G, path):
    data = nx.node_link_data(G)
    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)
```

**HTML (Markmap)**
1. Convert the NetworkX graph to a nested JSON tree that **markmap.js** understands:
   ```python
   def nx_to_markmap_tree(G):
       roots = [n for n, d in G.nodes(data=True) if d['type'] == 'file']
       def build(node):
           children = [build(c) for c in G.successors(node)]
           return {"name": G.nodes[node]['label'],
                   "children": children}
       return [build(r) for r in roots]
   ```
2. Write a small HTML file that loads `https://cdn.jsdelivr.net/npm/markmap-lib@0.13.5/dist/index.min.js` and calls `markmap.Markmap.create('#mindmap', data)`.
   ```html
   <!-- obsidian_breadcrumbs_graph/templates/markmap_template.html -->
   <!DOCTYPE html>
   <html>
   <head>
     <meta charset="utf-8"/>
     <title>Obsidian Breadcrumbs Graph</title>
     <script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.13.5/dist/index.min.js"></script>
   </head>
   <body>
     <svg id="mindmap"></svg>
     <script>
       const data = {{ JSON_DATA | safe }};
       markmap.Markmap.create('#mindmap', data);
     </script>
   </body>
   </html>
   ```
3. Render:
   ```python
   from jinja2 import Environment, FileSystemLoader
   def render_markmap_html(G, out_path):
       env = Environment(loader=FileSystemLoader(str(Path(__file__).parent / 'templates')))
       tmpl = env.get_template('markmap_template.html')
       json_data = nx_to_markmap_tree(G)
       html = tmpl.render(JSON_DATA=json.dumps(json_data))
       Path(out_path).write_text(html, encoding='utf-8')
       return out_path
   ```

*Optionally*, if the user prefers a pure SVG, run the `markmap-cli` npm package:
```python
subprocess.run(['npx', 'markmap-cli', '--output', out_svg, '--bundle', json_file])
```
(Provide a fallback in `exporter.py`.)

#### 3.6 Optional browser launch
```python
import webbrowser
def open_in_browser(path):
    webbrowser.open_new_tab('file://' + str(Path(path).resolve()))
```

---

### 4. Testing strategy
| Test | Goal |
|------|------|
| `test_parser.py` | Verify front‑matter extraction, correct detection of array‑link keys, handling of missing YAML block. |
| `test_graph.py` | Ensure graph merging creates the expected hierarchy, depth‑limit correctly prunes nodes, duplicate links across files are deduped. |
| Integration test (in `tests/`) | Run CLI on the three example files, check that JSON output matches a stored fixture, and that HTML file is generated without error. |
| Performance test | Run on a synthetic vault with 500 md files to ensure memory usage stays reasonable. |

All tests use the `pytest` runner; CI can be added later.

---

### 5. Packaging & distribution
* Use `pyproject.toml` with `setuptools`/`poetry` to expose a console script entry point:
```toml
[project.scripts]
obsidian-breadcrumbs-graph = "obsidian_breadcrumbs_graph.cli:main"
```
* Add a `requirements.txt` (or let poetry manage) listing `ruamel.yaml>=0.17`, `networkx`, `jinja2`, `pytest`.  
* Document the need for Node/npm and `markmap-cli` for SVG output in the README.

---

### 6. Next steps
1. Scaffold the project directory and create the `pyproject.toml`.  
2. Implement `parser.py` and verify it correctly extracts link arrays from the three sample files.  
3. Build a minimal `graph.py` that constructs the NetworkX graph and dump it as JSON.  

*You can start by creating the package skeleton; let me know when you’re ready, and I can provide the exact `pyproject.toml` and a starter `cli.py`.*

### Clarification Q&A
Before I outline a detailed implementation plan, I need a few clarifications so the tool matches exactly what you have in mind.

1. **Output format**  
   - Do you want a plain‑text tree (e.g., using Unicode box‑drawing characters) printed to the terminal, or a visual graph (e.g., generated as an SVG/HTML file) like *markmap* does?  
   - If you prefer a visual graph, should the tool launch a browser to display it, or just write the file to disk?

2. **Front‑matter keys to include**  
   - The examples contain many keys (`concepts`, `workflows`, `libraries`, `headings`, `down`, `items`, …). Should the tool treat **all** keys that hold an array of wiki‑links as nodes, or only a selected subset (e.g., `concepts`, `workflows`, `headings`)?  
   - If a key has a mixed list (some plain strings, some `[[links]]`), should non‑link items be ignored?

3. **Link handling / hierarchy**  
   - The Breadcrumbs plugin builds a hierarchy based on the order of links in a list (e.g., `["A", "B", "C"]` → A → B → C). Is that the rule you want to apply to every list in the front‑matter?  
   - Some front‑matter entries are single‑level (e.g., `libraries: ["[[Jinja]]", "[[Python black]]"]`). Should those be displayed as sibling leaves under a parent node named after the key (`libraries`), or should each be a top‑level root node?

4. **File selection**  
   - Will the tool be invoked with a single file path, a glob pattern, or should it walk the entire vault and generate a combined map?  
   - If multiple files are processed, do you want separate trees per file, or a merged graph linking across files?

5. **Customization / options**  
   - Would you like command‑line flags to filter by key (e.g., `--keys concepts,workflows`) or to set a maximum depth?  
   - Should the tool support outputting JSON/Markdown for downstream processing, or only the visual representation?

6. **Dependencies and packaging**  
   - Are you comfortable pulling in third‑party libraries such as `pyyaml` (for front‑matter parsing) and `graphviz`/`markmap-cli` for graph generation, or do you prefer a pure‑Python solution without external binaries?  
   - Do you need the tool packaged as a pip‑installable module, or just a single script you can run directly?

Once I have answers to these points, I can present a concrete step‑by‑step plan covering parsing, hierarchy construction, rendering, CLI design, and testing.

Answering your questions below:
1. I want a visual graph presented as HTML or SVG, and I prefer a visual graph.
2. The tool should treat all keys that hold an array as nodes, and provide filtering for which nodes are available.
3. Each of those should be a sibling leave under a parent node named after the key.
4. I would like the tool to walk files to a specified depth. Make the default 2 connections deep. I'd like the graph to be merged.
5. I would like the cli tags to filter both by key, as well as a maximum depth. Output both a visual representation, as well as JSON or yml graph representation.
6. Yes, I'm fine with both of those libraries being pulled in. I will handle the sourcing of all libraries.

