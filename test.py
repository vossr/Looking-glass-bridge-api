import bridge_api
import pprint

num_devices = bridge_api.get_number_of_devices()
device = bridge_api.get_device(0)
pprint.pprint(device)
