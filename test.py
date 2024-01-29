from Crypto.Util.number import long_to_bytes
import secrets

hex_value = 0x7112f78c5d4f524f35edb74957785d2fd690484a535428dca879404b4f24edee0704061d6093ee07045a
ct_bytes = long_to_bytes(hex_value)
key_rev = "MSEC{"

key = []
flag = []

for i in range(len(key_rev)):
    key.append(ct_bytes[i] ^ ord(key_rev[i]))
tmp = ct_bytes[40] ^ ord('!')
key.append(tmp)

tmp = ct_bytes[41] ^ ord('}')
key.append(tmp)
print(key)

for i in range(len(ct_bytes)):
    flag.append(ct_bytes[i] ^ key[i % len(key)])

print(bytes(flag))