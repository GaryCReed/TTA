import hashlib


def show_algorithms_available():
    print(hashlib.algorithms_guaranteed)


def hashes_match(h1, h2):
    if (h1 == h2):
        return True
    else:
        return False


def get_popular_passwords_from_file(file_name, p_list):
    with open(file_name) as file:
        for line in file:
            line = line.rstrip("\n")
            p_list.append(line)


def get_hashed_password(plaintext_password, algo="sha1"):

    pw = plaintext_password.encode()
    shake = False

    if algo == "sha1":
        hash_object = hashlib.sha1(pw)
    elif algo == "sha256":
        hash_object = hashlib.sha256(pw)
    elif algo == "sha512":
        hash_object = hashlib.sha512(pw)
    elif algo == "sha224":
        hash_object = hashlib.sha224(pw)
    elif algo == "sha384":
        hash_object = hashlib.sha384(pw)
    elif algo == "sha3_256":
        hash_object = hashlib.sha3_256(pw)
    elif algo == "sha3_512":
        hash_object = hashlib.sha3_512(pw)
    elif algo == "sha3_224":
        hash_object = hashlib.sha3_224(pw)
    elif algo == "sha3_384":
        hash_object = hashlib.sha3_384(pw)
    elif algo == "md5":
        hash_object = hashlib.md5(pw)
    elif algo == "blake2b":
        hash_object = hashlib.blake2b(pw)
    elif algo == "blake2s":
        hash_object = hashlib.blake2s(pw)
    elif algo.startswith('shake'):
        shake = True
        if algo == 'shake_128':
            hash_object = hashlib.shake_128()
        if algo == 'shake_256':
            hash_object = hashlib.shake_128()
    else:
        hash_object = None
    
    if shake:
      hex_dig = hash_object.hexdigest(16)
    else:
      hex_dig = hash_object.hexdigest()

    return hex_dig
