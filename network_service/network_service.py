import logging
import subprocess

######################################
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
######################################


class NetworkService:
    """NetworkService accepts a file(.txt) with ip addresses and check availability of each IP Address"""

    def __init__(self, file: str):
        """Pass path contianing list of ip address"""
        self.file = file

    def get_devices(self):
        """Generates a list of ip addresses from the loaded .txt file"""
        try:
            with open(self.file) as file:
                ip_addresses = file.read().splitlines()
                logging.info(f"Devices: {ip_addresses}")
                return ip_addresses
        except Exception as e:
            logging.error(f"{e}")

    @property
    def check_device_availability(self):
        """checks availability of the ip address in the list"""
        ip_addresses = self.get_devices()

        if not ip_addresses:
            logging.warning("File contains no IP Address!!!")
            return

        for ip_adderss in ip_addresses:
            try:
                print(f"pinging... {ip_adderss}")
                command = f"ping -c 5 {ip_adderss}"
                output = subprocess.check_output(command.split())

                logging.info(
                    f"Command executed: [{command}] [{ip_adderss} is reachable]"
                )
                print(f"{ip_adderss} is reachable.")

            except Exception as e:
                logging.error(f"{e}")

        return output.decode()


if __name__ == "__main__":
    nc = NetworkService("./devices.txt")
    nc.check_device_availability
