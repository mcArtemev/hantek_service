# Класс для mDNS сервиса
import socket

from zeroconf import Zeroconf, ServiceInfo


class MDNSService:
    print("Starting mDNS Server")

    def __init__(self):
        self.zeroconf = Zeroconf()
        self.info = ServiceInfo(
            "_http._tcp.local.",
            "HanterServer._http._tcp.local.",
            addresses=[socket.inet_aton("127.0.0.1")],
            port=5000,
            properties={},
            server="HantekServer.local",
        )

    def register_service(self):
        self.zeroconf.register_service(self.info)
        print(f"Server {self.info.server} started at port {self.info.port}")

    def unregister_service(self):
        self.zeroconf.unregister_service(self.info)
        self.zeroconf.close()
