import hashlib
import json


class block:
    idx = 0

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        data = str(self.index) + str(self.timestamp) + \
            str(self.previous_hash) + json.dumps(self.data)+str(block.idx)
        data_encode = data.encode()
        res = hashlib.sha256(data_encode).hexdigest()
        return res


block1 = block(0, '2018-01-01', {'hacked': 'hello'}, '0')
print(block1.hash)
