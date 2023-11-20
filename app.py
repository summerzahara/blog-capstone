from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog = Post()


@app.route('/')
def home():  # put application's code here
    data = blog.data
    return render_template('index.html', posts=data)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    post = blog.get_post(blog_id)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run()
