from flask import Flask, request
from db import db, init_db
from models import Post

app = Flask(__name__)
init_db(app)

@app.route("/", methods=["GET"])
def home():
    return'Welcome to Blogging Platform API'

@app.route("/posts", methods=["GET"])
def get_posts():
    all_posts = Post.query.all()
    return [
        {
            'id': post.id,
            "title": post.title,
            "content": post.content
        }
        for post in all_posts
    ]

@app.route('/posts/<int:post_id>', methods=["GET"])
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return {"error": "Post not found"}, 404
    return {"id": post.id, "title": post.title, "content": post.content}


@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Request body must be valid JSON"}, 400
    title = data.get("title")
    content = data.get("content")

    if not isinstance(title, str) or not isinstance(content, str):
        return {"error": "Title and Content must be strings"}, 400

    title = title.strip()
    content = content.strip()

    if not title or not content:
        return "Title and Content cannot be empty", 400

    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()

    return{
        'message': 'Post created',
        'id': new_post.id,
        "title": title,
        "content": content
    }, 201

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Request body must be valid JSON"}, 400
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return {"error": "Post not found"}, 404

    if "title" in data:
        title = data.get("title")

        if not isinstance(title, str):
            return {"error": "Title must be a string"}, 400

        title = title.strip()
        if not title:
            return {"error": "Title cannot be empty"}, 400
        post.title = title

    if 'content' in data:#content validation
        content = data.get("content")
        if not isinstance(content, str):
            return {"error": "Content must be a string"}, 400
        content = content.strip()
        if not content:
            return {"error": "Content cannot be empty"}, 400
        post.content = content
    db.session.commit()
    return {"id": post.id, "title": post.title, "content": post.content}


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return {"error": "Post not found"}, 404
    db.session.delete(post)
    db.session.commit()
    return {"message": "Post deleted"}, 200


with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

    with db.engine.connect() as connection:
        print("Database connected successfully!")

if __name__ == "__main__":
    app.run(debug=True)