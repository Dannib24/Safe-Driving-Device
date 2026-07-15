# Safe Driving Device

A Raspberry Pi-based embedded system that monitors driving behavior by collecting real-time sensor data and classifying braking events. The system was developed as a senior capstone project for my Bachelor of Science in Computer and Electrical Engineering at National University.

---

## Overview

The Safe Driving Device was designed to improve the accuracy of braking event detection using multiple sensors and real-time data processing. By combining acceleration, distance, and GPS speed information, the device classifies braking events as Normal, Hard, or Emergency.

The long-term vision for this project is to support the insurance industry by providing more accurate driving behavior data that could assist with usage-based insurance programs, driver coaching, and underwriting risk assessments.

---

## Features

- Real-time braking event detection
- Normal, Hard, and Emergency braking classification
- GPS speed tracking
- Distance monitoring using an ultrasonic sensor
- Live dashboard displaying driving information
- CSV event logging for later analysis
- Real-time sensor integration using Raspberry Pi

---

## Hardware Components

- Raspberry Pi 4
- MPU-6050 Accelerometer/Gyroscope
- HC-SR04 Ultrasonic Sensor
- Neo-6M GPS Module
- HDMI Display
- Jumper Wires
- Portable Power Supply

---

## Software & Technologies

- Python
- Raspberry Pi OS
- CSV Logging
- Sensor Data Processing
- Embedded Systems Programming
- Git & GitHub

---

## How It Works

The system continuously collects data from multiple sensors.

The accelerometer measures vehicle acceleration and deceleration.

The ultrasonic sensor monitors the distance between the vehicle and objects ahead.

The GPS module provides real-time vehicle speed.

The software combines these data points to classify braking events as:

- Normal Braking
- Hard Braking
- Emergency Braking

Each event is displayed on screen and logged to a CSV file for future analysis.

---

## My Contributions

I independently:

- Designed and assembled the hardware device
- Developed the Python application
- Integrated multiple hardware sensors
- Designed the braking classification algorithm
- Built the dashboard interface
- Implemented GPS speed tracking
- Implemented CSV data logging
- Tested and debugged the embedded system
- Tuned detection thresholds to improve braking classification accuracy

---

## Future Improvements

- Driver safety scoring system
- Insurance discount estimation based on driving behavior
- Machine learning for improved braking classification
- Interactive data visualizations and graphs
- Cloud dashboard for remote monitoring
- Mobile application integration
- Historical driving analytics
- Additional driving event detection (rapid acceleration, harsh cornering, distracted driving)

---

## Skills Demonstrated

- Embedded Systems
- Python Programming
- Sensor Integration
- Data Collection
- Data Analysis
- Algorithm Development
- Hardware Troubleshooting
- Software Debugging
- System Testing
- Technical Documentation
- Engineering Design
- Git Version Control

---

## Potential Applications

- Usage-Based Insurance (UBI)
- Driver Behavior Analytics
- Fleet Management
- Driver Coaching
- Vehicle Safety Research
- Risk Assessment

---

## Author

Danielle Griggs

Bachelor of Science in Computer and Electrical Engineering
National University
