from flask import Flask, render_template
import requests

app = Flask(__name__)
endpoint = "https://api.npoint.io/4526f5a760f183b935c8"


@app.route('/')
def home():
    data = requests.get(url=endpoint).json()
    return render_template('index.html', blogs=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def post(num):
    data = requests.get(url=endpoint).json()[num-1]
    return render_template('post.html', blog=data)


if __name__ == "__main__":
    app.run(debug=True)
