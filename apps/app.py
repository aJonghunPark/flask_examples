from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecretkey'

    from apps.section07 import views as section07_views
    app.register_blueprint(section07_views.section07, url_prefix="/section07")

    from apps.section08 import views as section08_views
    app.register_blueprint(section08_views.section08, url_prefix="/section08")

    from apps.section09 import views as section09_views
    app.register_blueprint(section09_views.section09, url_prefix="/section09")

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    return app


def page_not_found(e):
    """ 404 Not Found  """
    return render_template("404.html"), 404


def internal_server_error(e):
    """ 500 Internal Server Error """
    return render_template("500.html"), 500
