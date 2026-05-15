---
date created: Thursday, June 26th 2025, 12:49:41 pm
date modified: Thursday, June 26th 2025, 12:49:50 pm
---

# Seamless Knowledge Transfer: Exporting Markdown Tables, Callouts, and Tasks from Obsidian to Anki

## I. Executive Summary

This report addresses a critical challenge for knowledge workers and researchers: the automated and reliable transfer of structured information from Obsidian notes, specifically markdown tables, callouts, and tasks, into Anki flashcards. The overarching objective is to eliminate manual data re-entry, thereby establishing Obsidian as the singular, consistent source of truth for learning materials. This approach ensures data integrity and streamlines the spaced repetition workflow.

The analysis reveals that the "ObsidianToAnki" plugin, despite user concerns regarding its maintenance, stands as the most versatile and potent solution. Its robust support for custom syntax, particularly through regular expressions (regex), directly addresses the intricate parsing requirements for markdown tables, callouts, and tasks. While other plugins offer alternative functionalities, the profound customization capabilities inherent in ObsidianToAnki render it uniquely suited for advanced, highly specific workflows.

A hybrid strategy is recommended, primarily leveraging "ObsidianToAnki"—either as an Obsidian plugin or its standalone Python script counterpart—for its unparalleled custom regex parsing. This methodology ensures that Obsidian markdown files function as the canonical data source, aligning precisely with the user's desire for a "database-like" structure and effectively minimizing data redundancy across platforms.

## II. Understanding Your Advanced Workflow Requirements

### Deconstructing the User's Ideal Workflow: From Preformatted Notes to Anki Cards

The user's envisioned workflow is characterized by a sophisticated, multi-stage process for knowledge capture and transfer. The initial phase involves **information capture** within Obsidian, specifically utilizing "preformatted task or callout" structures. This preference for Obsidian's native markdown elements for content organization indicates that any viable solution must possess the capability to accurately interpret and extract data from these distinct formats. The reliance on these specific markdown constructs suggests a need for a parser that can understand Obsidian's unique extensions, going beyond simple question-answer pairs.

Following information capture, the workflow proceeds to **data assembly or collection**. Here, the captured information is either explicitly "assembled into a table" or its collection is managed "through regex expressions." This dual requirement highlights a critical need: the direct export of existing markdown tables, and the programmatic ability to extract and structure data from less rigidly formatted, yet patterned, content such as callouts or tasks by employing regular expressions. This aspect of the workflow is not merely about creating basic flashcards; it demands intelligent parsing of structured Obsidian content. The explicit mention of "regex expressions" points directly towards solutions with strong regex capabilities as a fundamental requirement, rather than those relying on simpler, predefined syntaxes.

The final stage involves the **export to Anki**, emphasizing the necessity for direct, efficient, and automated synchronization of this processed information. The objective is to avoid repetitive manual tasks, thereby ensuring that the knowledge transfer process is as seamless as possible. This sophisticated approach to data extraction from specific Obsidian markdown constructs necessitates a solution with highly flexible parsing capabilities, making raw regex power a critical differentiator when compared to simpler, predefined syntaxes.

### The Importance of Data Consistency: Why a "Database/JSON" Approach Matters

The user's explicit request for "a form of database or json file containing the information" underscores a fundamental operational requirement for data consistency, integrity, and machine-readability. This objective is crucial for preventing data silos, facilitating future automation, and enabling advanced analytical processes. The concern is not merely about data transfer but about establishing a reliable, single source of truth.

From a practical standpoint for Anki synchronization, Obsidian markdown files themselves can effectively serve as this "database." When information is structured consistently within these files—for instance, by employing markdown tables, adhering to defined callout formats, or utilizing standardized task syntax—these plain text files transform into a human-readable, version-controllable, and readily parsable data source. This approach inherently fulfills the user's requirement for a structured data store. The parsing mechanism, such as regular expressions, then functions as the "query engine" for this markdown "database," extracting the necessary fields for Anki cards.

The approach of treating Obsidian's structured markdown files as the "canonical source of truth" 1 is a more efficient and less complex solution than maintaining a separate, external database or JSON file solely for Anki integration. This method leverages the inherent structure of markdown and avoids the overhead and potential synchronization complexities associated with managing redundant data stores. The structured nature of markdown, combined with robust parsing tools, allows the markdown files themselves to function as a human-readable, version-controllable "database." This means that the information within these files, when consistently formatted, is already structured data, and the role of the Anki integration plugin becomes to extract this structured data, rather than requiring an intermediate database.

