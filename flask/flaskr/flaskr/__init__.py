import os

from flask import Flask

#: The application factory way of creating an app

def create_app(test_config=None):

    # flask entrypoint
    app = Flask(__name__)

    # look for / set up config
    app.config.from_mapping(
            SECRET_KEY ='dev',
            DATABASE=os.path.join(app.instance_path, 'flasker.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    # instance path where db stuff goes
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize database
    from . import db
    db.init_app(app)

    # import our blueprints
    from . import auth
    from . import blog

    # register them with flask
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # register rules
    # makes url_for('index') synonymous with url_for('blog.index')
    # basically makes the blueprint the default route
    app.add_url_rule('/', endpoint='index')

    # routes
    @app.route('/hello')
    def hello():
        return 'Hello World'

    # return processed app
    return app
