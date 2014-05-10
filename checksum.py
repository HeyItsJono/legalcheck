import struct

filename = 'venusaur_kirbypwn.pkm'

with open(filename,'rb') as f:
    cs = 0 # checksum starts at 0
    for offset in range (0x08,0x87,2): # starting point, ending point, 2 bytes
        f.seek(offset)
        bytes = f.read(2)
        cs += (bytes[1]<<8)+(bytes[0]) # sum each 2 byte word
    f.seek(0x06)
    bytes = f.read(2)
    cs67 = (bytes[1]<<8) + bytes[0] # checks 2 bytes at 06 and 07
    cs = cs % 0x10000 # truncate lower 2 bytes
    print("checksum: 0x" + hex(cs)[2:].upper())
f.close()

if cs == cs67: # does checksum match the word 06 / 07?
    print("checksum valid!")
else:
    with open(filename,'r+b') as f:
        print("checksum invalid... fixing")
        f.seek(0x06)
        data = struct.pack("H",cs)
        f.write(data)
        print("checksum fixed!")   
f.close()
