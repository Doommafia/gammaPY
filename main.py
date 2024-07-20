import ctypes
from ctypes import wintypes
import os

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# context handle
dc = user32.GetDC(0)

# gamma ramp
def set_gamma_ramp(gamma):
    gamma_array = (wintypes.WORD * 256)()
    for i in range(256):
        value = int(((i / 255.0) ** (1.0 / gamma)) * 65535 + 0.5)
        gamma_array[i] = min(max(value, 0), 65535)

    ramp_array = (wintypes.WORD * (256 * 3))(*gamma_array, *gamma_array, *gamma_array)
    gdi32.SetDeviceGammaRamp(dc, ctypes.byref(ramp_array))

if __name__ == "__main__":
    if os.path.exists("gammaTemp.txt"):
        new_gamma = 1.0
        os.remove("gammaTemp.txt")
    else:
        new_gamma = 1.5
        with open("gammaTemp.txt", "w") as file:
            file.write("1.5")
    
    set_gamma_ramp(new_gamma)
    print(f"Gamma set to {new_gamma}")