## III. In-Depth Analysis of Obsidian-to-Anki Integration Solutions

### A. The ObsidianToAnki Plugin: A Deep Dive

The Obsidian_to_Anki plugin serves as a direct and powerful bridge, enabling users to convert markdown notes into flashcards and seamlessly synchronize them with Anki.1 This plugin offers an extensive suite of features crucial for complex and varied learning workflows. These capabilities include support for custom Anki note types, advanced cloze deletions, the embedding of images and audio, and the creation of inline notes, making it highly adaptable to diverse learning styles and content formats.1

A critical aspect of this plugin, directly addressing the user's primary requirement, is its explicit support for "tables" and its provision of "flexible custom syntax for flashcard creation".4 This functionality is paramount for users who organize their learning material within markdown tables. Furthermore, the plugin offers granular control over the scanning process, allowing it to scan an entire Obsidian vault or specified sub-directories, and enabling users to exclude particular files or folders using glob patterns.1 A fundamental design principle of ObsidianToAnki is its ability to update notes directly from the source markdown file, thereby ensuring that the Obsidian note remains the canonical source of truth for the flashcard content.1

#### Addressing Maintenance Concerns

The user's apprehension regarding the "ObsidianToAnki" plugin's maintenance status is a pertinent consideration. However, a detailed examination of the available data presents a more nuanced perspective. While the project may not exhibit daily updates, the GitHub repository indicates that the "latest commit" occurred "last year" 1, and the "latest release is 3.6.0, as of January 24, 2024".5 This suggests that the project is not abandoned but rather undergoes periodic maintenance, receiving updates and new releases, albeit potentially not with the highest frequency. The presence of 221 open issues and 27 open pull requests 5 further signifies an active user base and ongoing community engagement, even if the resolution of these items might be slower than some users prefer. The perceived "lack of maintenance" may stem from a slower development pace rather than outright abandonment. For a technically proficient user, this periodic maintenance is often acceptable, particularly when weighed against the plugin's powerful and unique customization options, which directly address complex workflow needs. The prevailing situation reflects a trade-off between hyper-active development and the robust feature set already available.

#### Leveraging Custom Syntax with Regex: The Core of Your Workflow

The most significant strength of ObsidianToAnki for the user's specific workflow lies in its support for "custom syntax - Using regular expressions".1 This feature empowers users to define highly specific patterns within their Obsidian notes that the plugin will recognize and subsequently convert into Anki flashcards. This adaptability is crucial for handling diverse and complex markdown structures.

It is important to understand that all custom syntax functionalities are "off by default, and must be programmed into the script via the config file".1 This configuration mechanism is where the "deeper customization" 4 of the plugin is unlocked, allowing for precise control over the parsing logic. The plugin's Wiki explicitly provides a "Markdown table style" example for custom regex 1, which directly confirms its capability to parse markdown tables into Anki cards, addressing a core user requirement.

For users crafting custom regex patterns, the script automatically compiles these patterns with a 'multiline' flag. This is an essential technical detail, as it enables the regex to capture content that spans multiple lines, a common characteristic of Obsidian callouts or multi-line task descriptions. It is imperative that the number of capture groups defined within the regex accurately matches the number of fields in the target Anki note type.6 Discussions and issues documented on the plugin's GitHub repository 9 frequently highlight users actively engaging with and relying on this custom regex feature for diverse and highly specific use cases, including the creation of complex multi-field cards. The custom regex capability of ObsidianToAnki is the critical enabler for the user's advanced workflow. It transforms the plugin from a basic markdown-to-Anki converter into a highly flexible data extraction and mapping tool. This allows the user to define precise rules for extracting content from tables, callouts, and tasks, directly addressing their need for automation and structured data handling from varied Obsidian markdown formats.

#### Must-Have Table 1: ObsidianToAnki Custom Regex Examples for Structured Obsidian Notes

The following table provides concrete, actionable examples of regex patterns that can be implemented within the `obsidian_to_anki_config.ini` file. This serves as a practical guide, illustrating how ObsidianToAnki can parse specific Obsidian markdown structures—tables, callouts, and tasks—into Anki flashcards, thereby fulfilling the user's request for an in-depth description and practical guidance.

