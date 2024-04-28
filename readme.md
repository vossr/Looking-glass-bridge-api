# Python3 API for looking glass bridge
## License
- This API is distributed in source form. Users are required to independently link against the HoloPlay Core SDK, which must be obtained directly from Looking Glass Factory.
- Compliance: Users of this API must comply with the HoloPlayCoreSDK's licensing terms. It is essential for users to review and agree to these terms before utilizing this API in their projects.
- Please ensure that you have legally acquired the HoloPlayCoreSDK and adhere to its licensing conditions. This API assumes no liability for improper use or licensing of the HoloPlayCoreSDK by third parties.

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
