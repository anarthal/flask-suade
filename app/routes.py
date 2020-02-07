from flask import render_template, abort, Response
from flask_weasyprint import HTML, render_pdf
import json
from xml.etree.ElementTree import Element, SubElement, tostring
from app import app
from app.models import Report


def _get_report(report_id):
    report = Report.query.filter_by(id=report_id).first() # Database query
    if report is None: # Handle not found
        abort(404)
    return report


def _generate_xml(report):
    root = Element('report')

    # id
    id = SubElement(root, 'id')
    id.text = str(report.id)

    content = json.loads(report.content)

    # regular string properties
    for key, value in content.items():
        if isinstance(value, str):
            elm = SubElement(root, key)
            elm.text = value

    # inventory
    inventory = SubElement(root, 'inventory')
    for item in content['inventory']:
        item_node = SubElement(inventory, 'item')
        name = SubElement(item_node, 'name')
        name.text = item['name']
        price = SubElement(item_node, 'price')
        price.text = item['price']

    return tostring(root)


@app.route('/reports/pdf/<int:report_id>')
def reports_pdf(report_id):
    """
    Endpoint for PDF reports.
    """
    report = _get_report(report_id)

    # Render the PDF. We first render a HTML template and then use
    # flask_weasyprint to convert it into a PDF
    html = render_template('report.html', **json.loads(report.content))
    return render_pdf(HTML(string=html))


@app.route('/reports/xml/<int:report_id>')
def reports_xml(report_id):
    """
    Endpoint for XML reports.
    """
    report = _get_report(report_id)
    return Response(_generate_xml(report), mimetype='text/xml')
