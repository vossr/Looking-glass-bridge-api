# Python3 API for looking glass bridge

## Windows installation
- git clone https://github.com/rpehkone/looking-glass-bridge-python-api
- cd looking-glass-bridge-python-api
- git clone https://github.com/Looking-Glass/LookingGlassCoreSDK
- Compile visual studio project x64 release
- Move visual_studio\x64\Release\bridge_api.dll to here
- Move HoloPlayCore\dylib\Win64\HoloPlayCore.dll to here
- python3 -m pip install -e .

## Usage
```python
import bridge_api

num_devices = bridge_api.get_number_of_devices()
device = bridge_api.get_device(0)
print(device.info.device_type)
```
