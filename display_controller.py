# display_controller.py

# Displays live Safe Driving Device telemetry in the terminal/HDMI screen



import os

import time





class DisplayController:

    def __init__(self):

        print("Display controller ready")



    def clear_screen(self):

        os.system("clear")



    def show_data(self, sensor_data, gps_data, event_data):

        self.clear_screen()



        print("====================================")

        print("      SAFE DRIVING DEVICE")

        print("====================================")

        print()



        print("SENSOR DATA")

        print("------------------------------------")

        print(f"Accel X:      {sensor_data.get('accel_x')}")

        print(f"Accel Y:      {sensor_data.get('accel_y')}")

        print(f"Accel Z:      {sensor_data.get('accel_z')}")

        print(f"Distance:     {sensor_data.get('distance_cm')} cm")

        print()



        print("GPS DATA")

        print("------------------------------------")

        print(f"GPS Valid:    {gps_data.get('gps_valid')}")

        print(f"Latitude:     {gps_data.get('latitude')}")

        print(f"Longitude:    {gps_data.get('longitude')}")

        print(f"Speed:        {gps_data.get('speed_mph')} mph")

        print()



        print("DRIVING EVENT")

        print("------------------------------------")

        print(f"Event:        {event_data.get('event')}")

        print(f"Risk Level:   {event_data.get('risk_level')}")

        print(f"Brake Force:  {event_data.get('braking_force')}")

        print(f"Message:      {event_data.get('message')}")

        print()



        print("====================================")

        print("Press CTRL + C to stop")

        print("====================================")





if __name__ == "__main__":

    display = DisplayController()



    sample_sensor = {

        "accel_x": -0.52,

        "accel_y": 0.01,

        "accel_z": 0.98,

        "distance_cm": 35

    }



    sample_gps = {

        "gps_valid": False,

        "latitude": None,

        "longitude": None,

        "speed_mph": 0.0

    }



    sample_event = {

        "event": "hard_braking",

        "risk_level": "high",

        "braking_force": 0.52,

        "message": "Hard braking detected near object"

    }



    try:

        while True:

            display.show_data(sample_sensor, sample_gps, sample_event)

            time.sleep(1)



    except KeyboardInterrupt:

        print("\nDisplay stopped")