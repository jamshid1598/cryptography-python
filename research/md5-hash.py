import hashlib


print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)


def md5_digest(text):
    byte_string = text.encode()
    result = hashlib.md5(byte_string)
    print(result.digest())


def md5_hexdigest(text):
    result = hashlib.md5(text.encode())
    print(result.hexdigest())


if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    md5_digest(text)
    md5_hexdigest(text)