from flask import Flask, render_template
from flask_sse import sse
import lsl_reader

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix="/events")

with app.app_context():
    lsl_reader.start()


@app.route("/simulate_artifact")
def simulate_artifact():
    lsl_reader.send_blink_artifact_event()
    return "Artifact sent!"


@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response
