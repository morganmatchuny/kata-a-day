#The rgb() method is incomplete. Complete the method 
#so that passing in RGB decimal values will result 
#in a hexadecimal representation being returned. 
#The valid decimal values for RGB are 0 - 255. 
#Any (r,g,b) argument values that fall out of that 
#range should be rounded to the closest valid value.

def limit(rgb):
    if rgb < 0:
        return 0
    elif rgb > 255: 
        return 255
    else:
        return rgb
        
def to_hex(rgb):
    hex_code = hex(limit(rgb))[2:]
    return hex_code.zfill(2).upper()
    
def rgb(r, g, b):
    return to_hex(r) + to_hex(g) + to_hex(b)
