import time
import hashlib


class AccToken:
    def __init__(self, user_nonce, user_key):
        self.user_nonce = user_nonce
        self.user_key = user_key

    def generate(self):
        timestamp = int(time.time())
        hash = hashlib.sha256()
        hash.update(f"{timestamp}{self.user_key}".encode())
        return f"{self.user_nonce}:{timestamp}:{hash.hexdigest()}"
