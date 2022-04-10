import hashlib

class BC:
    def __init__(self, previousHash, transactionList):
        self.previousHash = previousHash
        self.transactionList = transactionList

        #Creates the data to placed into each block
        self.block_data = "-".join(transactionList) + "-" + previousHash
        #Hashes with Sha256 hashing algorinthm
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

bc = BC("bob", "1")
bc.displayBlock()