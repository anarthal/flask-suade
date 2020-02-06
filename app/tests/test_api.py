from flask_testing import TestCase
import unittest
import json
from PyPDF2 import PdfFileReader
from io import BytesIO
from app import app, db
from app.models import Report


class TestPDFEndpoint(TestCase):
    @staticmethod
    def setup_db():
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(Report(id=4, content=json.dumps({
                "organization": "Flowers Inc.",
                "reported_at": "2017-11-19",
                "created_at": "2017-11-23",
                "inventory": [
                    {"name": "Flower pot", "price": "2.00"},
                    {"name": "Roses, 24", "price": "50.00"}
                ]
            })))
            db.session.commit()

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/suade'
        self.setup_db()
        return app

    def test_existing_report(self):
        response = self.client.get('/reports/pdf/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/pdf')
        reader = PdfFileReader(BytesIO(response.data)) # Check it is a valid PDF
        self.assertEqual(reader.numPages, 1)
        content = reader.getPage(0).extractText()
        strings = ["Flowers Inc.", "2017-11-19", "2017-11-23", "Flower pot",
                   "$2.00", "Roses, 24", "$50.0"]
        for s in strings:
            self.assertIn(s, content)

    def test_non_existing_report(self):
        response = self.client.get('/reports/pdf/900')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()