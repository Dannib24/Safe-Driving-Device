# classification_engine.py

# Hybrid classification engine



import time





class ClassificationEngine:

    def __init__(self):

        self.last_event = "normal"

        self.last_event_time = 0



        # Faster response

        self.cooldown_seconds = 0.3



        # Thresholds

        self.hard_braking_threshold = 0.20

        self.emergency_braking_threshold = 0.25

        self.emergency_obstacle_distance_cm = 300



    def classify(self, sensor_data, gps_data):



        accel_x = sensor_data.get("accel_x", 0)

        distance_cm = sensor_data.get("distance_cm", None)



        speed_mph = gps_data.get("speed_mph", 0)

        gps_valid = gps_data.get("gps_valid", False)



        current_time = time.time()



        # Negative accel_x indicates braking

        braking_force = abs(accel_x) if accel_x < 0 else 0



        event = "normal"

        risk_level = "low"

        message = "Normal driving behavior"



        # Emergency braking

        if (

            braking_force >= self.emergency_braking_threshold

            and distance_cm is not None

            and distance_cm <= self.emergency_obstacle_distance_cm

        ):

            event = "emergency_braking"

            risk_level = "high"

            message = "Emergency braking detected near obstacle"



        # Hard braking

        elif braking_force >= self.hard_braking_threshold:

            event = "hard_braking"

            risk_level = "medium"

            message = "Hard braking detected"



        # GPS context

        if gps_valid:

            if speed_mph >= 25 and event != "normal":

                risk_level = "high"

                message += f" at {round(speed_mph, 2)} mph"

            elif speed_mph >= 5:

                message += f" at {round(speed_mph, 2)} mph"

            else:

                message += " while stopped or moving slowly"

        else:

            message += " GPS not locked"



        # Cooldown

        if event != self.last_event:

            if current_time - self.last_event_time < self.cooldown_seconds:

                event = self.last_event

            else:

                self.last_event = event

                self.last_event_time = current_time



        return {

            "event": event,

            "risk_level": risk_level,

            "message": message,

            "braking_force": round(braking_force, 3),

            "speed_mph": round(speed_mph, 2),

            "gps_valid": gps_valid,

            "distance_cm": distance_cm,

            "timestamp": round(current_time, 3)

        }





if __name__ == "__main__":



    engine = ClassificationEngine()



    test_cases = [

        {

            "name": "Normal",

            "sensor_data": {"accel_x": -0.10, "distance_cm": 120},

            "gps_data": {"gps_valid": True, "speed_mph": 12}

        },

        {

            "name": "Hard Braking",

            "sensor_data": {"accel_x": -0.25, "distance_cm": 120},

            "gps_data": {"gps_valid": True, "speed_mph": 18}

        },

        {

            "name": "Emergency Braking",

            "sensor_data": {"accel_x": -0.55, "distance_cm": 30},

            "gps_data": {"gps_valid": True, "speed_mph": 18}

        }

    ]



    for test in test_cases:

        print("\n" + test["name"])

        result = engine.classify(

            test["sensor_data"],

            test["gps_data"]

        )

        print(result)

        time.sleep(1)

