from ecdsa import SigningKey, SECP256k1
signing_key = SigningKey.generate(curve=SECP256k1)
print(signing_key)
 
verification_key = signing_key.verifying_key
print(verification_key)
 
signature = signing_key.sign(b"Not your keys, not your coins!")
print(signature)

assert vk.verify(signature, b"Not your keys, not your coins!")
