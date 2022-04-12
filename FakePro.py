import hashlib

class BC:
    def __init__(self, previousHash, company, item, owner):
        # previous hash is a reference to the previous block
        self.previousHash = previousHash
        self.company = company
        self.item = item
        self.owner = owner

        #Creates the data to placed into each block
        self.block_data = "".join(company) + " : " + "".join(item) + " : " + "".join(owner) + " | " + previousHash
        #Hashes with Sha256 hashing algorinthm
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def displayBlock(self):
        print("[", self.block_data, "|", "New Block Hash :", self.block_hash, "]")

    def predictHash(self):
        # Creates the data to placed into each block
        self.block_data = "".join(self.company) + " : " + "".join(self.item) + " : " + "".join(self.owner) + " | " + self.previousHash
        # Hashes with Sha256 hashing algorinthm
        self.pre_Hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        print("Predicted Block Hash :", self.block_hash)

    def compare(self):
        if self.pre_Hash == self.block_hash:
            print( "Hashes look right, this is a real token" )
        else:
            print( "Fake token detected" )


print("\nPackets look like --> ['Company' : 'Item' : 'Owner' | Old Hash | New Block Hash]\n")
bc = BC("Initial string", "Walmart", "VideoGame", "Walmart")
bc.displayBlock()
bc.predictHash()
bc.compare()
print("---------------------------------------------------------------------------------------------------")
bc2 = BC(bc.block_hash, "Walmart", "VideoGame", "Bob")
bc2.displayBlock()
bc2.predictHash()
bc2.compare()
