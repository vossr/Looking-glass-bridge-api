import bridge_api_internal as bridge
from types import SimpleNamespace

bridge.InitializeApp()

def get_number_of_devices():
    return bridge.GetNumDevices()

def get_device(device_index):
    num_devices = bridge.GetNumDevices()
    if device_index >= num_devices:
        raise Exception("No display " + str(device_index) + " connected. Devices connected: " + str(num_devices))

    info = SimpleNamespace(
        bridge_core_version = bridge.GetHoloPlayCoreVersion(),
        bridge_service_version = bridge.GetHoloPlayServiceVersion(),
        hdmi_name = bridge.GetDeviceHDMIName(device_index),
        device_type = bridge.GetDeviceType(device_index),
        button0_down = bridge.GetDevicePropertyInt(device_index, "/buttons/0") == 1,
        button1_down = bridge.GetDevicePropertyInt(device_index, "/buttons/1") == 1,
        button2_down = bridge.GetDevicePropertyInt(device_index, "/buttons/2") == 1,
        button3_down = bridge.GetDevicePropertyInt(device_index, "/buttons/3") == 1
    )

    window = SimpleNamespace(
        x = bridge.GetDevicePropertyWinX(device_index),
        y = bridge.GetDevicePropertyWinY(device_index),
        w = bridge.GetDevicePropertyScreenW(device_index),
        h = bridge.GetDevicePropertyScreenH(device_index),
        aspect_ratio = bridge.GetDevicePropertyDisplayAspect(device_index)
    )

    shader = SimpleNamespace(
        lenticular_pitch = bridge.GetDevicePropertyPitch(device_index),
        lenticular_tilt = bridge.GetDevicePropertyTilt(device_index),
        center_offset = bridge.GetDevicePropertyCenter(device_index),
        subpixel_size = bridge.GetDevicePropertySubp(device_index),
        fringe = bridge.GetDevicePropertyFringe(device_index),
        red_index = bridge.GetDevicePropertyRi(device_index),
        blue_index = bridge.GetDevicePropertyBi(device_index),
        should_invert = bridge.GetDevicePropertyInvView(device_index),
        vertex_shader = bridge.GetVertexShaderGLSL(),
        fragment_shader = bridge.GetFragmentShaderGLSL()
    )

    quilt = SimpleNamespace(
        recommended_texture_resolution_w = bridge.GetDevicePropertyQuiltX(device_index),
        recommended_texture_resolution_h = bridge.GetDevicePropertyQuiltY(device_index),
        tiling_dimension_x = bridge.GetDevicePropertyTileX(device_index),
        tiling_dimension_y = bridge.GetDevicePropertyTileY(device_index)
    )

    device = SimpleNamespace(
        info = info,
        window = window,
        shader = shader,
        quilt = quilt
    )
    return device
