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
        print(self.block_hash)


t1 = "Bob sends 5 bitcoin to John"
t2 = "Wonton sends 1 bitcoin to John"
t3 = "Wonton sends 3 bitcoin to Anita"
t4 = "Anita sends 2 Bitcoin to Bob"
t5 = "Wonton send 190 bitcoin to Hacker"
t6 = "Hacker sends 200 bitcoin to Bossman"


bc = BC("Initial string", [t1,t2])
bc.displayBlock()
print("--------------------")
bc2 = BC(bc.block_hash, [t3,t4])
bc2.displayBlock()
print("--------------------")
bc3 = BC(bc2.block_hash, [t5,t6])
bc3.displayBlock()
