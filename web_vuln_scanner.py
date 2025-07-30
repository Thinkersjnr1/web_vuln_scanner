from flask import Flask, request, render_template, jsonify, send_file
import sqlite3
from zapv2 import ZAPv2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

# Initialize OWASP ZAP API
zap = ZAPv2(apikey='gpqomq19a2h0pvlgpfsk459qis', proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})

# Global variables to track scan progress
current_scan = {'type': None, 'id': None, 'progress': 0}

# Database setup
def init_db():
    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities
                 (id INTEGER PRIMARY KEY, url TEXT, vuln_type TEXT, description TEXT, mitigation TEXT)''')
    conn.commit()
    conn.close()

# Mitigation suggestions
def get_mitigation(vuln_type):
    mitigations = {
        'SQL Injection': 'Use parameterized queries and prepared statements.',
        'Cross Site Scripting': 'Implement input sanitization and output encoding.',
        'Cross-Site Request Forgery': 'Use CSRF tokens and validate requests.'
    }
    return mitigations.get(vuln_type, 'Review and apply best practices.')

# Route for starting scan
@app.route('/start_scan', methods=['POST'])
def start_scan():
    global current_scan
    target_url = request.form['url']
    
    # Start ZAP scan
    zap.urlopen(target_url)
    scan_id = zap.spider.scan(url=target_url)
    current_scan = {'type': 'spider', 'id': scan_id, 'progress': 0}
    
    # Wait for spider to complete
    while int(zap.spider.status(scan_id)) < 100:
        current_scan['progress'] = int(zap.spider.status(scan_id))
        pass
    
    # Start active scan
    scan_id = zap.ascan.scan(url=target_url)
    current_scan = {'type': 'active', 'id': scan_id, 'progress': 0}
    
    # Wait for active scan to complete
    while int(zap.ascan.status(scan_id)) < 100:
        current_scan['progress'] = int(zap.ascan.status(scan_id))
        pass
    
    # Retrieve alerts
    alerts = zap.core.alerts(baseurl=target_url)
    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    for alert in alerts:
        vuln_type = alert.get('alert')
        description = alert.get('description')
        mitigation = get_mitigation(vuln_type)
        c.execute("INSERT INTO vulnerabilities (url, vuln_type, description, mitigation) VALUES (?, ?, ?, ?)",
                  (target_url, vuln_type, description, mitigation))
    conn.commit()
    conn.close()
    
    current_scan = {'type': None, 'id': None, 'progress': 100}
    return render_template('results.html', alerts=alerts, url=target_url)

# Route for checking scan progress
@app.route('/progress', methods=['GET'])
def get_progress():
    global current_scan
    if current_scan['type'] == 'spider':
        progress = int(zap.spider.status(current_scan['id']))
    elif current_scan['type'] == 'active':
        progress = int(zap.ascan.status(current_scan['id']))
    else:
        progress = current_scan['progress']
    return jsonify({'progress': progress})

# Route for generating PDF report
@app.route('/report/<url>')
def generate_report(url):
    conn = sqlite3.connect('vuln.db')
    c = conn.cursor()
    c.execute("SELECT * FROM vulnerabilities WHERE url=?", (url,))
    vulns = c.fetchall()
    conn.close()

    pdf_file = f"report_{url.replace('http://', '').replace('/', '_')}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Vulnerability Report for {url}")
    y = 700
    for vuln in vulns:
        c.drawString(100, y, f"Vulnerability: {vuln[2]}")
        c.drawString(100, y-20, f"Description: {vuln[3]}")
        c.drawString(100, y-40, f"Mitigation: {vuln[4]}")
        y -= 60
    c.save()
    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
