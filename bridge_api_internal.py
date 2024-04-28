from ctypes import CDLL, c_char_p, c_int, c_float
import os

file_path = os.path.abspath(__file__)
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bridge_api.dll')
lib = CDLL(dll_path)

lib.InitializeApp.restype = c_char_p
def InitializeApp():
    error = lib.InitializeApp()
    if error:
        error_str = error.decode('utf-8')
        raise Exception(error_str)

lib.CloseApp.restype = None
def CloseApp():
    lib.CloseApp()

lib.GetHoloPlayCoreVersion.restype = c_char_p
def GetHoloPlayCoreVersion():
    return lib.GetHoloPlayCoreVersion().decode('utf-8')

lib.GetHoloPlayServiceVersion.restype = c_char_p
def GetHoloPlayServiceVersion():
    return lib.GetHoloPlayServiceVersion().decode('utf-8')

lib.GetNumDevices.restype = c_int
def GetNumDevices():
    return lib.GetNumDevices()

lib.GetDeviceHDMIName.restype = c_char_p
lib.GetDeviceHDMIName.argtypes = [c_int]
def GetDeviceHDMIName(device_index):
    return lib.GetDeviceHDMIName(device_index).decode('utf-8')

lib.GetDeviceType.restype = c_char_p
lib.GetDeviceType.argtypes = [c_int]
def GetDeviceType(device_index):
    return lib.GetDeviceType(device_index).decode('utf-8')

lib.GetDevicePropertyInt.restype = c_int
lib.GetDevicePropertyInt.argtypes = [c_int, c_char_p]
def GetDevicePropertyInt(device_index, property_str):
    return lib.GetDevicePropertyInt(device_index, property_str.encode('utf-8'))

lib.GetDevicePropertyWinX.restype = c_int
lib.GetDevicePropertyWinX.argtypes = [c_int]
def GetDevicePropertyWinX(device_index):
    return lib.GetDevicePropertyWinX(device_index)

lib.GetDevicePropertyWinY.restype = c_int
lib.GetDevicePropertyWinY.argtypes = [c_int]
def GetDevicePropertyWinY(device_index):
    return lib.GetDevicePropertyWinY(device_index)

lib.GetDevicePropertyScreenW.restype = c_int
lib.GetDevicePropertyScreenW.argtypes = [c_int]
def GetDevicePropertyScreenW(device_index):
    return lib.GetDevicePropertyScreenW(device_index)

lib.GetDevicePropertyScreenH.restype = c_int
lib.GetDevicePropertyScreenH.argtypes = [c_int]
def GetDevicePropertyScreenH(device_index):
    return lib.GetDevicePropertyScreenH(device_index)

lib.GetDevicePropertyDisplayAspect.restype = c_float
lib.GetDevicePropertyDisplayAspect.argtypes = [c_int]
def GetDevicePropertyDisplayAspect(device_index):
    return lib.GetDevicePropertyDisplayAspect(device_index)

lib.GetDevicePropertyPitch.restype = c_float
lib.GetDevicePropertyPitch.argtypes = [c_int]
def GetDevicePropertyPitch(device_index):
    return lib.GetDevicePropertyPitch(device_index)

lib.GetDevicePropertyTilt.restype = c_float
lib.GetDevicePropertyTilt.argtypes = [c_int]
def GetDevicePropertyTilt(device_index):
    return lib.GetDevicePropertyTilt(device_index)

lib.GetDevicePropertyCenter.restype = c_float
lib.GetDevicePropertyCenter.argtypes = [c_int]
def GetDevicePropertyCenter(device_index):
    return lib.GetDevicePropertyCenter(device_index)

lib.GetDevicePropertySubp.restype = c_float
lib.GetDevicePropertySubp.argtypes = [c_int]
def GetDevicePropertySubp(device_index):
    return lib.GetDevicePropertySubp(device_index)

lib.GetDevicePropertyFringe.restype = c_float
lib.GetDevicePropertyFringe.argtypes = [c_int]
def GetDevicePropertyFringe(device_index):
    return lib.GetDevicePropertyFringe(device_index)

lib.GetDevicePropertyRi.restype = c_int
lib.GetDevicePropertyRi.argtypes = [c_int]
def GetDevicePropertyRi(device_index):
    return lib.GetDevicePropertyRi(device_index)

lib.GetDevicePropertyBi.restype = c_int
lib.GetDevicePropertyBi.argtypes = [c_int]
def GetDevicePropertyBi(device_index):
    return lib.GetDevicePropertyBi(device_index)

lib.GetDevicePropertyInvView.restype = c_int
lib.GetDevicePropertyInvView.argtypes = [c_int]
def GetDevicePropertyInvView(device_index):
    return lib.GetDevicePropertyInvView(device_index)

lib.GetDevicePropertyQuiltX.restype = c_int
lib.GetDevicePropertyQuiltX.argtypes = [c_int]
def GetDevicePropertyQuiltX(device_index):
    return lib.GetDevicePropertyQuiltX(device_index)

lib.GetDevicePropertyQuiltY.restype = c_int
lib.GetDevicePropertyQuiltY.argtypes = [c_int]
def GetDevicePropertyQuiltY(device_index):
    return lib.GetDevicePropertyQuiltY(device_index)

lib.GetDevicePropertyTileX.restype = c_int
lib.GetDevicePropertyTileX.argtypes = [c_int]
def GetDevicePropertyTileX(device_index):
    return lib.GetDevicePropertyTileX(device_index)

lib.GetDevicePropertyTileY.restype = c_int
lib.GetDevicePropertyTileY.argtypes = [c_int]
def GetDevicePropertyTileY(device_index):
    return lib.GetDevicePropertyTileY(device_index)

lib.GetVertexShaderGLSL.restype = c_char_p
def GetVertexShaderGLSL():
    return lib.GetVertexShaderGLSL().decode('utf-8')

lib.GetFragmentShaderGLSL.restype = c_char_p
def GetFragmentShaderGLSL():
    return lib.GetFragmentShaderGLSL().decode('utf-8')
