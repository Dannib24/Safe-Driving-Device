import csv

gps_data = [
    [0, 41.6101, -87.7205, 0, "Connected"],
    [5, 41.6105, -87.7210, 12, "Connected"],
    [10, 41.6112, -87.7218, 24, "Connected"],
    [15, 41.6120, -87.7226, 31, "Connected"],
    [20, 41.6131, -87.7235, 38, "Connected"],
    [25, 41.6140, -87.7242, 25, "Connected"],
    [30, 41.6148, -87.7251, 10, "Connected"],
]

filename = "gps_verification_data.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "time_seconds",
        "latitude",
        "longitude",
        "speed_mph",
        "gps_status"
    ])

    writer.writerows(gps_data)

print(f"GPS simulation data saved to {filename}")