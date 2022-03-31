# CRYPTOGRAPHY
from lib2to3.pgen2.token import CIRCUMFLEX
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64



def get_generated_key(request, *args, **kwargs):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
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



def load_key(request, private_key=None, public_key=None, password=None, *args, **kwargs):
    if private_key:
        private_key = serialization.load_pem_private_key(
            private_key.encode(),
            password=password,
        )
        return private_key
    
    elif public_key:
        public_key = serialization.load_pem_public_key(
            public_key.encode(),
        )
        return public_key

    else:
        return None


def encryption_view(request, public_key, message, *args, **kwargs):
    public_key = load_key(request, public_key=public_key, *args, **kwargs)
    cipher_message = None
    
    try:
        cipher_message = public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        cipher_message = str(base64.b64encode(cipher_message),'utf-8')
    except Exception as e:
        print("Error in 'encryption_view': ", e)
    
    return cipher_message


def decryption_view(request, private_key, message, *args, **kwargs):
    private_key = load_key(request, private_key=private_key, *args, **kwargs)
    plain_message = None
    cipher_message = base64.b64decode(message)
    
    try:
        plain_message = private_key.decrypt(
            cipher_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        plain_message = plain_message.decode()
    except Exception as e:
        print("Error in 'decryption_view': ", e)
        
    return plain_message