# CRYPTOGRAPHY
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def get_generated_key(request, *args, **kwargs):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    
    """
    # serialize encrypted private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    )
    """
    
    # serialize not encrypted private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    
    privateKey = private_pem.decode('utf-8')
    publicKey = public_pem.decode('utf-8')
    
    return privateKey, publicKey