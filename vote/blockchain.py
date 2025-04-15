# vote/blockchain.py
import datetime
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data='Genesis Block', previous_hash='0')

    def create_block(self, data, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = f"{block['index']}{block['timestamp']}{block['data']}{block['previous_hash']}".encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]

    def get_chain(self):  # ✅ Optional: required for blockchain viewer
        return self.chain

# ✅ THIS MUST BE AT THE BOTTOM, OUTSIDE THE CLASS
blockchain = Blockchain()
