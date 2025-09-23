# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Data Structures Learning Repository** containing educational materials for learning data structures and algorithms. It is structured as a comprehensive curriculum with markdown-based documentation and LaTeX presentation materials.

## Repository Structure

The repository follows a modular educational approach:

- **`topics/`** - Core learning modules with individual markdown files for each data structure and algorithm topic
- **`slides/BeamerTemplate/`** - LaTeX Beamer presentation template for creating educational slides
- **`slides/[Topic]/`** - Topic-specific presentation materials (e.g., `slides/Stack/`)
- **`assignments/`** - Practical coding assignments with implementations, tests, and documentation
- **`Time/`** - Time and space complexity analysis materials
- **`Roadmap.md`** - Master curriculum guide that outlines the complete learning path

## Key Architecture Components

### Educational Content Organization
- **Sequential Learning Path**: Content follows a progression from foundations (`01-Foundations.md`) through advanced topics (`09-Next-Steps.md`)
- **Cross-Referenced Topics**: Individual topic files (e.g., `Arrays.md`, `Trees.md`, `Hash-Tables.md`) provide deep-dive content that complements the sequential modules
- **Wikilink Structure**: Uses `[[topic]]` syntax for internal cross-references between related concepts

### Presentation System
- **BeamerTemplate**: Complete LaTeX presentation framework with modular theme components
- **Theme Structure**: Separated into individual `.sty` files for colors, fonts, inner/outer themes for customization
- **Configuration Files**: Modular configs in `configs/` directory for title pages and global settings

## Common Development Commands

### Python Assignment Testing
```bash
# Run unit tests for assignments (e.g., stack assignment)
cd assignments/stack/
python test_stack.py

# Run application demonstrations
python application.py
```

### LaTeX Presentation Compilation
```bash
# Compile Beamer presentations
cd slides/BeamerTemplate/
pdflatex CleanEasy.tex

# Alternative compilation
latexmk CleanEasy.tex

# Compile specific topic presentations
cd slides/Stack/
pdflatex stack.tex
```

### Content Development
- No build process required for markdown content
- Use any markdown editor or preview tool
- Cross-references use wikilink format: `[[Topic-Name]]`

## Content Guidelines

### Markdown Structure
- Each topic file should follow the established pattern with "Knowledge Points" and "Details" sections
- Use clear hierarchical headings (##, ###) for organization
- Include practical examples and implementation notes
- Cross-reference related topics using wikilink syntax

### Learning Path Integration
- New topics should be integrated into the main `Roadmap.md` sequence
- Consider both sequential placement and individual topic depth
- Maintain the progression from basic to advanced concepts

### LaTeX Presentations
- Use the provided CleanEasy theme for consistency
- Separate content into modular components when possible
- Follow the established package and configuration structure in `CleanEasy.tex`

### Assignment Structure
- Each assignment should include three core files:
  - Implementation file (e.g., `stack.py`) with complete working code
  - Application file (e.g., `application.py`) demonstrating practical use cases
  - Test file (e.g., `test_stack.py`) with comprehensive unit tests
- Include detailed README.md explaining concepts, implementation trade-offs, and learning objectives
- Provide student template versions by removing core implementations for educational exercises