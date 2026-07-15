# gps_reader.py

# GPS parser for Neo-6M

# Reads RMC and VTG data and prevents stale speed from staying displayed



import serial

import time

import pynmea2





class GPSReader:



    def __init__(self,

                 port="/dev/serial0",

                 baudrate=9600,

                 timeout=1):



        self.serial_connection = serial.Serial(

            port,

            baudrate=baudrate,

            timeout=timeout

        )



        self.last_valid_data = {

            "gps_valid": False,

            "latitude": None,

            "longitude": None,

            "speed_mph": 0.0,

            "timestamp": round(time.time(), 3)

        }



        self.last_speed_update_time = 0

        self.speed_timeout_seconds = 3.0



        print("GPS reader connected")



    def _check_stale_speed(self):

        if time.time() - self.last_speed_update_time > self.speed_timeout_seconds:

            self.last_valid_data["speed_mph"] = 0.0



    def read_gps(self):



        try:

            line = self.serial_connection.readline().decode(

                "utf-8",

                errors="ignore"

            ).strip()



            print("RAW GPS:", line)



            if not line.startswith("$"):

                self._check_stale_speed()

                return self.last_valid_data



            msg = pynmea2.parse(line)



            # RMC sentence: position + speed

            if line.startswith("$GPRMC") or line.startswith("$GNRMC"):



                if getattr(msg, "status", "V") == "A":



                    speed_knots = float(msg.spd_over_grnd or 0)

                    speed_mph = speed_knots * 1.15078



                    self.last_speed_update_time = time.time()



                    self.last_valid_data = {

                        "gps_valid": True,

                        "latitude": round(msg.latitude, 6),

                        "longitude": round(msg.longitude, 6),

                        "speed_mph": round(speed_mph, 2),

                        "timestamp": round(time.time(), 3)

                    }



                    return self.last_valid_data



            # VTG sentence: speed/course

            if line.startswith("$GPVTG") or line.startswith("$GNVTG"):



                speed_kph = getattr(msg, "spd_over_grnd_kmph", None)



                if speed_kph not in [None, ""]:

                    speed_mph = float(speed_kph) * 0.621371



                    self.last_speed_update_time = time.time()



                    self.last_valid_data["gps_valid"] = True

                    self.last_valid_data["speed_mph"] = round(speed_mph, 2)

                    self.last_valid_data["timestamp"] = round(time.time(), 3)



                    return self.last_valid_data



            self._check_stale_speed()

            return self.last_valid_data



        except Exception as e:



            print("GPS error:", e)



            self._check_stale_speed()



            return {

                "gps_valid": False,

                "latitude": self.last_valid_data.get("latitude"),

                "longitude": self.last_valid_data.get("longitude"),

                "speed_mph": self.last_valid_data.get("speed_mph", 0.0),

                "error": str(e),

                "timestamp": round(time.time(), 3)

            }



    def close(self):



        self.serial_connection.close()



        print("GPS connection closed")





if __name__ == "__main__":



    gps = GPSReader()



    try:



        while True:



            data = gps.read_gps()



            print(data)



            time.sleep(0.5)



    except KeyboardInterrupt:



        print("Stopping GPS reader...")



    finally:



        gps.close()

