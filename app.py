import tracing
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from flask import Flask

app = Flask(__name__)

FlaskInstrumentor.instrument_app(app)

@app.route("/")
def hello():
    return 'Hello World!'

app.run(debug=True)