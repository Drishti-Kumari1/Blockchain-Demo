import hashlib

def hash_block(data):
    return hashlib.sha256(data.encode()).hexdigest()

data = "Student Record: Drishti - BTech 2nd Year"
print("Hash of data:", hash_block(data))
