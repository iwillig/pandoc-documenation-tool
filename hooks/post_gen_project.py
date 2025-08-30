#!/usr/bin/env python
"""Post-generation hook for the Pandoc Documentation Tool cookiecutter template."""

import os
import subprocess
import sys
from pathlib import Path


def remove_empty_files():
    """Remove empty conditional files created by cookiecutter."""
    # Remove empty grammar checker if not included
    if not {{ cookiecutter.include_grammar_check }}:
        grammar_file = Path("tools/check_grammar.py")
        if grammar_file.exists() and grammar_file.stat().st_size == 0:
            grammar_file.unlink()
            print("✓ Removed unused grammar checker")
    
    # Remove empty introduction if not created
    if not {{ cookiecutter.create_introduction_chapter }}:
        intro_file = Path("chapters/introduction.org")
        if intro_file.exists() and intro_file.stat().st_size == 0:
            intro_file.unlink()
            print("✓ Removed unused introduction chapter")


def initialize_git():
    """Initialize a git repository."""
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit from Pandoc Documentation Tool"],
            check=True,
            capture_output=True
        )
        print("✓ Initialized git repository")
        return True
    except subprocess.CalledProcessError:
        print("⚠ Could not initialize git repository")
        return False
    except FileNotFoundError:
        print("⚠ Git not found - skipping repository initialization")
        return False


def install_dependencies():
    """Install Python dependencies using pipenv."""
    try:
        print("Installing Python dependencies...")
        subprocess.run(
            ["pipenv", "install", "--dev"],
            check=True,
            capture_output=False
        )
        print("✓ Installed Python dependencies")
        return True
    except subprocess.CalledProcessError:
        print("⚠ Could not install dependencies automatically")
        print("  Run 'pipenv install --dev' manually")
        return False
    except FileNotFoundError:
        print("⚠ Pipenv not found - please install it first:")
        print("  pip install pipenv")
        return False


def check_requirements():
    """Check if required tools are installed."""
    requirements = {
        "pandoc": "Document conversion",
        "yq": "YAML processing for Makefile",
        "make": "Build system"
    }
    
    missing = []
    for cmd, description in requirements.items():
        try:
            subprocess.run(
                ["which", cmd],
                check=True,
                capture_output=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing.append(f"  - {cmd}: {description}")
    
    if missing:
        print("\n⚠ Missing required tools:")
        print("\n".join(missing))
        print("\nInstall them using your package manager:")
        print("  macOS: brew install pandoc yq")
        print("  Ubuntu: apt-get install pandoc && snap install yq")
    else:
        print("✓ All required tools found")
    
    return len(missing) == 0


def create_gitignore():
    """Create a .gitignore file."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Pipenv
Pipfile.lock

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Build outputs
index.html
index.md
build_readme.md
*.log

# Ruff
.ruff_cache/
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    print("✓ Created .gitignore file")


def print_next_steps():
    """Print helpful next steps for the user."""
    print("\n" + "="*50)
    print("🎉 {{ cookiecutter.project_name }} created successfully!")
    print("="*50)
    
    print("\n📝 Next steps:")
    print("  1. cd {{ cookiecutter.project_slug }}")
    
    if not Path("Pipfile.lock").exists():
        print("  2. pipenv install --dev")
    
    print("  3. make              # Build documentation")
    print("  4. make serve        # Preview at http://localhost:4030")
    
    print("\n📚 Quick tips:")
    print("  - Write chapters in chapters/*.org")
    print("  - Update metadata.yml to add new chapters")
    print("  - Run 'make watch' for auto-rebuild")
    {% if cookiecutter.include_grammar_check -%}
    print("  - Run 'make grammar' to check grammar")
    {%- endif %}
    
    print("\n📖 Documentation: See README.md for full details")
    print("\nHappy writing! ✨")


def main():
    """Run all post-generation tasks."""
    print("\n🚀 Setting up {{ cookiecutter.project_name }}...\n")
    
    # Clean up empty files
    remove_empty_files()
    
    # Create .gitignore
    create_gitignore()
    
    # Check requirements
    check_requirements()
    
    # Install dependencies
    install_dependencies()
    
    # Initialize git
    initialize_git()
    
    # Print next steps
    print_next_steps()


if __name__ == "__main__":
    main()