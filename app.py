from flask import Flask, render_template, request, redirect, send_file, flash
from models import Session, QueryLog
from scraper import fetch_case_metadata

app = Flask(__name__)
app.secret_key = 'replace-with-envkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    result = fetch_case_metadata(case_type, case_number, filing_year)

    # Log in DB
    db = Session()
    log = QueryLog(case_type=case_type, case_number=case_number, filing_year=filing_year,
                   court='Delhi High Court', raw_response=result.get('raw_html', ''))
    db.add(log)
    db.commit()

    if 'error' in result:
        flash("Error: " + result['error'])
        return redirect('/')

    return render_template('results.html', details=result)

@app.route('/download/<path:pdf_url>')
def download(pdf_url):
    # Would fetch and serve PDF
    return send_file(pdf_url, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
