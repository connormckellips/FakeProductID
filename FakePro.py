import hashlib


class BC:
    # initializes a product block upon creation
    def __init__(self, previousHash, company, item, owner):
        # previous hash is a reference to the previous block
        self.previousHash = previousHash
        self.company = company
        self.item = item
        self.owner = owner

        # Creates the data to placed into each block
        self.block_data = "".join(company) + " : " + "".join(item) + " : " + "".join(owner) + " | " + previousHash
        # Hashes with Sha256 hashing algorinthm
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    # creates a predicted hash for product block
    def predictHash(self):
        # Creates the data to placed into each block
        self.block_data = "".join(self.company) + " : " + "".join(self.item) + " : " + "".join(self.owner) + " | " + self.previousHash
        # Hashes with Sha256 hashing algorinthm
        self.pre_Hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        print("Predicted Block Hash :", self.block_hash)

    # compares the hashes with each other
    def compare(self, item):
        # pre_hash item we are creating
        if self.pre_Hash == item.block_hash:
            print( "Hashes look right, this is a real token" )
        else:
            print( "Fake token detected" )

    # adds the product onto the list of products
    def displayProduct(self):
        self.predictHash()
        print("[", self.block_data, "|", "New Block Hash :", self.block_hash, "]")


# prints what the product information should look like to the user
print("\nPackets look like --> ['Company' : 'Item' : 'Owner' | Old Hash | New Block Hash]\n")
# creates the initial product and adds it into the blockchain, checks if it is fake
bc = BC("No Hash Made Yet", "Walmart", "VideoGame", "Walmart")
bc.displayProduct()
bc.compare(bc)

print("---------------------------------------------------------------------------------------------------")
# creates a second block and adds it into the blockchain, checks if it is fake
realItem = BC(bc.block_hash, "Walmart", "VideoGame", "Bob")
realItem.displayProduct()
realItem.compare(realItem)

print("---------------------------------------------------------------------------------------------------")
fakeItem = BC(bc.block_hash, "Walmart", "VideoGame", "Hacker")
fakeItem.displayProduct()

fakeItem.compare(realItem)


