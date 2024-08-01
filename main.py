from COM.com_port_scanner import COMPortScanner
from GPS.gps_reader import GPSReader
from Controllers.attenuator_controller import AttenuatorController
from MDNS.mdns_service import MDNSService
from api import start_api

if __name__ == '__main__':
    scanner = COMPortScanner()
    attenuator_controller = AttenuatorController(scanner)

    start_api(scanner, attenuator_controller)