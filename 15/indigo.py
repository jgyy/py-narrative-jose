"""
Indigo Mission Debrief
"""
from base64 import urlsafe_b64encode
from hashlib import sha3_256
from cryptography.fernet import Fernet


def main():
    """
    main function
    """
    fermat_prime = b"65537"
    key = sha3_256(fermat_prime)
    key_bytes = key.digest()
    fernet_key = urlsafe_b64encode(key_bytes)
    custom_cipher = Fernet(fernet_key)
    mess = (
        b"gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZzi"
        + b"GyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzq"
        + b"ULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6"
        + b"sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY="
    )
    print(custom_cipher.decrypt(mess))


if __name__ == "__main__":
    main()
