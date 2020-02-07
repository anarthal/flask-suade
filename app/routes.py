from app import app
from flask import render_template, abort
from app.models import Report
from flask_weasyprint import HTML, render_pdf
import json


@app.route('/reports/pdf/<int:report_id>')
def reports_pdf(report_id):
    """
    Endpoint for PDF reports.
    """
    report = Report.query.filter_by(id=report_id).first() # Database query
    if report is None: # Handle not found
        abort(404)

    # Render the PDF. We first render a HTML template and then use
    # flask_weasyprint to convert it into a PDF
    html = render_template('report.html', **json.loads(report.content))
    return render_pdf(HTML(string=html))

