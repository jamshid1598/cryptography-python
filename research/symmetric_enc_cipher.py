from cProfile import label
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes,
)
import os
import base64

backend = default_backend()


plaintext = """ 

What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Why do we use it?

It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).

Where does it come from?

Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
Where can I get some?

There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
"""



def fix_binary_data_length(binary_data):
    """
    Right padding of binary data with 0 bytes
    Fix "ValueError: The length of the provided data is not a multiple of the block length."
    """
    block_length = 16
    binary_data_length = len(binary_data)
    length_with_padding = (
        binary_data_length + (block_length - binary_data_length) % block_length
    )
    return binary_data.ljust(length_with_padding, b"\0"), binary_data_length


def encrypt(binary_data, key):
    binary_data, binary_data_length = fix_binary_data_length(binary_data)
    key = base64.b64decode(key)
    iv = os.urandom(
        16
    )  # does not need to be secret, but must be unpredictable at encryption time
    
    # AES (Advanced Encryption Standard) is a block cipher standardized by NIST. AES is both fast, and cryptographically strong. It is a good default choice for encryption.
    # CBC (Cipher Block Chaining) is a mode of operation for block ciphers. It is considered cryptographically strong. (see https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.CBC)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(binary_data) + encryptor.finalize()
    stored_encrypted_data = "AES.MODE_CBC${iv}${binary_data_length}${encrypted_data})".format(
        iv=str(base64.b64encode(iv), 'utf-8'),
        binary_data_length=binary_data_length,
        encrypted_data=str(base64.b64encode(encrypted_data), 'utf-8'),
    )
    return stored_encrypted_data


def decrypt(stored_encrypted_data, key):
    f = lambda x: x.strip()
    algorithm, iv, binary_data_length, encrypted_data = [f(x) for x in stored_encrypted_data.split("$")]
    assert algorithm == "AES.MODE_CBC"
    encrypted_data = base64.b64decode(encrypted_data)
    iv = base64.b64decode(iv)
    key = base64.b64decode(key)
    binary_data_length = int(binary_data_length)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data[:binary_data_length]


if __name__ == "__main__":
    key = os.urandom(32)
    print(key)
    key = str(base64.b64encode(key), 'utf-8')
    
    
    stored_encrypted_data = encrypt(plaintext.encode(), key)
    print(stored_encrypted_data)
    decrypted_data = decrypt(stored_encrypted_data, key)
    print(decrypted_data.decode())
