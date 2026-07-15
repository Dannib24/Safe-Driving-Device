# csv_logger.py

# Logs driving events to a CSV file



import csv

import os

from datetime import datetime





class CSVLogger:

    def __init__(self, filename="driving_log.csv"):

        self.filename = filename

        self.headers = [

            "timestamp",

            "event",

            "risk_level",

            "braking_force",

            "speed_mph",

            "distance_cm",

            "message"

        ]



        self._initialize_file()



    def _initialize_file(self):

        file_exists = os.path.isfile(self.filename)



        if not file_exists:

            with open(self.filename, mode="w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow(self.headers)



    def log_event(self, event_data):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



        row = [

            timestamp,

            event_data.get("event"),

            event_data.get("risk_level"),

            event_data.get("braking_force"),

            event_data.get("speed_mph"),

            event_data.get("distance_cm"),

            event_data.get("message")

        ]



        with open(self.filename, mode="a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(row)



        print("Event logged:", row)





if __name__ == "__main__":

    logger = CSVLogger()



    sample_event = {

        "event": "hard_braking",

        "risk_level": "high",

        "braking_force": 0.52,

        "speed_mph": 35,

        "distance_cm": 28,

        "message": "Hard braking detected near object"

    }



    logger.log_event(sample_event)