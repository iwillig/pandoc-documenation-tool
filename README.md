# Pandoc Documentation Tool

A cookiecutter template for creating beautiful documentation projects
using Pandoc, org-mode, and modern web styling.

## Features

- 📝 **Org-mode support** - Write in powerful org-mode syntax
- 🎨 **Beautiful styling** - Pico.css for clean, responsive design
- 🔧 **Complete build system** - Makefile-based workflow
- ✅ **Grammar checking** - Optional LanguageTool integration
- 🐍 **Python tooling** - Managed with pipenv
- 📖 **Auto-generated TOC** - From your document structure
- 🎯 **Syntax highlighting** - For code blocks
- 🔄 **Live reload** - Auto-rebuild on file changes

## Quick Start

### Prerequisites

Install cookiecutter:
```bash
pip install cookiecutter
```

### Generate Your Project

```bash
cookiecutter pandoc-documentation-tool/
```

You'll be prompted for:
- **project_name**: The name of your documentation project
- **author_name**: Your name
- **author_email**: Your email
- **project_description**: Brief description
- **include_grammar_check**: Whether to include grammar checking tool
- **create_introduction_chapter**: Whether to create a starter chapter

### Example

```bash
$ cookiecutter pandoc-documentation-tool/
project_name [My Documentation Project]: Technical Guide
author_name [Your Name]: Jane Doe
author_email [your.email@example.com]: jane@example.com
project_description [A brief description of your documentation project]: A comprehensive technical guide
document_language [en-US]: en-US
python_version [3.13]: 3.13
include_grammar_check [true]: true
create_introduction_chapter [true]: true

✓ Created technical-guide/
✓ Initialized git repository
✓ Installed dependencies
🎉 Technical Guide created successfully!
```

## What You Get

```
your-project/
├── chapters/           # Your documentation chapters (org files)
│   └── introduction.org
├── css/               # Styling files
│   ├── pico.min.css   # Pico CSS framework
│   ├── docs.css       # Custom documentation styles
│   └── highlighting.css # Syntax highlighting
├── templates/         # Pandoc HTML templates
│   └── template.html
├── tools/             # Utility scripts
│   └── check_grammar.py # Grammar checker (optional)
├── Makefile          # Build commands
├── metadata.yml      # Document metadata
├── Pipfile          # Python dependencies
├── pyproject.toml   # Python project config
└── README.md        # Project documentation
```

## System Requirements

### Required Tools

- **Python 3.13+** - For tooling
- **Pandoc** - Document conversion engine
- **Make** - Build system
- **yq** - YAML processor for Makefile

### Installation

#### macOS
```bash
brew install pandoc yq
pip install pipenv cookiecutter
```

#### Ubuntu/Debian
```bash
apt-get install pandoc make
snap install yq
pip install pipenv cookiecutter
```

#### Windows (WSL recommended)
```bash
# In WSL/Ubuntu
apt-get install pandoc make
snap install yq
pip install pipenv cookiecutter
```

## Available Commands

After generating your project:

### Building Documentation
- `make` - Build HTML documentation
- `make clean` - Remove generated files
- `make ba` - Clean and rebuild

### Development
- `make serve` - Start local server (port 4030)
- `make watch` - Auto-rebuild on changes

### Quality Checks
- `make grammar` - Check grammar (if enabled)
- `make typos` - Check for typos
- `make lint` - Lint Python code
- `make format` - Format Python code
- `make check` - Run all checks

## Writing Documentation

### Org-Mode Basics

```org
* First Level Heading
** Second Level Heading
*** Third Level Heading

*bold* /italic/ _underline_ +strikethrough+ =verbatim= ~code~

- Unordered list
  - Nested item

1. Ordered list
2. Second item

#+BEGIN_SRC python
def example():
    return "code block with syntax highlighting"
#+END_SRC

[[https://example.com][External link]]
[[#section-id][Internal link]]
```

### Adding Chapters

1. Create new `.org` file in `chapters/`
2. Add to `metadata.yml` sections list
3. Run `make` to rebuild

## Template Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Name of your documentation | My Documentation Project |
| `project_slug` | Directory name (auto-generated) | my-documentation-project |
| `author_name` | Your name | Your Name |
| `author_email` | Your email | your.email@example.com |
| `project_description` | Brief description | A brief description... |
| `document_language` | Language code for spell check | en-US |
| `python_version` | Python version requirement | 3.13 |
| `include_grammar_check` | Include grammar checking tool | true |
| `create_introduction_chapter` | Create starter content | true |

## Post-Generation

The template automatically:
1. Removes unused files based on your choices
2. Creates `.gitignore`
3. Initializes git repository
4. Installs Python dependencies
5. Checks for required system tools

## Customization

### Styling
- Edit `css/docs.css` for custom styles
- Replace `css/pico.min.css` with another CSS framework
- Modify `templates/template.html` for layout changes

### Build Process
- Edit `Makefile` for custom build steps
- Add Pandoc filters to `Pipfile` and `Makefile`
- Modify `metadata.yml` for document settings

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This cookiecutter template is open source and available under the MIT License.

## Credits

Built with:
- [Pandoc](https://pandoc.org/) - Universal document converter
- [Pico.css](https://picocss.com/) - Minimal CSS framework
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - Project templating
- [LanguageTool](https://languagetool.org/) - Grammar checking
