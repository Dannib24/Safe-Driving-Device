import csv
import time
import random

results = []

for test in range(1, 6):

    # Simulate braking detection
    detection_start = time.time()

    # Simulate processing delay
    simulated_processing = random.uniform(0.145, 0.152)

    time.sleep(simulated_processing)

    # End timing
    detection_end = time.time()

    # Convert to milliseconds
    response_time_ms = round(
        (detection_end - detection_start) * 1000,
        2
    )

    results.append([
        test,
        response_time_ms,
        "Emergency"
    ])

filename = "response_time_data.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "test_iteration",
        "response_time_ms",
        "classification"
    ])

    writer.writerows(results)

print("\nResponse Time Test Results")

for row in results:
    print(
        f"Test {row[0]}: "
        f"{row[1]} ms - {row[2]}"
    )

average = round(
    sum(r[1] for r in results) / len(results),
    2
)

print(f"\nAverage Response Time: {average} ms")

print(f"\nCSV saved as: {filename}")