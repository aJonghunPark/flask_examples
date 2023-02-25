from os import abort

from apps.app import db
from apps.blog.models import Post
from apps.blog.posts.forms import PostForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

posts = Blueprint("posts", __name__)


# Create
@posts.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Created")
        return redirect(url_for("blog.core.index"))

    return render_template("create_post.html", form=form)


# Blog Post (View)
@posts.route("/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, date=post.date, post=post)


# Update
@posts.route("/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Updated")
        return redirect(url_for("blog.posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.text.data = post.text

    return render_template("create_post.html", title="Updating", form=form)


# Delete
@posts.route("/<int:post_id>/delete", methods=["GET", "POST"])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Blog Post Deleted")
    return redirect(url_for("blog.core.index"))
