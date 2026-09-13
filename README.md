# GitGuard

## Overview

GitGuard is a Git Repository Health Analyzer that evaluates a repository's local Git health and connected GitHub repository information.

It analyzes branches, commits, working tree status, recent commits, and GitHub repository metrics, then generates a health score and actionable recommendations.

## Features

- Analyze current Git branch
- Count total commits
- Check working tree status
- Analyze local branches
- Display recent commits
- Generate a repository health score
- Provide actionable recommendations
- Detect GitHub remote repository
- Retrieve GitHub repository metrics
- Support HTTPS and SSH GitHub remotes
- Automated testing with pytest
- Continuous Integration with GitHub Actions

## Health Score

GitGuard calculates a repository health score out of 100 based on the current state of the repository.

| Metric | Condition | Points |
|---|---|---:|
| Working Tree | Clean | +30 |
| Commits | 5 or more | +30 |
| Commits | 3-4 | +20 |
| Commits | 1-2 | +10 |
| Branches | 3 or more | +20 |
| Branches | 2 | +10 |
| Branches | 1 | +5 |
| Recent Commits | Available | +10 |
| Current Branch | Available | +10 |

### Score Status

| Score | Status |
|---:|---|
| 90-100 | Excellent |
| 75-89 | Good |
| 50-74 | Better |
| 0-49 | Try to improve |

The score is designed to provide a quick overview of repository health rather than act as a strict code-quality metric.

## GitHub Integration

GitGuard automatically detects the GitHub repository connected to the current local repository through its Git remote.

It then retrieves repository information using the GitHub REST API.

### Retrieved GitHub Metrics

- Repository owner
- Repository name
- Stars
- Forks
- Open issues
- Repository visibility

GitGuard supports both common GitHub remote formats:

- HTTPS
- SSH

The local Git analysis and GitHub analysis are performed on the repository connected to the current working directory.

## Testing & CI

GitGuard uses `pytest` for automated testing.

The test suite covers:

- Health score status classification
- HTTPS GitHub remote parsing
- SSH GitHub remote parsing
- Repository recommendations
- Health score calculation
- Successful GitHub API response handling
- GitHub 404 error handling

### Continuous Integration

GitHub Actions automatically runs the test suite whenever changes are pushed or a pull request is created.

This helps ensure that new changes do not break existing functionality.

Current test status: **7 tests passing**

## Project Structure

```text
Gitguard/
|-- .github/
|   `-- workflows/
|       `-- tests.yml
|-- gitguard/
|   |-- __init__.py
|   `-- analyzer.py
|-- tests/
|   `-- test_analyzer.py
|-- main.py
|-- README.md
|-- .gitignore
`-- LICENSE
```

### Key Components

- `main.py` - Application entry point and output formatting
- `gitguard/analyzer.py` - Git analysis, health scoring, recommendations, and GitHub API integration
- `tests/` - Automated tests for core functionality
- `.github/workflows/tests.yml` - GitHub Actions CI workflow

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Gitguard
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install testing dependency

```bash
python -m pip install pytest
```

### 5. Run GitGuard

```bash
python main.py
```

### 6. Run automated tests

```bash
python -m pytest
```

All tests should pass before making or merging changes.

## Example Output

```text
GitGuard Repository Health Analyzer
-----------------------------------
Repository Name: Gitguard

Current Branch: main

Total Commits: 8

Working Tree Status: Dirty

Total no. of Branches: 1

Branches:
* main

Recent Commits:
80fe1db Add score and recommendation system
6451b40 Resolve merge conflict in main.py
...

Score: 55

Score Status: Better

Recommendations:
Commit your pending changes
Create/Use feature branches

GITHUB REPOSITORY
-------------------
Owner: <owner>
Repository Name: <repository>

Stars: 0
Forks: 0
Open Issues: 0
Visibility: public
```

The output provides both local Git repository analysis and connected GitHub repository information in a single report.

## Technologies Used

- Python
- Git
- GitHub
- GitHub REST API
- pytest
- GitHub Actions
- Linux / WSL

## Git Workflow

GitGuard was developed using a structured Git and GitHub workflow.

```text
Feature development
       |
Feature branch
       |
Meaningful commits
       |
Merge conflict simulation
       |
Conflict resolution
       |
Merge
       |
Automated tests
       |
GitHub Actions
       |
Verified main branch
```

The project also includes an intentionally created and resolved merge conflict to demonstrate practical Git conflict-resolution skills.

## Future Improvements

Potential future enhancements include:

- Add more repository health metrics
- Add configurable scoring rules
- Improve repository error handling
- Add support for additional Git hosting platforms
- Generate machine-readable reports
- Add a richer command-line interface
