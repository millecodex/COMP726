"""
# Tutorial: Create a block to store transaction data and hash using python's hashlib
To be useful the data will contain many fields such as:<br>
 - identifier
 - timestamp
 - previous hash (to make the chain)
 - merkle root
 - list of transactions (the data of interest)
 
These can be stored in a python dictionary which is a key-value structure. Think of the key as an index.

`dict = {key_1:value_1,
         key_2:value_2,
        .
        .
        .
        key_n:value_n   
}`
------------------------------------------
@file: block_creation.py
@updated: August 08, 2020
@author: Jeff Nijsse
------------------------------------------
"""

import hashlib as hash
import pickle

# initialize a genesis block. Note 'transactions' is initialized as an empty list
block = {
    'height':1,
    'time':0,
    'prevHash':'this is the genesis block',
    'merkleRoot': '',
    'transactions': []
        }
#print(block)

# create a transaction, in this case a string
transaction='Pay $1,000,000 to Jeff'
#print(transaction)


encoded_tx = transaction.encode()
#print(encoded_tx)

hashed_tx = hash.sha1(encoded_tx)
#print(hashed_tx)

#The `digest()` and `hexdigest()` methods will output byte objects and hex strings respectively
#print(hashed_tx.digest())
#print(hashed_tx.hexdigest())

#Lets store this transaction and add it to the block we created above.
hex_tx = hashed_tx.hexdigest()
block["transactions"].append(hex_tx)
#print(block)

# Create a new block and append it to the chain
""" This block only has a single transaction (perhaps its the block reward to Jeff ;) Now we will create a new block and append it to the chain. The block is created in the same manner, except we must make a few updates:

1.   the blockheight is now incremented by 1
2.   the time is incremented by 1
3.   the prevHash field with the hash of the genesis block. This will ensure the state of the blockchain is preserved moving forward.

some attributes have been hard-coded for simplicity
"""
block2 = {
    'height':2,
    'time':1,
    'prevHash':'null',
    'merkleRoot': 'null',
    'transactions': []
    }

# create a transaction and add it to the block
tx = hash.sha1('Alice +10'.encode()).hexdigest()
block2["transactions"].append(tx)
block2["merkleRoot"] = tx
#print(block2)

# link the blocks -> hash the genesis block object
# use pickle for serialization, then hash and store digest
# convert to a byte object
byte_genesis = pickle.dumps(block)

# compress to a human-readable SHA-1 digest
hash_genesis = hash.sha1(byte_genesis).hexdigest()
#print('\n')
#print(hash_genesis)

# set the prevHash and print the block
block2["prevHash"] = hash_genesis
#for key, value in block2.items():
#    print(key+': '+str(value))

# Modify a transaction to attack the chain
# change the dollar sign to a negative sign in the original transaction
new_transaction = 'Pay -1,000,000 to Jeff'
hashed_new_tx=hash.sha1(new_transaction.encode()).hexdigest()

# update the block with the new tx; recall 'block' is the original or genesis block; our tx was at position 0
block["transactions"][0]=hashed_new_tx

# hash the updated block
import pickle
byte_genesis_new = pickle.dumps(block)
hash_genesis = hash.sha1(byte_genesis_new).hexdigest()

# compare hashes
#if block2["prevHash"] != hash_genesis:
#    print('Your chain has been attacked!!')

print('uncomment the print statements to follow along')    
