"""
Encryption and Hashing with Python
"""
from base64 import urlsafe_b64encode
from hashlib import algorithms_available, sha3_256
from cryptography.fernet import Fernet


def main():
    """
    main function
    """
    print(algorithms_available)
    hash_obj = sha3_256()
    hash_obj.update(b"Hello")
    print(hash_obj.hexdigest())
    hash_obj.update(b"hello")
    print(hash_obj.hexdigest())
    key = Fernet.generate_key()
    print(key)
    cipher = Fernet(key)
    text = b"Hello. Are you there?"
    encrypted_text = cipher.encrypt(text)
    print(encrypted_text)
    other_cipher = Fernet(key)
    decrypted_text = other_cipher.decrypt(encrypted_text)
    print(decrypted_text)
    keyword = b"my secret byte string"
    key = sha3_256(keyword)
    print(key)
    print(key.digest())
    key_bytes = key.digest()
    fernet_key = urlsafe_b64encode(key_bytes)
    print(fernet_key)
    custom_cipher = Fernet(fernet_key)
    encrypted_mess = custom_cipher.encrypt(
        b"This is a string that was encrypted with a base64 from a custom string. "
    )
    print(encrypted_mess)
    print(custom_cipher.decrypt(encrypted_mess))


if __name__ == "__main__":
    main()
