###########
#   Connor McKellips
#   Nick Raffel
#
#   Applied Cryptography - MSCS 396
#   This is a Coding assignment that demonstrates basic blockchain cryptography
#   A product block contains data of the item, company, store, owner, etc.
#   It also creates a keyed hash based on that information
#
############

import hashlib

# Class to set up the blockchain, hashes, and ability to compare them
class BC:
    # initializes a product block upon creation
    def __init__(self, previousHash, company, item, owner):
        # creates the block's previous hash, company, item, and owner
        self.previousHash = previousHash
        self.company = company
        self.item = item
        self.owner = owner

        # Creates the data to placed into each block
        self.block_data = "".join(company) + " : " + "".join(item) + " : " + "".join(owner) + " | " + previousHash
        # Hashes with Sha256 hashing algorithm
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    # creates a predicted hash for product block
    def predictHash(self, company, item, owner, hash):
        # Creates the data to placed into each block
        block_data = "".join(company) + " : " + "".join(item) + " : " + "".join(owner) + " | " + hash
        # Hashes with Sha256 hashing algorinthm
        pre_Hash = hashlib.sha256(block_data.encode()).hexdigest()
        return pre_Hash

    # compares the hashes with each other
    def compare(self, item):
        # prints true if the block holds the correct hash value (product is validated)
        if self.pre_Hash == item.block_hash:
            print( "Hashes look right, this is a real token" )
        else:
            print( "Fake token detected" )

    # adds the product onto the list of products
    def displayProduct(self):
        # prints new hash information
        print("[", self.block_data, "|", "New Block Hash :", self.block_hash, "]")


# simple function for input validation
def check_option(answer):
    # if the input is not a valid character, it prints false
    if not option.isdigit() or int(option) <= 0 or int(option) > 3:
        print("not an option")
        return False
    else:
        return True


# Creates the Initial token
VideoGame = BC("Initialized", "CryptoMart", "VideoGame", "CryptoMart")
Book = BC("Initialized", "CryptoMart", "Book", "CryptoMart")
Monkey_NFT = BC("Initialized", "CryptoMart", "Monkey NFT", "CryptoMart")
print("Welcome to CryptoMart, A secure online market!")
print("Packets look like --> ['Company' : 'Item' : 'Owner' | Old Hash | New Block Hash]")

# Input variable that also acts as a digital signature
name = input("First what is your name?\n>> ")
print("Hi " + name + ", What would you like to buy? ")
print("Here is our stock!")
print("1:", VideoGame.item, "\n2:", Book.item, "\n3:", Monkey_NFT.item)
option = input(">> ")

# While loop for input validation to make sure input is valid
while not check_option(option):
    option = input(">> ")

# if check option is accepted
if check_option(option):
    # option 1 (video game) check
    if option == "1":
        print("Oh, a ", VideoGame.item, "!\nHere's the Block with the Hashes!")
        # creates the new book that you bought and displays the packet
        new_videogame = BC(VideoGame.block_hash, "CryptoMart", "VideoGame", name)
        new_videogame.displayProduct()

        # fake video game that the "hacker" tried to steal while you bought it
        fake_vg = BC(VideoGame.block_hash, "CryptoMart", "Book", "Hacker")
        print("Looks like a hacker is trying to take your new Video Game!",
              "\nFortunately, we can compare the hashes to check the integrity")
        print("Your Hash:\t\t", new_videogame.block_hash, "\nHacker's Hash:\t", fake_vg.block_hash)

        # creates the predicted hash that the Crypto store is anticipating
        needed_hash = BC.predictHash("", "CryptoMart", "VideoGame", name, VideoGame.block_hash)
        print("Needed Hash:\t", needed_hash)

        # if the needed hash is the same as your hash then it's accepted
        if needed_hash == new_videogame.block_hash:
            print("Your hash, is the accepted Hash!")
        else:
            print("Error, your hash was not the right hash.")

    # option 2 (book) check
    if option == "2":
        print("Oh, a ", Book.item, "!\nHere's the Block with the Hashes!")
        # creates the new book that you bought and dispays the packet
        new_book = BC(Book.block_hash, "CryptoMart", "Book", name)
        new_book.displayProduct()

        # fake book that the "hacker" tried to steal while you bought it
        fake_book = BC(Book.block_hash, "CryptoMart", "Book", "Hacker")
        print("Looks like a hacker is trying to take your new Book!",
              "\nFortunately, we can compare the hashes to check the integrity")
        print("Your Hash:\t\t", new_book.block_hash, "\nHacker's Hash:\t", fake_book.block_hash)

        # creates the predicted hash that the Crypto store is anticipating
        needed_hash = BC.predictHash("", "CryptoMart", "Book", name, Book.block_hash)
        print("Needed Hash:\t", needed_hash)

        # if the needed hash is the same as your hash then it's accepted
        if needed_hash == new_book.block_hash:
            print("Your hash, is the accepted Hash!")
        else:
            print("Error your hash, was not the right hash.")

    # option 3 (monkey NFT) check
    if option == "3":
        print("Oh, a ", Monkey_NFT.item, "!\nHere's the Block with the Hashes!")
        # creates the new book that you bought and dispays the packet
        new_monkey_nft = BC(Monkey_NFT.block_hash, "CryptoMart", "Monkey NFT", name)
        new_monkey_nft.displayProduct()

        # fake NFT that the "hacker" tried to steal while you bought it
        fake_nft = BC(Monkey_NFT.block_hash, "CryptoMart", "Monkey NFT", "Hacker")
        print("Looks like a hacker is trying to take your new Book!",
              "\nFortunately, we can compare the hashes to check the integrity")
        print("Your Hash:\t\t", new_monkey_nft.block_hash, "\nHacker's Hash:\t", fake_nft.block_hash)

        # creates the predicted hash that the Crypto store is anticipating
        needed_hash = BC.predictHash("", "CryptoMart", "Monkey NFT", name, Monkey_NFT.block_hash)
        print("Needed Hash:\t", needed_hash)

        # if the needed hash is the same as your hash then it's accepted
        if needed_hash == new_monkey_nft.block_hash:
            print("Your hash, is the accepted Hash!")
        else:
            print("Error your hash, was not the right hash.")