import time
from queue import Queue
import threading
import serial


class AttenuatorController(threading.Thread):
    def __init__(self, scanner):
        super().__init__()
        self.scanner = scanner
        self.command_queue = Queue()

    def run(self):
        print("Starting AttentuatorController")
        while True:
            if self.scanner.attenuator_port:
                with serial.Serial(self.scanner.attenuator_port, 9600, timeout=1) as ser:
                    while True:
                        command = self.command_queue.get()
                        if command:
                            ser.write(command.encode())
                            response = ser.readline().decode('ascii', errors='replace')
                            print(f"Attenuator Response: {response}")
            else:
                time.sleep(5)

    def send_command(self, command):
        self.command_queue.put(command)
