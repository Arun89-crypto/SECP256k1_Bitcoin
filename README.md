# SECP256k1_Bitcoin

This is the cryptography algorithm used in bitcoin to generate public and private keys.  
Bitcoin uses SECP256k1 C-language library to use this encryption in the Bitcoin operating system.

### Installations

```sh
pip3 install pycryptodome
```

### Imports

```py
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
```
