from apps.app import login_manager
from apps.blog.core.views import core
from apps.blog.error_pages.handlers import error_pages
from apps.blog.posts.views import posts
from apps.blog.users.views import users
from flask import Blueprint, render_template

login_manager.login_view = "blog.users.login"

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")
blog.register_blueprint(core)
blog.register_blueprint(users)
blog.register_blueprint(posts)
blog.register_blueprint(error_pages)
