import tracing
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from flask import Flask, jsonify
import requests

app = Flask(__name__)

FlaskInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()  # This line instruments requests

@app.route("/")
def hello():
    return 'Hello World!'

@app.route("/posts")
def posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    comments()
    return jsonify(posts)

@app.route("/users")
def users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    posts = response.json()
    return jsonify(posts)

def comments():
    requests.get('https://jsonplaceholder.typicode.com/comments')

app.run(debug=True)