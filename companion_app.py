from flask import Flask, render_template_string, abort

import csv

import os



app = Flask(__name__)



CSV_FILE = "driving_log.csv"



HTML = """

<!DOCTYPE html>

<html>

<head>

    <title>Safe Driving Device Dashboard</title>

    <style>

        body {

            font-family: Arial, sans-serif;

            background: #111827;

            color: white;

            padding: 30px;

        }

        h1 { color: #38bdf8; }

        .card {

            background: #1f2937;

            padding: 20px;

            border-radius: 12px;

            margin-bottom: 20px;

        }

        table {

            width: 100%;

            border-collapse: collapse;

            background: #1f2937;

        }

        th, td {

            padding: 10px;

            border-bottom: 1px solid #374151;

            text-align: left;

        }

        th { color: #38bdf8; }

        a {

            color: white;

            text-decoration: none;

            display: block;

            width: 100%;

        }

        tr:hover {

            background: #374151;

        }

        .high { color: #f87171; font-weight: bold; }

        .medium { color: #facc15; font-weight: bold; }

        .low { color: #4ade80; font-weight: bold; }

        .button {

            display: inline-block;

            padding: 10px 14px;

            background: #38bdf8;

            color: #111827;

            border-radius: 8px;

            font-weight: bold;

            margin-top: 10px;

        }

    </style>

</head>

<body>

    <h1>Safe Driving Device Companion Dashboard</h1>



    <div class="card">

        <h2>Latest Driving Event</h2>

        {% if latest %}

            <p><strong>Time:</strong> {{ latest.timestamp }}</p>

            <p><strong>Event:</strong> {{ latest.event }}</p>

            <p><strong>Risk Level:</strong>

                <span class="{{ latest.risk_level|lower }}">{{ latest.risk_level }}</span>

            </p>

            <p><strong>Speed:</strong> {{ latest.speed_mph }} mph</p>

            <p><strong>Distance:</strong> {{ latest.distance_cm }} cm</p>

            <p><strong>Message:</strong> {{ latest.message }}</p>

            <a class="button" href="/event/{{ latest.id }}">Open Latest Event Report</a>

        {% else %}

            <p>No driving events logged yet.</p>

        {% endif %}

    </div>



    <div class="card">

        <h2>Recent Event History</h2>

        <p>Click any event row below to open a screenshot-ready report.</p>



        <table>

            <tr>

                <th>Timestamp</th>

                <th>Event</th>

                <th>Risk</th>

                <th>Speed</th>

                <th>Distance</th>

                <th>Message</th>

            </tr>



            {% for row in rows %}

            <tr>

                <td><a href="/event/{{ row.id }}">{{ row.timestamp }}</a></td>

                <td><a href="/event/{{ row.id }}">{{ row.event }}</a></td>

                <td><a class="{{ row.risk_level|lower }}" href="/event/{{ row.id }}">{{ row.risk_level }}</a></td>

                <td><a href="/event/{{ row.id }}">{{ row.speed_mph }} mph</a></td>

                <td><a href="/event/{{ row.id }}">{{ row.distance_cm }} cm</a></td>

                <td><a href="/event/{{ row.id }}">{{ row.message }}</a></td>

            </tr>

            {% endfor %}

        </table>

    </div>

</body>

</html>

"""



EVENT_HTML = """

<!DOCTYPE html>

<html>

<head>

    <meta http-equiv="refresh" content="2">

    <title>Driving Event Report</title>

    <style>

        body {

            font-family: Arial, sans-serif;

            background: #111827;

            color: white;

            padding: 40px;

        }

        h1 { color: #38bdf8; }

        .report {

            background: #1f2937;

            padding: 30px;

            border-radius: 16px;

            max-width: 750px;

        }

        .field {

            font-size: 22px;

            margin-bottom: 18px;

        }

        .label {

            color: #38bdf8;

            font-weight: bold;

        }

        .high { color: #f87171; font-weight: bold; }

        .medium { color: #facc15; font-weight: bold; }

        .low { color: #4ade80; font-weight: bold; }

        a {

            color: #38bdf8;

            display: inline-block;

            margin-top: 20px;

            font-size: 18px;

        }

    </style>

</head>

<body>

    <h1>Safe Driving Device Event Report</h1>



    <div class="report">

        <div class="field"><span class="label">Timestamp:</span> {{ event.timestamp }}</div>

        <div class="field"><span class="label">Event:</span> {{ event.event }}</div>

        <div class="field">

            <span class="label">Risk Level:</span>

            <span class="{{ event.risk_level|lower }}">{{ event.risk_level }}</span>

        </div>

        <div class="field"><span class="label">Speed:</span> {{ event.speed_mph }} mph</div>

        <div class="field"><span class="label">Distance:</span> {{ event.distance_cm }} cm</div>

        <div class="field"><span class="label">Message:</span> {{ event.message }}</div>

    </div>



    <a href="/">Back to Dashboard</a>

</body>

</html>

"""



def read_events():

    if not os.path.exists(CSV_FILE):

        return []



    with open(CSV_FILE, mode="r") as file:

        reader = csv.DictReader(file)

        rows = list(reader)



    events = []

    for index, row in enumerate(rows):

        row["id"] = index

        events.append(row)



    return events





@app.route("/")

def dashboard():

    all_events = read_events()

    rows = all_events[-50:][::-1]

    latest = rows[0] if rows else None

    return render_template_string(HTML, rows=rows, latest=latest)





@app.route("/event/<int:event_id>")

def event_detail(event_id):

    all_events = read_events()



    if event_id < 0 or event_id >= len(all_events):

        abort(404)



    event = all_events[event_id]

    return render_template_string(EVENT_HTML, event=event)





if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)