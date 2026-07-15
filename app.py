from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

CSV_FILE = "driving_log.csv"

def read_events():
    events = []

    if not os.path.exists(CSV_FILE):
        return events

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            events.append(row)

    return events


@app.route("/")
def dashboard():
    events = read_events()

    latest_event = events[-1] if events else None
    recent_events = events[-10:][::-1]

    return render_template(
        "dashboard.html",
        latest_event=latest_event,
        recent_events=recent_events
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)