import struct

a= 0x12456
b = struct.pack("<I", a) # Integer non signé little-endian
c = struct.unpack(">I", b)[0] # Dépaquetage de l'entier non signé little-endian

struct.pack("<I", a).hex()

print(a)
print(b)
print(c)

