import threading
import time
import serial.tools.list_ports


# Класс для сканирования COM портов
class COMPortScanner(threading.Thread):
    def __init__(self):
        super().__init__()
        self.gps_port = None  # Переменная для хранения порта GPS
        self.attenuator_port = None  # Переменная для хранения порта аттенюатора

    # Метод поиска порта GPS
    def run(self):
        print("Starting COM Port Scanner")
        while True:
            ports = list(serial.tools.list_ports.comports())
            for port in ports:
                if self.is_gps(port):
                    self.gps_port = port.device
                    print(f"GPS Port: {self.gps_port}")
                if self.is_attenuator(port):
                    self.attenuator_port = port.device
                    print(f"Attenuator Port: {self.attenuator_port}")
            time.sleep(5)

    def is_gps(self, port):
        return 'GPS' in port.description

    def is_attenuator(self, port):
        return 'ATT' in port.description
