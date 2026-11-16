# Exam Preparation for BCA

Question papers, textbook blocks, converted study notes, and previous-year-question (PYQ) analysis for BCA examination preparation.

## Subjects

### MCS-206 - Object Oriented Programming using Java

- [Complete PYQ analysis and exam guide](MCS-206/MCS-206_Complete_PYQ_Analysis.md)
- Previous-year question papers from December 2021 through June 2026
- Four textbook blocks in [`booke/`](MCS-206/booke/)
- Extracted, searchable text in [`work/`](MCS-206/work/)
- Topics include Java fundamentals, OOP, inheritance, exceptions, multithreading, I/O, collections, GUI programming, and JDBC

### MSEI-023 - Cyber Security

- [Complete PYQ analysis report](MSEI-023/PYQ_ANALYSIS_REPORT.md)
- Previous-year question papers from June 2021 through June 2026
- Four textbook blocks in [`books/`](MSEI-023/books/)
- [`analyze_questions.py`](MSEI-023/analyze_questions.py) for topic-frequency analysis
- Topics include social engineering, database security, web security, internet security, VAPT, ransomware, cloud security, and cyber-security audits

## Repository structure

```text
.
├── MCS-206/
│   ├── *.pdf                         # Question papers
│   ├── booke/                        # Textbook blocks
│   ├── work/                         # Searchable extracted text
│   └── MCS-206_Complete_PYQ_Analysis.md
├── MSEI-023/
│   ├── *.pdf                         # Question papers
│   ├── books/                        # Textbook blocks
│   ├── PYQ_ANALYSIS_REPORT.md
│   └── analyze_questions.py
└── README.md
```

## Suggested workflow

1. Start with the relevant subject's PYQ analysis report.
2. Use the priority topics and revision checklist to plan study sessions.
3. Read the corresponding textbook block for concepts and examples.
4. Practise answering the linked previous-year papers under timed conditions.
5. Use the extracted text files for quick searching when revising.

## Running the MSEI-023 analysis script

The script uses only Python's standard library:

```powershell
cd MSEI-023
python analyze_questions.py
```

It prints topic frequencies and groups questions by paper and marks category.

## File formats

- PDF files contain the original question papers and textbook blocks.
- Markdown files contain manually prepared analysis and revision material.
- Text files contain searchable extracts of MCS-206 material.
- PDF files are tracked with [Git LFS](https://git-lfs.com/).

## Disclaimer

The analyses describe historical question-paper patterns and are intended as study aids. Repeated topics and frequency rankings do not guarantee future questions. Always prepare the complete syllabus and verify the current examination pattern with official university information.
