import time

# -----------------------------
# SIMULATED TEST SCENARIOS
# -----------------------------

simulation_data = [

    # NORMAL BRAKING
    {
        "event": "Normal",
        "sensor_data": {
            "acceleration": 1.2,
            "distance": 220
        },
        "gps_data": {
            "speed": 42,
            "latitude": 41.6101,
            "longitude": -87.7205
        }
    },

    {
        "event": "Normal",
        "sensor_data": {
            "acceleration": 2.1,
            "distance": 180
        },
        "gps_data": {
            "speed": 31,
            "latitude": 41.6112,
            "longitude": -87.7218
        }
    },

    # EMERGENCY BRAKING
    {
        "event": "Emergency",
        "sensor_data": {
            "acceleration": 5.8,
            "distance": 45
        },
        "gps_data": {
            "speed": 18,
            "latitude": 41.6131,
            "longitude": -87.7235
        }
    },

    {
        "event": "Emergency",
        "sensor_data": {
            "acceleration": 6.1,
            "distance": 30
        },
        "gps_data": {
            "speed": 10,
            "latitude": 41.6140,
            "longitude": -87.7242
        }
    },

    # RECKLESS BRAKING
    {
        "event": "Reckless",
        "sensor_data": {
            "acceleration": 3.8,
            "distance": 110
        },
        "gps_data": {
            "speed": 22,
            "latitude": 41.6148,
            "longitude": -87.7251
        }
    },

    {
        "event": "Reckless",
        "sensor_data": {
            "acceleration": 4.3,
            "distance": 85
        },
        "gps_data": {
            "speed": 12,
            "latitude": 41.6152,
            "longitude": -87.7258
        }
    }

]

# -----------------------------
# GENERATOR FUNCTION
# -----------------------------

def get_simulated_data():
    for item in simulation_data:

        print("\n----------------------------")
        print(f"Simulated Event: {item['event']}")
        print("----------------------------")

        print("Sensor Data:")
        print(item["sensor_data"])

        print("GPS Data:")
        print(item["gps_data"])

        yield item["sensor_data"], item["gps_data"]

        time.sleep(3)