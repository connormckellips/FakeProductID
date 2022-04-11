import hashlib

class BC:
    def __init__(self, previousHash, transactionList):
        self.previousHash = previousHash
        self.transactionList = transactionList

        #Creates the data to placed into each block
        self.block_data = "-".join(transactionList) + "-" + previousHash
        #Hashes with Sha256 hashing algorinthm
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def displayBlock(self):
        print(self.block_data)
        print("Signature :",self.block_hash)


t1 = "Bob sends 5 bitcoin to John"
t2 = "Wonton sends 1 bitcoin to John"
t3 = "Wonton sends anita 3 Bitcoin"
t4 = "Anita sends bob 2 bitcoin"

bc = BC("Initial string", [t1,t2])
bc.displayBlock()
print("--------------------")
bc2 = BC("Second Transaction", [t3,t4])
bc2.displayBlock()
