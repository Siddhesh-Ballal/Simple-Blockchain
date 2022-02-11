import hashlib
from json.tool import main
from unittest import result

def hashgenerator(data):
    result = hashlib.sha3_256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class Blockchain:
    def __init__ (self):
        hashLast = hashgenerator('Hash of Last block')
        hashStart = hashgenerator('Hash of First block')

        genesis = Block('First block of the Blockchain', hashStart, hashLast)
        self.chain = [genesis]

    def addBlock(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashgenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)


my_blockchain = Blockchain()
my_blockchain.addBlock("I'm the 2nd block")
my_blockchain.addBlock("And this is the 3rd!")
my_blockchain.addBlock("While this is the 4th")
my_blockchain.addBlock("Finally this is the 5th!!")

for each_block in my_blockchain.chain:
    print("\nBlock data: ", my_blockchain.__dict__)

 