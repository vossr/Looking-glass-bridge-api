#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include "bridge_api.h"
#include "LookingGlassCoreSDK/HoloPlayCore/include/HoloPlayCore.h"
#include "LookingGlassCoreSDK/HoloPlayCore/include/HoloPlayShaders.h"

char *InitializeApp(void) {
	hpc_client_error error = hpc_InitializeApp("HoloPlayInfo.c", hpc_LICENSE_NONCOMMERCIAL);
	if (error) {
		return "Bridge Service not running";
	}
	return NULL;
}

void CloseApp(void) {
	hpc_CloseApp();
}

char *GetHoloPlayCoreVersion(void) {
	static char buf[1024];
	hpc_GetHoloPlayCoreVersion(buf, 1000);
	return buf;
}

char *GetHoloPlayServiceVersion(void) {
	static char buf[1024];
	hpc_GetHoloPlayServiceVersion(buf, 1000);
	return buf;
}

int GetNumDevices(void) {
	return hpc_GetNumDevices();
}

char *GetDeviceHDMIName(int device_index) {
	static char buf[1024];
	hpc_GetDeviceHDMIName(device_index, buf, 1000);
	return buf;
}

char *GetDeviceType(int device_index) {
	static char buf[1024];
	hpc_GetDeviceType(device_index, buf, 1000);
	return buf;
}

int GetDevicePropertyInt(int device_index, char *property_str) {
	return hpc_GetDevicePropertyInt(device_index, property_str);
}

int GetDevicePropertyWinX(int device_index) {
	return hpc_GetDevicePropertyWinX(device_index);
}

int GetDevicePropertyWinY(int device_index) {
	return hpc_GetDevicePropertyWinY(device_index);
}

int GetDevicePropertyScreenW(int device_index) {
	return hpc_GetDevicePropertyScreenW(device_index);
}

int GetDevicePropertyScreenH(int device_index) {
	return hpc_GetDevicePropertyScreenH(device_index);
}

float GetDevicePropertyDisplayAspect(int device_index) {
	return hpc_GetDevicePropertyDisplayAspect(device_index);
}

float GetDevicePropertyPitch(int device_index) {
	return hpc_GetDevicePropertyPitch(device_index);
}

float GetDevicePropertyTilt(int device_index) {
	return hpc_GetDevicePropertyTilt(device_index);
}

float GetDevicePropertyCenter(int device_index) {
	return hpc_GetDevicePropertyCenter(device_index);
}

float GetDevicePropertySubp(int device_index) {
	return hpc_GetDevicePropertySubp(device_index);
}

float GetDevicePropertyFringe(int device_index) {
	return hpc_GetDevicePropertyFringe(device_index);
}

int GetDevicePropertyRi(int device_index) {
	return hpc_GetDevicePropertyRi(device_index);
}

int GetDevicePropertyBi(int device_index) {
	return hpc_GetDevicePropertyBi(device_index);
}

int GetDevicePropertyInvView(int device_index) {
	return hpc_GetDevicePropertyInvView(device_index);
}

int GetDevicePropertyQuiltX(int device_index) {
	return hpc_GetDevicePropertyQuiltX(device_index);
}

int GetDevicePropertyQuiltY(int device_index) {
	return hpc_GetDevicePropertyQuiltY(device_index);
}

int GetDevicePropertyTileX(int device_index) {
	return hpc_GetDevicePropertyTileX(device_index);
}

int GetDevicePropertyTileY(int device_index) {
	return hpc_GetDevicePropertyTileY(device_index);
}

char *GetVertexShaderGLSL(void) {
	return (char*)hpc_LightfieldVertShaderGLSL;
}

char *GetFragmentShaderGLSL(void) {
	return (char*)hpc_LightfieldFragShaderGLSL;
}
