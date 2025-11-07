from network_service.network_service import NetworkService

nc = NetworkService("./network_service/devices.txt")
nc.check_device_availability
