from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
import os





base_dir = Path(__file__).resolve().parent
print(base_dir)


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

print(private_key)
print(public_key)


pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(pem)
f.close()

private_key_path = os.path.join(base_dir, 'private_key.pem') 
with open(private_key_path, 'rb') as private_key_file:
    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=None,
        backend=default_backend()
    )

    private_key_file.close()

# public_key = private_key.public_key()

with open(private_key_path, 'rb') as public_key_file:
    public_key = serialization.load_pem_public_key(
        public_key_file.read(),
        backend=default_backend()
    )
    public_key_file.close()

print(public_key)

# with open(private_key_path, "rb") as key_file:
#     public_key = serialization.load_pem_public_key(
#         key_file.read(),
#         backend=default_backend()
#     )



print(private_key)
# print(private_key.public_key())


