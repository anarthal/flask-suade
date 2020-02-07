from app import app, db, models
import inspect


@app.shell_context_processor
def make_shell_context():
    """
    Convenience function to set up the flask command line
    (executed when you run flask shell). We import all models
    to make life easier.
    """
    res = { name: cls for name, cls in models.__dict__.items()
            if inspect.isclass(cls) and issubclass(cls, db.Model) }
    res['db'] = db
    return res
