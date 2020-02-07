
class Config(object):
    """
    The Flask application config.
    """

    # How to connect to the Postgre server
    SQLALCHEMY_DATABASE_URI = 'postgresql://interview:uo4uu3AeF3@candidate.suade.org/suade'

    # Docs say this item helps performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False