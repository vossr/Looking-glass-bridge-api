#ifndef BRIDGE_API_H
#define BRIDGE_API_H

#ifdef __cplusplus
extern "C" {
#endif

__declspec(dllexport) char *InitializeApp(void);
__declspec(dllexport) void  CloseApp(void);
__declspec(dllexport) char *GetHoloPlayCoreVersion(void);
__declspec(dllexport) char *GetHoloPlayServiceVersion(void);
__declspec(dllexport) int   GetNumDevices(void);
__declspec(dllexport) char *GetDeviceHDMIName(int device_index);
__declspec(dllexport) char *GetDeviceType(int device_index);
__declspec(dllexport) int   GetDevicePropertyInt(int device_index, char *property_str);
__declspec(dllexport) int   GetDevicePropertyWinX(int device_index);
__declspec(dllexport) int   GetDevicePropertyWinY(int device_index);
__declspec(dllexport) int   GetDevicePropertyScreenW(int device_index);
__declspec(dllexport) int   GetDevicePropertyScreenH(int device_index);
__declspec(dllexport) float GetDevicePropertyDisplayAspect(int device_index);
__declspec(dllexport) float GetDevicePropertyPitch(int device_index);
__declspec(dllexport) float GetDevicePropertyTilt(int device_index);
__declspec(dllexport) float GetDevicePropertyCenter(int device_index);
__declspec(dllexport) float GetDevicePropertySubp(int device_index);
__declspec(dllexport) float GetDevicePropertyFringe(int device_index);
__declspec(dllexport) int   GetDevicePropertyRi(int device_index);
__declspec(dllexport) int   GetDevicePropertyBi(int device_index);
__declspec(dllexport) int   GetDevicePropertyInvView(int device_index);
__declspec(dllexport) int   GetDevicePropertyQuiltX(int device_index);
__declspec(dllexport) int   GetDevicePropertyQuiltY(int device_index);
__declspec(dllexport) int   GetDevicePropertyTileX(int device_index);
__declspec(dllexport) int   GetDevicePropertyTileY(int device_index);
__declspec(dllexport) char *GetVertexShaderGLSL(void);
__declspec(dllexport) char *GetFragmentShaderGLSL(void);

#ifdef __cplusplus
}
#endif

#endif /* BRIDGE_API_H */
