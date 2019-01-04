# -*- coding: utf-8 -*-
# standard library modules
import os

# third party modules
from flask import Flask

# local/proprietary modules
from asset_planner.cache import cache

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Using cache
    cache_config={'CACHE_TYPE': 'redis',
                  'CACHE_REDIS_URL': os.environ.get('REDIS_URL', '127.0.0.1:6379'),
                  # cache timeout sets to 1200 sec (20 min), since this may be the active perf
                  # analysis time period.
                  'CACHE_DEFAULT_TIMEOUT': 1200
    }
    cache.init_app(app, config=cache_config)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='a191cklizurhf2o89'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # apply the blueprints to the app
    from asset_planner import bp_index
    app.register_blueprint(bp_index.bp)

    return app
