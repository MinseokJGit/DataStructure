# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Data Structures Learning Repository** containing educational materials for learning data structures and algorithms, structured as a comprehensive curriculum with markdown documentation, Python assignments, and LaTeX presentations.

## Repository Structure

- **`Roadmap.md`** - Master curriculum guide outlining the complete learning progression (Foundations → Advanced Structures → Algorithms → Applications)
- **`topics/`** - Individual markdown files for each data structure/algorithm topic, using wikilink cross-references (`[[Topic-Name]]`)
  - Sequential modules: `01-Foundations.md` through `09-Next-Steps.md`
  - Standalone deep-dives: `Arrays.md`, `Trees.md`, `Hash-Tables.md`, etc.
- **`assignments/`** - Python coding assignments with multiple implementations:
  - `stack/`, `queue/`, `linked_list/`, `tree/`, `graph/`, `trie/`
  - Each follows the three-file pattern (see below)
- **`slides/BeamerTemplate/`** - Reusable LaTeX Beamer theme with modular `.sty` files in `theme/` subdirectory
- **`slides/[Topic]/`** - Topic-specific presentations that use the BeamerTemplate theme

## Common Development Commands

### Python Assignments
```bash
# Run unit tests for an assignment (use absolute path from repo root)
python /Users/minseokjeon/dgistpl/DataStructure/assignments/stack/test_stack.py
python /Users/minseokjeon/dgistpl/DataStructure/assignments/queue/test_queue.py

# Run demonstrations
python /Users/minseokjeon/dgistpl/DataStructure/assignments/stack/application.py

# Note: Tests use function-based approach, not unittest classes
# The test files define test functions and run them with a custom runner
```

### LaTeX Presentations
```bash
# Compile the BeamerTemplate example
cd slides/BeamerTemplate/
pdflatex CleanEasy.tex
# or: latexmk CleanEasy.tex

# Compile topic-specific presentations
cd slides/Stack/
pdflatex stack.tex

# Note: Topic presentations use \input@path to reference ../BeamerTemplate/theme/
```

## Key Architecture Patterns

### Assignment Structure (Three-File Pattern)
Each assignment follows this mandatory structure (see `assignments/stack/` and `assignments/queue/` as reference):

1. **`[topic].py`** - Complete implementation with multiple approaches
   - Multiple implementation variants (e.g., ArrayStack vs LinkedListStack)
   - Utility functions demonstrating practical applications
   - Include comparison comments on time/space trade-offs

2. **`application.py`** - Real-world demonstrations
   - Must show 4-6 practical use cases
   - Include performance comparisons when multiple implementations exist
   - Demonstrates how the data structure solves real problems

3. **`test_[topic].py`** - Comprehensive tests using function-based approach
   - Define test functions: `def test_[feature]():`
   - Use assert statements for verification
   - Custom test runner at the end of file
   - Test all operations, edge cases, and exception handling
   - Include tests for utility functions

4. **`README.md`** - Comprehensive assignment documentation
   - Implementation comparison table with time/space complexity
   - Learning objectives
   - Student template instructions (how to hide implementations for exercises)
   - Common pitfalls and extension ideas
   - Real-world applications section
   - Performance characteristics summary

### Topic Documentation Pattern
Each topic file in `topics/` follows this structure:
1. One-line description at the top
2. **Knowledge Points** section with wikilinks: `[[concept]]`
3. **Details** section with subsections (###) for each knowledge point
4. Code examples in Details section
5. Complexity analysis where relevant

### Presentation Theme System
The BeamerTemplate provides a modular theme:
- **Theme files** in `slides/BeamerTemplate/theme/`:
  - `beamerthemeCleanEasy.sty` - Main theme
  - `beamercolorthemeCleanEasy.sty` - Color scheme
  - `beamerfontthemeCleanEasy.sty` - Font settings
  - `beamerinnerthemeCleanEasy.sty` - Inner elements
  - `beamerouterthemeCleanEasy.sty` - Outer elements

- **Configuration pattern** for topic presentations:
  - Reference the theme using: `\makeatletter \def\input@path{{../BeamerTemplate/theme/}} \makeatother`
  - Use `\usetheme{CleanEasy}` in the preamble
  - Import configs: `\input{../BeamerTemplate/configs/configs}`
  - Topic-specific customization can be added in local configs if needed

## Content Development Workflows

### Adding a New Assignment
1. Create `assignments/[topic]/` directory
2. Implement the three-file pattern (`[topic].py`, `application.py`, `test_[topic].py`)
3. Write README.md following `assignments/queue/README.md` structure (most comprehensive example)
4. Include in README:
   - Implementation comparison table
   - Real-world applications section
   - Performance characteristics summary
   - Student template code
   - Extension ideas
5. Update `Roadmap.md` to reference the new assignment in the appropriate module

### Adding a New Topic
1. Create `topics/[Topic-Name].md` with Knowledge Points and Details sections
2. Use wikilink syntax `[[concept]]` for cross-references
3. Add the topic to `Roadmap.md` in the appropriate module (## 3-9)
4. Consider creating a matching presentation in `slides/[Topic]/`

### Creating a New Presentation
1. Create `slides/[Topic]/` directory
2. Reference the theme: `\makeatletter \def\input@path{{../BeamerTemplate/theme/}} \makeatother`
3. Use `\usetheme{CleanEasy}` for consistent styling
4. Import shared configs: `\input{../BeamerTemplate/configs/configs}`
5. Set presentation metadata (title, author, institute, date)

## Technical Requirements

- **Python**: 3.x
- **Testing**: Function-based tests with assert statements, not unittest.TestCase classes
- **LaTeX**: Standard distribution with Beamer package
- **Content Format**: Markdown with wikilink support for cross-references

## Important Notes

- The test files use function-based testing with assert statements, not unittest classes
- When running tests, use absolute paths from repository root
- `assignments/stack/README.md` and `assignments/queue/README.md` serve as canonical references for creating new assignments
- Queue assignment README is the most comprehensive with grading rubric and detailed sections
- Wikilinks (`[[Topic-Name]]`) are used throughout for cross-referencing but require a compatible markdown viewer
- The learning path in `Roadmap.md` is sequential but topic files can be studied independently