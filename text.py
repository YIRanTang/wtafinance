import struct
import ctypes
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
def float2hex(s):
    fp = ctypes.pointer(ctypes.c_float(s))
    cp = ctypes.cast(fp,ctypes.POINTER(ctypes.c_long))
    return hex(cp.contents.value)

def hex_to_float(h):
    i = int(h,16)
    return struct.unpack('<f',struct.pack('<I', i))[0]
def hex2float(h):
    i = int(h,16)
    cp = ctypes.pointer(ctypes.c_int(i))
    fp = ctypes.cast(cp,ctypes.POINTER(ctypes.c_float))
    return fp.contents.value
if __name__ == '__main__':
    f = [1.5,-1.5,3.5,-3.5]
    h = ['410b3333']
    # for i in f:
    #     print(float_to_hex(i),"   |   ",float2hex(i))
    #     h.append(float_to_hex(i))
    print(h)
    for i in h :
        print(round(hex_to_float(i),3),"   |   ",hex2float(i))