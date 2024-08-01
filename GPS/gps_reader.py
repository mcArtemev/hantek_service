# Класс для чтения данных с порта GPS
import threading
import time
import serial


class GPSReader(threading.Thread):
    def __init__(self, scanner):
        super().__init__()
        self.scanner = scanner

    def run(self):
        print("Starting GPS Reader")
        while True:
            if self.scanner.gps_port:
                with serial.Serial(self.scanner.gps_port, 9600, timeout=1) as ser:
                    while True:
                        line = ser.readline().decode('ascii', errors='replace')
                        print(f"GPS Data: {line}")
                        time.sleep(1)
            else:
                time.sleep(5)
