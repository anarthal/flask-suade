from app import app
from flask import render_template, abort
from app.models import Report
from flask_weasyprint import HTML, render_pdf
import json

# TODO: add an index

@app.route('/reports/pdf/<int:report_id>')
def greeting_pdf(report_id):
    report = Report.query.filter_by(id=report_id).first()
    if report is None:
        abort(404)
    html = render_template('report.html', **json.loads(report.content))
    return render_pdf(HTML(string=html))

