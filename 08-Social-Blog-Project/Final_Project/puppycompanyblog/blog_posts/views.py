from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts',__name__)


# CREATE
@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(
            title=form.title.data,
            text=form.text.data,
            user_id=current_user.id,
        )
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)


# BLOG POST (VIEW)
# Everyone is supposed to have access to the blog posts for viewing only
@blog_posts.route('/<int:blog_post_id>') # the blogpost Id integer is used in the database query
def blog_post(blog_post_id):
    # grab the requested blog post by id number or return 404
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    return render_template(
        'blog_post.html',
        title=blog_post.title,
        date=blog_post.date,
        post=blog_post,
    ) # also possible to pass only the blog_post object and get title and date data in the template


# UPDATE
@blog_posts.route("/<int:blog_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403) # permission issue, not the right author to update a post; comes with Flask

    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit() # nothing to add it's just an update
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    elif request.method == 'GET': # way to feel the form with the current blogpost content
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', title='Updating', form=form)


# DELETE
@blog_posts.route("/<int:blog_post_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user: # permission to delete the post
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))
    # will create a button in the template instead of a view for the deletion process