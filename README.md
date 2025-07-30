# Web Vulnerability Scanner Dashboard

**A Python-based web application built on Kali Linux to automate vulnerability scanning using OWASP ZAP, display results in an interactive dashboard, and generate PDF reports with mitigation suggestions. This project showcases skills in penetration testing, API integration, web development, and cybersecurity analysis, making it an ideal portfolio piece for cybersecurity job applications.**

# Project Overview

**The Web Vulnerability Scanner Dashboard automates the process of scanning web applications for vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF). It leverages OWASP ZAP’s API for scanning, Flask for the web interface, SQLite for data storage, and ReportLab for PDF report generation. A key feature is the real-time progress indicator, showing scan completion percentage to enhance user experience.**

# Features

Automated Scanning: Performs spider and active scans using OWASP ZAP to identify vulnerabilities.

Interactive Dashboard: Displays a form to input target URLs, a real-time progress indicator (e.g., "Scanning... 45%"), and a results table with vulnerabilities, descriptions, and mitigations.

Progress Tracking: Shows scan progress percentage, updated every 2 seconds via API polling.

Report Generation: Exports scan results as a PDF with detailed vulnerability information and mitigation suggestions.

Data Persistence: Stores scan results in an SQLite database for easy retrieval.

Ethical Design: Built for use on authorized test environments like testphp.vulnweb.com.

# Technologies Used





Backend: Python, Flask, OWASP ZAP (via zapv2 library), SQLite, ReportLab

Frontend: HTML, CSS, JavaScript

Environment: Kali Linux

Key Libraries: flask, zapv2, reportlab, sqlite3

# Development Process

The project was developed in iterative steps to ensure functionality, usability, and professionalism:





# Environment Setup:

Install OWASP ZAP on Kali Linux (sudo apt install zaproxy).

Configur ZAP to run in daemon mode for API access.

Install Python dependencies: pip install flask zapv2 reportlab.

# Backend Development:

Created web_vuln_scanner.py using Flask to handle routes for scanning, progress tracking, and report generation.

Integrated OWASP ZAP’s API to perform spider and active scans, retrieving vulnerabilities like SQL Injection, XSS, and CSRF.

Implemented SQLite database to store scan results.

Added a /progress endpoint to return real-time scan progress.

# Frontend Development:

Designed index.html with a form for URL input, a loading spinner, and a progress percentage display.

Built results.html to show a table of vulnerabilities with mitigation suggestions.

Used CSS to maintain a consistent dark theme (#000000 background, #3533cd accents).

Added JavaScript in index.html to poll the /progress endpoint every 2 seconds and update the percentage.

# Report Generation:

Integrated ReportLab to generate PDF reports from SQLite data, including vulnerability details and mitigations.

User Experience Enhancements:

Added a "Scanning..." message with a CSS spinner to indicate scan activity.

Implemented real-time progress updates to show scan completion percentage (e.g., "Scanning... 45%").

Disabled the submit button during scanning to prevent multiple submissions.

# Testing:

Tested on testphp.vulnweb.com, a safe environment for ethical hacking.

Verified scan times (~6-13 minutes for small sites), progress updates, and PDF output.

Ensured compatibility with Kali Linux and ZAP’s default settings.

# Prerequisites

Kali Linux with OWASP ZAP installed (sudo apt update && sudo apt install zaproxy).

Python 3 and pip installed.

Required Python packages: flask, zapv2, reportlab.

OWASP ZAP API key (found in ~/.ZAP/config.xml or ZAP GUI under Tools > Options > API).

# Setup Instructions

Clone the Repository:

git clone https://github.com/Thinkersjnr1/web-vuln-scanner.git

cd web-vuln-scanner

# Install Dependencies:

pip install flask zapv2 reportlab

# Start OWASP ZAP in Daemon Mode:

zap.sh -daemon -port 8080 -host 0.0.0.0

# Retrieve your ZAP API key 

~/.ZAP/config.xml or ZAP GUI.

# Update the apikey 

in web_vuln_scanner.py (line 10) with your key.



# Organize Project Files:

Place web_vuln_scanner.py in the root directory.

Create a templates folder and place index.html and results.html inside.

Ensure README.md is in the root directory.

# Run the Application:

python3 web_vuln_scanner.py

Access the dashboard at http://localhost:5000.

# Usage

Start a Scan:

Open http://localhost:5000 in a browser.

Enter a target URL (e.g., http://testphp.vulnweb.com) and click "Scan Now".

# Monitor Progress:

**A "Scanning..." message with a spinner and percentage (e.g., "Scanning... 45%") appears**.

**Progress updates every 2 seconds until the scan completes (~6-13 minutes for small sites).**

# View Results:

Results display in a table with vulnerabilities, descriptions, and mitigations.

Click **Download PDF Report** to save a PDF of the findings.

# Ethical Considerations:

Only scan websites you have explicit permission to test (e.g., testphp.vulnweb.com or your own setup).

# Example Workflow

Input URL: http://testphp.vulnweb.com

Scan Progress: Spidering (0-100%), then Active Scanning (0-100%)

Output: Table with vulnerabilities (e.g., SQL Injection, XSS), mitigations, and a downloadable PDF report

Sample Mitigation: "SQL Injection: Use parameterized queries and prepared statements."

# Notes

Scan Time: Small sites (~10-20 pages) take ~6-13 minutes; larger sites may take 20-40+ minutes.

# Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a feature branch (git checkout -b feature/new-feature).

Commit changes (git commit -m "Add new feature").

Push to the branch (git push origin feature/new-feature).

Open a pull request with a detailed description.

Please ensure code follows PEP 8 standards and includes tests for new features.

# License

see license

# Contact

For questions or collaboration, reach out via yewenusewedo@gmail.com or www.linkedin.com/in/daniel-yewenu-45a370250 .

**“Securing the web, one scan at a time.”**

# Daniel Yewenu 2025
