from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import pathlib
import os


base_dir = pathlib.Path(__file__).resolve().parent


with open(os.path.join(base_dir, 'message.txt'), 'rb') as message_file:
    encoded_message = message_file.read()
    message_file.close()
    

private_key_path = os.path.join(base_dir, 'private_key.pem')
public_key = None

with open(private_key_path, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend(),
    )
    key_file.close()
    public_key = private_key.public_key()


if public_key:
    encrypted = public_key.encrypt(
        encoded_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

encrypted_message_file = os.path.join(base_dir, 'message.encrypted')
f = open(encrypted_message_file, 'wb')
f.write(encrypted)
f.close()