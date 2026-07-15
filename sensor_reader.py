# sensor_reader.py

# MPU6050 + HC-SR04 sensor reader for Safe Driving Device



import time

import smbus

import RPi.GPIO as GPIO





class SensorReader:



    MPU6050_ADDR = 0x68



    # MPU6050 Registers

    PWR_MGMT_1 = 0x6B

    ACCEL_XOUT_H = 0x3B

    ACCEL_YOUT_H = 0x3D

    ACCEL_ZOUT_H = 0x3F



    def __init__(self, trig_pin=23, echo_pin=24):



        self.trig_pin = trig_pin

        self.echo_pin = echo_pin



        # Initialize I2C bus

        self.bus = smbus.SMBus(1)



        # Wake up MPU6050

        self.bus.write_byte_data(

            self.MPU6050_ADDR,

            self.PWR_MGMT_1,

            0

        )



        print("MPU6050 connected successfully!")



        # GPIO setup for HC-SR04

        GPIO.setmode(GPIO.BCM)



        GPIO.setup(self.trig_pin, GPIO.OUT)

        GPIO.setup(self.echo_pin, GPIO.IN)



        GPIO.output(self.trig_pin, False)



        print("Ultrasonic sensor ready")



        time.sleep(2)



    def read_raw_data(self, addr):



        high = self.bus.read_byte_data(

            self.MPU6050_ADDR,

            addr

        )



        low = self.bus.read_byte_data(

            self.MPU6050_ADDR,

            addr + 1

        )



        value = (high << 8) | low



        if value > 32768:

            value = value - 65536



        return value



    def read_imu(self):



        accel_x = self.read_raw_data(self.ACCEL_XOUT_H)

        accel_y = self.read_raw_data(self.ACCEL_YOUT_H)

        accel_z = self.read_raw_data(self.ACCEL_ZOUT_H)



        # Convert to g-force

        accel_x = accel_x / 16384.0

        accel_y = accel_y / 16384.0

        accel_z = accel_z / 16384.0



        return {

            "accel_x": round(accel_x, 3),

            "accel_y": round(accel_y, 3),

            "accel_z": round(accel_z, 3),

        }



    def read_distance(self):



        GPIO.output(self.trig_pin, False)

        time.sleep(0.0002)



        GPIO.output(self.trig_pin, True)

        time.sleep(0.00001)

        GPIO.output(self.trig_pin, False)



        pulse_start = time.time()

        timeout = pulse_start



        while GPIO.input(self.echo_pin) == 0:

            pulse_start = time.time()



            if pulse_start - timeout > 0.03:

                return None



        pulse_end = time.time()

        timeout = pulse_end



        while GPIO.input(self.echo_pin) == 1:

            pulse_end = time.time()



            if pulse_end - timeout > 0.03:

                return None



        pulse_duration = pulse_end - pulse_start



        distance = pulse_duration * 17150



        if distance <= 0 or distance > 400:

            return None



        return round(distance, 2)



    def read_all(self):



        imu_data = self.read_imu()



        distance = self.read_distance()



        return {

            **imu_data,

            "distance_cm": distance,

            "timestamp": round(time.time(), 3)

        }



    def cleanup(self):



        GPIO.cleanup()



        print("GPIO cleaned up")





if __name__ == "__main__":



    sensor = SensorReader()



    try:



        while True:



            data = sensor.read_all()



            print(data)



            time.sleep(0.5)



    except KeyboardInterrupt:



        print("Stopping sensor reader...")



        sensor.cleanup()