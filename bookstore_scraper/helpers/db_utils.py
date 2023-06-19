def encode(token):
    encoded = token.encode('utf-8')
    return encoded

def decode(token):
    decoded = token.decode('utf-8', 'replace')
    return decoded

if __name__ == '__main__':
    a = encode('isha')
    print(a)
    decode(a)