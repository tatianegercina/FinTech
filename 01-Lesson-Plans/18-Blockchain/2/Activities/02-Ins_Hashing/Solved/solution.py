# Hashing Demo

# initial imports
import hashlib

# output sha256 hash in hexadecimal string format
def hash(message):
    return hashlib.sha256(message).hexdigest()

sentence_one = b"The quick brown fox jumped over the lazy dog"

print(sentence_one, hash(sentence_one))
# output: 7d38b5cd25a2baf85ad3bb5b9311383e671a8a142eb302b324d4a5fba8748c69

sentence_two = b"The quick brown fox jumped over the lazy dog"

print(sentence_two, hash(sentence_two))
# output: 7d38b5cd25a2baf85ad3bb5b9311383e671a8a142eb302b324d4a5fba8748c69

payment_message = b"I agree to pay Joe $90"

print(payment_message, hash(payment_message))
# output: 8784fee852b5ee466c49b331098286feebc7c0d03ebf6ba826833fac376f4607

payment_message = b"I agree to pay Joe $9"

print(payment_message, hash(payment_message))
# output: eee60f2df1736fb21297cd062d81eaa6f9f95241bf38c04a4db4ff264a0bae72
