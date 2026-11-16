# BCA Exam Preparation Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Git LFS](https://img.shields.io/badge/Git%20LFS-Tracked-blue.svg)](https://git-lfs.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![IGNOU](https://img.shields.io/badge/IGNOU-BCA%20%7C%20MSCIS%20%7C%20PGDIS-orange.svg)](https://ignou.ac.in/)

A comprehensive collection of previous-year question papers, textbook materials, extracted study notes, and detailed frequency analyses for BCA (and related IGNOU) examination preparation.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Subjects Covered](#subjects-covered)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Screenshots / Demo](#screenshots--demo)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## Project Overview

This repository serves as a centralized study resource for students preparing for **IGNOU BCA (Bachelor of Computer Applications)** and related postgraduate (MSCIS, PGDIS) term-end examinations. It addresses the common problem of scattered study materials by consolidating:

- **Previous Year Question (PYQ) papers** — official question papers spanning 9–10 years
- **Textbook blocks** — complete course material in PDF format
- **Searchable extracted text** — OCR-processed content for quick keyword searching
- **Detailed frequency analyses** — topic-wise occurrence counts, priority classifications, repeated questions, and structured revision plans

The analyses are derived from **manual review of every question** across all available papers, not automated heuristics, ensuring accuracy in topic mapping and frequency counts.

---

## Subjects Covered

### MCS-206 — Object Oriented Programming using Java
| Detail | Information |
|--------|-------------|
| **Program** | BCA |
| **Papers Analyzed** | 10 (Dec 2021 – June 2026) |
| **Textbook Blocks** | 4 Blocks (16 Units) in `booke/` |
| **Extracted Text** | Available in `work/` (blocks + all papers) |
| **Analysis Report** | [`MCS-206_Complete_PYQ_Analysis.md`](MCS-206/MCS-206_Complete_PYQ_Analysis.md) |
| **Key Topics** | Java fundamentals, OOP, inheritance, polymorphism, exception handling, multithreading, I/O streams, collections, GUI (AWT/Swing/JavaFX), JDBC |

### MSEI-023 — Cyber Security
| Detail | Information |
|--------|-------------|
| **Program** | MSCIS / PGDIS |
| **Papers Analyzed** | 10 (June 2021 – June 2026) |
| **Textbook Blocks** | 4 Blocks (16 Units) in `books/` |
| **Analysis Script** | [`analyze_questions.py`](MSEI-023/analyze_questions.py) (stdlib only) |
| **Analysis Report** | [`PYQ_ANALYSIS_REPORT.md`](MSEI-023/PYQ_ANALYSIS_REPORT.md) |
| **Key Topics** | Social engineering, database security, web security (XSS/SQLi), internet security, VAPT, ransomware, cloud security, zero-day, Kerberos, PKI, cyber security audit (ISO 27001) |

### BCS-040 — Statistical Techniques
| Detail | Information |
|--------|-------------|
| **Program** | BCA |
| **Papers Analyzed** | 9 (June 2021 – Dec 2025; June 2023 unavailable) |
| **Textbook Blocks** | 4 Blocks (14 Units) in `booke/` |
| **Extracted Text** | Available in root (all papers as `.txt`) |
| **Analysis Report** | [`BCS-040_Complete_PYQ_Analysis.md`](BCS-040/BCS-040_Complete_PYQ_Analysis.md) |
| **Key Topics** | Descriptive statistics, probability, distributions, sampling, estimation, hypothesis testing (Z/t/F/χ²), ANOVA, regression, time series forecasting, SQC, sampling techniques (SRS, systematic, stratified, cluster) |

---

## Features

- **Complete PYQ Coverage** — 29 question papers across 3 subjects (9–10 years each)
- **Textbook Integration** — All 4 blocks per subject (12 blocks total, 46 units) as PDFs
- **Searchable Content** — Extracted text files for MCS-206 and BCS-040 enabling instant keyword search
- **Automated Analysis Tool** — `analyze_questions.py` for MSEI-023 (pure Python stdlib, no dependencies)
- **Frequency Analysis** — Topic occurrence counts across all papers, ranked by priority (High/Medium/Low)
- **Repeated Question Detection** — Exact and near-exact question repeats identified across years
- **Chapter-wise Mapping** — Every topic mapped to textbook block and unit
- **Marks-wise Breakdown** — Questions categorized by 1/2/5/10-mark patterns
- **Revision Checklists** — Must-know, should-know, nice-to-know classifications with practice programs
- **Study Plans** — 7-day structured revision schedules per subject
- **Git LFS** — Large PDF files tracked efficiently without bloating repository history

---

## Tech Stack

| Category | Tools / Technologies |
|----------|---------------------|
| **Version Control** | Git, Git LFS |
| **Analysis Script** | Python 3 (standard library only: `re`, `collections`) |
| **Documentation** | Markdown (GitHub-flavored) |
| **File Formats** | PDF (papers, textbooks), Markdown (analysis), TXT (extracted text) |
| **Platform** | Cross-platform (Windows, Linux, macOS) |

---

## Project Structure

```text
.
├── BCS-040/                          # Statistical Techniques
│   ├── *.pdf                         # 11 question papers (Jun 2021 – Dec 2025)
│   ├── booke/                        # 14 textbook units (Unit-1.pdf … Unit-14.pdf)
│   ├── *.txt                         # Extracted text for all 11 papers
│   └── BCS-040_Complete_PYQ_Analysis.md
│
├── MCS-206/                          # OOP using Java
│   ├── *.pdf                         # 10 question papers (Dec 2021 – Jun 2026)
│   ├── booke/                        # 4 textbook blocks (Block-1.pdf … Block-4.pdf)
│   ├── work/                         # Extracted text (4 blocks + 10 papers)
│   ├── MCS-206_Complete_PYQ_Analysis.md
│   └── MCS-206_Java_PYQ_Analysis_Exam_Guide.pdf
│
├── MSEI-023/                         # Cyber Security
│   ├── *.pdf                         # 10 question papers (Jun 2021 – Jun 2026)
│   ├── books/                        # 4 textbook blocks (Block-1.pdf … Block-4.pdf)
│   ├── analyze_questions.py          # Frequency analysis script (stdlib)
│   └── PYQ_ANALYSIS_REPORT.md
│
├── .gitattributes                    # Git LFS configuration for *.pdf
├── .gitignore
└── README.md
```

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `*/booke/` or `*/books/` | Original textbook PDFs (IGNOU course material) |
| `*/work/` | OCR-extracted searchable text (MCS-206 only) |
| `BCS-040/*.txt` | Extracted question paper text (BCS-040 only) |
| Root of each subject | Question papers, analysis reports, auxiliary files |

---

## Installation & Setup

### Prerequisites

- **Git** (with [Git LFS](https://git-lfs.com/) installed)
- **Python 3.8+** (only required for MSEI-023 analysis script)
- **PDF Reader** (for viewing question papers and textbooks)

### Clone the Repository

```bash
# Clone with LFS files (recommended)
git lfs install
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Or clone without LFS first, then pull large files
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
git lfs pull
```

### Verify LFS Files

```bash
# Check that PDF files are actual files (not LFS pointers)
ls -lh MCS-206/*.pdf MSEI-023/*.pdf BCS-040/*.pdf
# File sizes should be > 100 KB, not 133 bytes
```

### Environment Variables

No environment variables or `.env` files are required. The analysis script uses only the Python standard library.

---

## Usage

### View Analysis Reports

Open the Markdown files directly on GitHub or locally with any Markdown viewer:

```bash
# MCS-206 (Java)
cat MCS-206/MCS-206_Complete_PYQ_Analysis.md

# MSEI-023 (Cyber Security)
cat MSEI-023/PYQ_ANALYSIS_REPORT.md

# BCS-040 (Statistical Techniques)
cat BCS-040/BCS-040_Complete_PYQ_Analysis.md
```

### Run MSEI-023 Frequency Analysis

The script uses only Python's standard library — no `pip install` needed.

```bash
cd MSEI-023
python analyze_questions.py
```

**Output:** Topic frequencies, papers where each topic appeared, and marks categories printed to stdout.

### Search Extracted Text (MCS-206 & BCS-040)

```bash
# Search for a topic across all MCS-206 extracted files
grep -ri "multithreading" MCS-206/work/

# Search BCS-040 question papers
grep -ri "anova" BCS-040/*.txt
```

### Suggested Study Workflow

1. **Start** with the subject's PYQ analysis report (`*_Complete_PYQ_Analysis.md` or `PYQ_ANALYSIS_REPORT.md`)
2. **Review** the priority topics and revision checklist to plan study sessions
3. **Read** the corresponding textbook block PDF for concepts and examples
4. **Practice** answering the linked previous-year papers under timed conditions
5. **Use** extracted text files for quick keyword searching during revision
6. **Run** the analysis script (MSEI-023) to regenerate frequency data if needed

---

## Screenshots / Demo

| Analysis Report Preview | Frequency Analysis Output |
|:-----------------------:|:-------------------------:|
| ![MCS-206 Analysis](docs/screenshots/mcs206-analysis.png) | ![MSEI-023 Script](docs/screenshots/msei023-script.png) |
| *MCS-206 frequency tables, repeated questions, revision checklist* | *Topic counts, paper mappings, marks distribution* |

> **Note:** Screenshots are placeholders. Add actual images to `docs/screenshots/` and update the paths above.

**Live Demo:** Not applicable — this is a static document repository. View rendered Markdown directly on GitHub.

---

## Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add: description of change"`
4. **Push** to your fork: `git push origin feature/your-feature`
5. **Open** a Pull Request

### Contribution Ideas

- Add missing question papers (e.g., BCS-040 June 2023)
- Provide extracted text for MSEI-023 papers
- Improve analysis reports with additional insights
- Add support for more subjects (MCS-011, MCS-012, etc.)
- Create a unified analysis script for all subjects
- Translate analysis reports to other languages

### Pull Request Guidelines

- Keep changes focused and atomic
- Update relevant analysis reports if adding new papers
- Ensure PDF files are tracked via Git LFS (`git lfs track "*.pdf"`)
- Do not commit API keys, passwords, or personal information
- Follow the existing Markdown formatting style

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

> **Note:** The question papers and textbook materials are copyright of **IGNOU (Indira Gandhi National Open University)**. They are included here for **educational and personal study purposes only** under fair use. The analysis reports, extracted text, and scripts are original work licensed under MIT.

---

## Disclaimer

> **IMPORTANT:** All analyses in this repository describe **historical question-paper patterns** and are intended **solely as study aids**.
>
> - Repeated topics and frequency rankings **do not guarantee** future questions.
> - The university **may change** examination patterns, introduce new topics, or alter weightage at any time.
> - **Always prepare the complete syllabus** as per the official IGNOU prospectus.
> - Verify the current examination pattern with official university notifications before the exam.
> - This repository is **not affiliated with, endorsed by, or sponsored by IGNOU**.

---

## Quick Reference: Subject Comparison

| Aspect | MCS-206 (Java) | MSEI-023 (Cyber Security) | BCS-040 (Statistics) |
|--------|----------------|---------------------------|----------------------|
| **Program** | BCA | MSCIS / PGDIS | BCA |
| **Papers** | 10 | 10 | 9 |
| **Exam Marks** | 100 (70% weight) | 50 | 50 |
| **Pattern** | Q1: 8×5=40, Q2-5: 3×20 | Mixed → Descriptive (2022+) | Sec A: 4×5, Sec B: 3×10 |
| **High-Priority Topics** | Inheritance, Exceptions, Multithreading, JDBC, Polymorphism | Social Engineering, SQLi, XSS/XSRF, VAPT, Ransomware | ANOVA, Chi-square, Regression, Time Series |
| **Analysis Script** | No | Yes (`analyze_questions.py`) | No |
| **Extracted Text** | Yes (`work/`) | No | Yes (root `*.txt`) |

---

*Last updated: November 2026*  
*Maintained for BCA/MSCIS/PGDIS exam preparation*