|Syntax Description|Example Markdown|Target Anki Note Type (Fields)|Corresponding Regex Pattern (for `obsidian_to_anki_config.ini`)|Regex Explanation|
|---|---|---|---|---|
|**Markdown Table Style**|\| Front Content \|<br><br>\| ------ \|<br><br>\| Back Content \||Basic (Front, Back) or Custom "Table Card" (Question, Answer)|`\|([^\n|]+)\|\n\|(?:[^\n|
|**Custom Callout Style**|> [!question] What is the capital of France?<br><br>> Paris.|Custom "Question/Answer" (Question, Answer)|`^> [!(?:question|info|
|**Custom Task Style**|- [ ] Task: Review report outline<br><br>Due Date: 2024-07-30<br><br>Priority: High|Custom "Task Details" (Task, Due Date, Priority)|`^- \[\s*\]\s*Task:\s*(.+?)\n\s*Due Date:\s*(.+?)\n\s*Priority:\s*(.+)$`|This regex is structured to extract specific fields from a multi-line task block. Group 1 captures the "Task" description. Group 2 captures the "Due Date," and Group 3 captures the "Priority." This pattern requires a custom Anki note type with three corresponding fields to map the extracted data accurately.|

#### Configuration File (`obsidian_to_anki_config.ini`) Explained

The `obsidian_to_anki_config.ini` file is a central component for customizing the plugin's behavior, particularly for defining custom regex patterns and linking them to specific Anki note types.1 This file serves as the primary interface for users to implement their tailored parsing logic.

Within this configuration file, users can precisely map their custom regex patterns to the appropriate Anki note types.6 This mapping is crucial for ensuring that extracted data is correctly assigned to the intended fields within Anki. Beyond regex definitions, the

`config.ini` also governs other fundamental plugin behaviors. These include specifying directories to scan, defining files or folders to ignore, and setting default deck assignments for flashcards.1 The

`config.ini` file effectively functions as the user's "database schema" for flashcard generation. It is the location where the user defines _how_ their structured markdown—which serves as their "database"—should be interpreted and subsequently mapped to Anki cards. This direct configuration capability aligns perfectly with the user's technical proficiency and their desire for granular control over the data transformation process.

### B. Exploring Alternative Obsidian Plugins

While ObsidianToAnki offers extensive customization, the Obsidian plugin ecosystem provides several alternatives, each with distinct philosophies and feature sets. Understanding these alternatives helps in making an informed decision based on specific workflow preferences.

**Yanki:** This plugin prioritizes a "Pure Markdown syntax. No fuss." approach.4 Yanki streamlines the synchronization of flashcards from specified folders in an Obsidian vault to Anki, automatically mapping the vault's folder hierarchy to Anki decks.17 It supports Anki's default note types (Basic, Reversed, Cloze, Type-in-the-answer) and infers the card type directly from the Markdown structure, for instance, using a

`---` thematic break to delineate the front and back of a card.17 Yanki also supports GitHub Flavored Markdown (GFM) features, including tables, task lists, WikiLinks, and LaTeX.17 While its simplicity is appealing, its "no fuss" philosophy means less room for highly custom regex patterns for arbitrary structures like unique callout or task formats beyond standard GFM.

**Anki Sync (also known as ObsidianAnkiSync):** This plugin enables robust flashcard creation and synchronization using a "flexible, markup-based syntax".16 It supports rich formatting, including math, code blocks, tables, and images, and allows for cloze deletions even within LaTeX math and code blocks.16 Cards are synchronized with options to create, update, or delete based on changes detected in the Obsidian vault.16 Deck and tag assignments can be configured on a per-file or per-block basis.16

**Blue Star:** This plugin is designed to generate Anki flashcards through a variety of "multiple parsing modes".4 It offers flexible options for card creation, supporting headings, sections, custom delimiters, or crucially,

_regular expressions_.16 This regex capability positions Blue Star as a strong contender for custom parsing needs. Additionally, it allows for document-level overrides, providing fine-grained control over card generation behavior within individual notes.19

**Brief overview of other relevant plugins:**

- **Note Synchronizer** 15: This plugin establishes a two-way link between Obsidian and Anki, mapping note content, folders, and tags directly to Anki's structure. It supports all Anki note types by importing them as markdown templates and utilizes YAML front matter for organizing note fields.
    
- **Anki Integration** 7: This plugin offers a user-friendly interface with pop-up windows for creating decks and notes, aiming for a seamless, native flashcard creation experience within Obsidian. Its focus is more on ease of use than complex markdown parsing.
    
- **AI-AnkiSync** 7: This plugin enhances flashcard workflows by combining note-based card creation with AI-powered content refinement. It can automatically detect flashcard patterns and improve content using language models, assigning decks and tags based on file names and note headings. While valuable for AI-assisted content generation, its primary function is not direct parsing of existing tables, callouts, or tasks.
    

The landscape of Obsidian-Anki integration plugins presents a spectrum ranging from "pure Markdown" simplicity (as offered by Yanki) to highly customizable, regex-driven parsing (exemplified by ObsidianToAnki and Blue Star). Given the user's specific requirements for handling tables, callouts, and tasks, coupled with their explicit mention of regex, the latter category of plugins is strongly favored.

### C. Comparative Analysis: Choosing the Right Plugin

To facilitate an informed decision, the following table provides a comparative analysis of key Obsidian-Anki plugins, focusing on features most relevant to the user's requirements, particularly markdown table support, custom syntax, and maintenance status.

|Plugin Name|Markdown Table Support|Custom Syntax/Regex Flexibility|Callout/Task Potential|Maintenance Status|Ease of Setup|Sync Direction|Data Source Philosophy|Key Differentiator|
|---|---|---|---|---|---|---|---|---|
|**ObsidianToAnki**|Yes (via custom regex) 2|High (custom regex via config file) 1|Direct support via custom regex patterns|Periodically Maintained (latest release Jan 2024, commits last year) 1|Medium (requires AnkiConnect & config file editing)|Obsidian -> Anki|Markdown as canonical source of truth 1|Unparalleled regex customization for complex parsing.|
|**Yanki**|Yes (GFM tables) 17|Low (predefined Markdown patterns) 17|Indirect (requires specific markdown structure)|Active (latest commit ~1 year ago) 4|Low (pure Markdown, minimal fuss)|Obsidian -> Anki|Markdown as canonical source of truth|Simplicity, pure Markdown, maps folder hierarchy to decks.|
|**Anki Sync**|Yes (rich formatting) 18|Medium (flexible markup-based syntax) 18|Indirect (via markup, not explicit callout/task parsing)|Active (latest commit ~8 months ago) 18|Medium (markup-based)|Obsidian -> Anki|Markdown as source of truth|Rich formatting support, cloze in code/LaTeX.|
|**Blue Star**|Not explicitly stated, but possible via regex|High (regex, custom delimiters) 19|Direct support via custom regex patterns|Periodically Maintained (latest commit ~7 months ago) 19|Medium (requires AnkiConnect & config)|Obsidian -> Anki|Markdown as source of truth|Multiple parsing modes, strong regex capabilities.|
|**Note Synchronizer**|Not explicitly stated, but possible via markdown templates|Medium (YAML front matter, markdown templates) 15|Indirect (via YAML/templates)|Periodically Maintained (latest commit ~3 years ago) 15|Medium|Two-way|Maps note content, folders, tags to Anki structure|Two-way linking, YAML front matter for fields.|

## IV. Script-Based Solutions for Ultimate Control

For users seeking the highest degree of control over their data transformation and Anki integration, standalone Python scripts offer a powerful alternative or complement to Obsidian plugins. These solutions are particularly appealing to technical users who may wish to automate complex data transformations or integrate with other custom scripts.

### A. Standalone Python Tools for Markdown Conversion

**ObsidianToAnki as a Python Script:** Beyond its functionality as an Obsidian plugin, ObsidianToAnki can also be executed as a standalone Python script.1 This mode of operation provides "deeper customization through config files" 4 compared to the plugin's graphical interface. When run as a script, it generates an

`obsidian_to_anki_config.ini` file for configuration 1, allowing direct manual editing of regex patterns and other operational settings. For users prioritizing maximum control and willing to engage directly with configuration files, the Python script version of ObsidianToAnki offers unparalleled flexibility. This is particularly beneficial for a user who might prefer to fine-tune parsing logic or integrate the flashcard generation process into a larger automated workflow.

**`markdown-anki-decks`:** This is a command-line program designed to convert markdown files into Anki decks, packaged as `.apkg` files.22 It follows a more rigid structural convention: H1 tags are interpreted as deck titles, H2 tags as questions, and the markdown content situated between H2 tags serves as the answers.22 While it supports AnkiConnect for direct synchronization and can be reimported without creating duplicate cards, and also handles cloze syntax and sounds 22, its fixed parsing structure makes it less flexible than ObsidianToAnki's custom regex for arbitrary markdown formats.

**`md2anki`:** Another Python-based tool, `md2anki` converts Markdown documents into Anki decks (`.apkg` files).23 A significant advantage of

`md2anki` is its explicit support for "All basic Markdown features (i.e. tables, bold, italics, lines)" 23, making it a strong contender for native table handling. It also supports LaTeX math, embedded images, and code blocks.23 Furthermore,

`md2anki` can merge notes from multiple markdown input files into a single Anki deck.23 While

`markdown-anki-decks` and `md2anki` are viable for general markdown conversion, `md2anki` stands out due to its native table support. However, neither of these tools offers the same level of granular, custom regex parsing for arbitrary structures like Obsidian-specific callouts and tasks as ObsidianToAnki. They are best suited for simpler, more standardized markdown-to-Anki conversions.

### B. Crafting Custom Data Pipelines with Regex

For highly specific or evolving markdown structures that might challenge even the most flexible plugins, a multi-stage data pipeline can be implemented. This approach involves extracting structured data from Obsidian notes using specialized tools and then feeding this data into Anki via custom scripts or native import functionalities.

**Using Obsidian's native capabilities or external tools to extract structured data:** Obsidian offers plugins that can facilitate the extraction of structured data from its markdown files. For instance, plugins like "Table to CSV Exporter" 24 and "JSON table" 25 can export data from Obsidian tables into CSV or JSON formats. This capability directly addresses the user's "database or json file" requirement, providing an intermediate structured output that can be used for other purposes or as input for a subsequent Anki import step. Additionally, Obsidian's native search and replace functionality with regex 19 or dedicated plugins such as "Regex Pipeline" 26 can be employed to pre-process or extract data from callouts and tasks. This pre-processing can transform the data into a more Anki-friendly format, such as simple question-answer lines or a temporary CSV/JSON file. For highly specific or evolving markdown structures, a multi-stage pipeline might be necessary. This could involve using Obsidian's native regex capabilities or specialized plugins to first extract data into a standard format (like CSV/JSON), and then feeding that into an Anki import tool (either a Python script or Anki's native CSV import). This offers maximum flexibility but also introduces higher complexity in the workflow.

**Integrating extracted data with Python scripts for Anki import:** Once data is in a structured format (e.g., CSV, JSON) through the aforementioned extraction methods, Python scripts can be utilized for programmatic Anki card creation. Libraries such as `genanki` can be employed to programmatically generate Anki decks (`.apkg` files), or custom scripts can interact directly with AnkiConnect for real-time import. This approach provides the most granular control over card fields, note types, and deck organization, aligning precisely with the user's desire for a "database" approach to their learning material. The Python ecosystem offers the ultimate "database" level control. If Obsidian plugins or even the ObsidianToAnki script's regex capabilities prove insufficient for highly bespoke extraction and mapping, a custom Python script can parse any structured markdown (or intermediate CSV/JSON) and build Anki cards precisely. This represents the most robust, albeit most involved, solution for complex data transformation needs.

## V. Recommended Workflow Implementation Strategies

### A. Optimal Strategy for Markdown Tables

The most direct and efficient method for exporting markdown tables from Obsidian to Anki involves leveraging the "ObsidianToAnki" plugin with its explicit support for "Markdown table style" regex.1 This approach minimizes complexity while capitalizing on the plugin's core strength in custom parsing.

**Implementation Steps:**

1. **Install AnkiConnect:** This is a fundamental prerequisite for all Obsidian-Anki integrations. In Anki, navigate to `Tools` > `Add-ons` > `Browse & Install...`. Search for "AnkiConnect" (code: `2055492159`) 20, install it, and restart Anki. Subsequently, configure AnkiConnect by going to
    
    `Tools` > `Add-ons` > `AnkiConnect` > `Config`. Add `"app://obsidian.md"` to the `webCorsOriginList` 1 and restart Anki once more to apply the changes.
    
2. **Install ObsidianToAnki Plugin:** In Obsidian, open `Settings` > `Community Plugins`. If `Safe Mode` is enabled, disable it temporarily. Click "Browse" and search for "ObsidianToAnki".5 Install and then enable the plugin.
    
3. **Configure ObsidianToAnki with Markdown Table Regex:** Access the ObsidianToAnki plugin settings within Obsidian. Locate the "Custom Regexps" section, which is typically part of the "Note Type Table" configuration. For the desired Anki note type (e.g., "Basic" or a custom "Table Card" type that you may have created in Anki), paste the provided regex for Markdown table style: `\|([^\n|]+)\|\n\|(?:[^\n|]+)\|\n\|([^\n|]+)\|`.8 Ensure that the 'Regex' option is checked for that specific note type.8
    
4. **Format Obsidian Tables:** Structure your Obsidian markdown tables such that they conform to the pattern recognized by the regex. The example regex provided is designed for tables with a single column for the front of the card and a single column for the back, separated by the standard markdown table header/separator line.8
    
5. **Sync to Anki:** To initiate the synchronization, click the Anki icon located in the Obsidian ribbon 1 or use the command palette to trigger the sync command. Monitor Obsidian's status bar for progress notifications.20
    

### B. Best Practices for Callouts and Tasks

To effectively convert Obsidian callouts and tasks into Anki flashcards, leveraging ObsidianToAnki's custom regex capabilities is recommended. This approach allows users to maintain their preferred Obsidian formatting while automating the Anki card creation process. The power of regex enables the definition of highly specific extraction logic, transforming the flexible nature of Obsidian notes into structured Anki cards. This is a more advanced approach but provides the precise control the user seeks over their data. The ability to use regex with multiline content 6 is crucial for handling the typical structure of callouts and tasks.

**Implementation Steps (Conceptual Regex examples, assuming an Anki note type with appropriate fields, e.g., "Question" and "Answer" for callouts, or "Task", "Due Date", "Priority" for tasks):**

1. **For Callouts:**
    
    - **Obsidian Markdown Example:**
        
        > [!question] What is the capital of France?
        > 
        > Paris.
        
    - **Conceptual Regex for `obsidian_to_anki_config.ini` (for a "Question::Answer" card):**
        
        Ini, TOML
        
        ```
        
        #... other note types...
        MyCustomCalloutNoteType = ^> \[!(?:question|info|tip|todo|example|quote|cite|abstract|summary|tldr|bug|failure|fail|missing|error|danger|warning|caution|attention|hint|important|note|seealso|success|check|done|valid|example|quote|cite|abstract|summary|tldr|bug|failure|fail|missing|error|danger|warning|caution|attention|hint|important|note|seealso|success|check|done|valid)\](?:-|\+)?\s*(.+?)\n>\s*(.+)$
        ```
        
    - **Explanation:** This regex is designed to capture the title of the callout (Group 1), which would typically serve as the "Question" field in Anki. It then captures the content within the callout (Group 2), which would populate the "Answer" field. The pattern is robust enough to account for various standard callout types (e.g., `question`, `info`, `tip`) and can also handle optional foldable markers (`-` or `+`) that might appear after the callout type.
        
2. **For Tasks:**
    
    - **Obsidian Markdown Example:**
        
        - [ ] Task: Review report outline
            
            Due Date: 2024-07-30
            
            Priority: High
            
    - **Conceptual Regex for `obsidian_to_anki_config.ini` (for a "Task::Details" card):**
        
        Ini, TOML
        
        ```
        
        #... other note types...
        MyCustomTaskNoteType = ^- \[\s*\]\s*Task:\s*(.+?)\n\s*Due Date:\s*(.+?)\n\s*Priority:\s*(.+)$
        ```
        
    - **Explanation:** This regex is crafted to extract specific pieces of information from a multi-line task block. Group 1 captures the main "Task" description. Group 2 captures the "Due Date," and Group 3 captures the "Priority." This specific pattern would necessitate a custom Anki note type with three corresponding fields to ensure accurate mapping of the extracted data.
        
3. **General Regex Considerations:**
    
    - For robust multiline content capture and to avoid accidental matches with Anki ID comments, it is often beneficial to incorporate patterns such as `(?:^.{1,3}$|^.{4}(?
