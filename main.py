# main.py

# Main controller for Safe Driving Device



import time



from sensor_reader import SensorReader

from gps_reader import GPSReader

from classification_engine import ClassificationEngine

from csv_logger import CSVLogger

from display_controller import DisplayController





def main():

    sensor_reader = None

    gps_reader = None



    try:

        sensor_reader = SensorReader()

        gps_reader = GPSReader()

        classifier = ClassificationEngine()

        csv_logger = CSVLogger()

        display = DisplayController()



        print("Safe Driving Device started")

        print("Logging live drive data...")

        time.sleep(2)



        while True:

            sensor_data = sensor_reader.read_all()

            gps_data = gps_reader.read_gps()



            event_data = classifier.classify(sensor_data, gps_data)



            display.show_data(sensor_data, gps_data, event_data)



            # Log every row, including normal braking/driving

            csv_logger.log_event(event_data)



            # Faster loop for quicker braking detection

            time.sleep(0.1)



    except KeyboardInterrupt:

        print("\nStopping Safe Driving Device...")



    except Exception as e:

        print(f"\nSystem error: {e}")



    finally:

        if sensor_reader:

            sensor_reader.cleanup()



        if gps_reader:

            gps_reader.close()



        print("Safe Driving Device stopped")





if __name__ == "__main__":

    main()