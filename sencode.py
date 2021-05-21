base64str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
hex_encoded = "2AB12E3D3211"


def mybase64_encode(a):
    tmp = ''

    for i in a:
        tmp += (bin(b.index(i, 0, -1))[2:].zfill(4))

    tmp2 = ''

    for i in range(0, len(tmp), 6):
        tmp2 += (base64str[int((tmp[i:i + 6]), 2)])

    return tmp2


print(hex_encoded)
print(mybase64_encode(hex_encoded))