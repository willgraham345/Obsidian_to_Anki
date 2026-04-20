---
summary: Python's implementation of the import system. Exposes import machinery for dynamic loading, module inspection, custom importers, and resource/metadata access.
type: note/library
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
up: "[[Python]]"
similar:
  - "[[Python import]]"
  - "[[Python Modules]]"
ai_generated: true
date created: Wednesday, November 12th 2025, 5:59:44 pm
date modified: Tuesday, April 7th 2026, 11:00:56 am
keywords:
  - "[[Python import]]"
libraries:
  - "[[Python importlib metadata]]"
  - "[[Python importlib resources]]"
library_of:
  - "[[Python Scoping Rules]]"
  - "[[Python]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Python Modules]]"
  - "[[Python Package Managers]]"
  - "[[Python Packages]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[importlib — The implementation of import — Python 3.14.0 documentation](https://docs.python.org/3/library/importlib.html#module-importlib)

## Concepts of Note
### Sub-packages
󰙎 importlib.util ;;; Utilities for spec creation, module loading, lazy loading, and availability checks — the most commonly used sub-package
󰙎 importlib.abc ;;; Abstract base classes for custom importers: `MetaPathFinder`, `PathEntryFinder`, `Loader`
󰙎 importlib.machinery ;;; Concrete finder/loader implementations: `SourceFileLoader`, `ModuleSpec`, `FileFinder`
󰙎 importlib.metadata ;;; Read installed package metadata (version, entry points, classifiers) — see [[Python importlib metadata]]
󰙎 importlib.resources ;;; Access package data files at runtime — see [[Python importlib resources]]

### Import System Primitives
󰙎 ModuleSpec ;;; Object describing a module before it loads: `name`, `loader`, `origin` (file path), `submodule_search_locations`
󰙎 finder ;;; Locates a module given its name. `sys.meta_path` finders run first; `sys.path_hooks` finders handle path-based entries
󰙎 loader ;;; Executes a module given its spec — responsible for `exec_module()`
󰠗 How to add a custom finder? ;; Insert an object implementing `find_spec(fullname, path, target)` into `sys.meta_path`
󰠗 Difference between `importlib.import_module` and `__import__`? ;; `import_module` is the clean public API — handles relative imports via the `package` arg and returns the leaf module, not the root package

## Usage
### Dynamic Import by Name
 `importlib.import_module('os.path')` ;;; Import a module by string name — equivalent to `import os.path`, returns the module object
 `importlib.import_module('.sibling', package='mypkg')` ;;; Relative import: imports `mypkg.sibling`
 `cls = getattr(importlib.import_module(mod_name), class_name)` ;;; Load a class by fully-qualified string names — common plugin pattern


```python
import importlib

# Simple dynamic import
os_path = importlib.import_module('os.path')

# Plugin loader pattern: load class by config string
def load_plugin(module_path: str, class_name: str):
    mod = importlib.import_module(module_path)
    return getattr(mod, class_name)

Handler = load_plugin('myapp.handlers.http', 'HttpHandler')
instance = Handler()
```

### Check Availability Without Importing
 `importlib.util.find_spec('numpy')` ;;; Returns `ModuleSpec` if importable, `None` if not — safe availability check with no side effects
 `if importlib.util.find_spec('ujson') is not None:` ;;; Guard before using an optional dependency


```python
import importlib.util

# Optional dependency with fallback
if importlib.util.find_spec('ujson') is not None:
    import ujson as json
else:
    import json

# Check multiple optional deps at startup
MISSING = [pkg for pkg in ('numpy', 'pandas', 'scipy')
           if importlib.util.find_spec(pkg) is None]
if MISSING:
    raise RuntimeError(f"Missing required packages: {MISSING}")
```

### Load Module from Arbitrary File Path
 `spec = importlib.util.spec_from_file_location('mymod', '/path/to/mymod.py')` ;;; Create a spec for a `.py` file not on `sys.path`
 `mod = importlib.util.module_from_spec(spec)` ;;; Instantiate the module object from the spec (does not execute it yet)
 `spec.loader.exec_module(mod)` ;;; Execute the module — after this, `mod` is fully populated
 `sys.modules['mymod'] = mod` ;;; Register in `sys.modules` so subsequent `import mymod` reuses this instance


```python
import importlib.util
import sys

def import_from_path(module_name: str, file_path: str):
    """Load any .py file as a module, regardless of sys.path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod   # register before exec to handle circular imports
    spec.loader.exec_module(mod)
    return mod

# Load a script outside the project tree
config = import_from_path('deploy_config', '/etc/myapp/deploy.py')
print(config.DATABASE_URL)
```

### Reload
 `importlib.reload(mod)` ;;; Re-execute a previously imported module in-place — picks up source changes without restarting; the module object identity is preserved


```python
import importlib
import sys

# Hot-reload a config module during a long-running process
import myapp.config as config

def refresh_config():
    importlib.reload(config)          # re-executes the module file in-place
    print("Reloaded:", config.DEBUG)  # module object identity unchanged

# Thread-safe reload
import threading
_lock = threading.Lock()

def safe_reload(mod):
    with _lock:
        importlib.reload(mod)
```

### Lazy Loading
 `loader = importlib.util.LazyLoader(spec.loader); spec.loader = loader` ;;; Wrap a loader so the module body executes only on first attribute access — useful for optional heavy dependencies

```python
import importlib.util
import sys

def lazy_import(name: str):
    """Import a module lazily — body executes only on first attribute access."""
    spec = importlib.util.find_spec(name)
    loader = importlib.util.LazyLoader(spec.loader)
    spec.loader = loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    loader.exec_module(mod)
    return mod

# numpy is NOT loaded yet — no startup cost
np = lazy_import('numpy')
# First attribute access triggers actual import
arr = np.array([1, 2, 3])
```

### Custom Meta Path Finder

```python
import importlib.abc
import importlib.machinery
import sys

class PrefixRedirectFinder(importlib.abc.MetaPathFinder):
    """Redirect imports of 'legacy.*' to 'newpkg.*'."""

    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith('legacy.'):
            return None
        new_name = fullname.replace('legacy.', 'newpkg.', 1)
        return importlib.util.find_spec(new_name)

# Register before any legacy imports
sys.meta_path.insert(0, PrefixRedirectFinder())

# Now 'import legacy.utils' transparently loads 'newpkg.utils'
import legacy.utils
```