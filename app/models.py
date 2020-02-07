from app import db


class Report(db.Model):
    """
    A database report object. id is a unique numeric identifier.
    content is a JSON with the contents of the report.
    """
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, name='type')
