from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import pathlib
import os


base_dir = pathlib.Path(__file__).resolve().parent

text = "This means you can use either key but I will demonstrate using the public key to encrypt, this will mean anyone with the private key can decrypt the message."

btext = text.encode()

public_key = None

private_key_path = os.path.join(base_dir, 'private_key.pem')

with open(private_key_path, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend(),
    )

    key_file.close()

public_key = private_key.public_key()


""" 
Encrypting
"""
encrypted = public_key.encrypt(
    btext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(encrypted)


""" 
Decrypting
"""
original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)