"""
Tutorial: Proof of Work - Mining

**_Proof of work_** is the unique contribution to the bitcoin protocol that achieves two aims:
1. allows nodes to vote with their hashpower to achieve consensus
2. keeps the network secure by aligning incentives.
------------------------------------------
@file: pow.py
@updated: August 08, 2020
@author: Jeff Nijsse
------------------------------------------
"""
import hashlib
import pickle
import time
import secrets

# Prepare a block to be mined
# we will need pickle to turn our block into a byte object
# sha256 operates one byte at a time
# create a new block using sample values
block = {   'timestamp': 1553200425.597771,
            'transactions': ['a','b','c'],
            'prev_hash': '00574faf29dbb37a3b12c2f8f5c05cf03c708313d4ad1d5d968cd2438beea104',
            'merkle_root': 'aa0522a507b6499cb3512494908ac9220',
        }

# pickle the block
pickled_block = pickle.dumps(block)
print(pickled_block)

# hash the block and output a digest of hexidecimal digits
hashed_block = hashlib.sha256(pickled_block).hexdigest()
print(hashed_block)

# introduce a variable that is added to the block what when changed can change the hash
# this is called a nonce
# choose 16 because a hex output has 16 digits
for nonce in range(16):
    print(str(nonce)+'_block_nonce')

for nonce in range(16):  
    print(hashlib.sha256((str(nonce)+'block_nonce').encode()).hexdigest())

# set the number of leading zeroes to act as a target difficulty
target = 1

# loop through the hashes checking each one
for nonce in range(16):  
    hash = hashlib.sha256((str(nonce)+'block_nonce').encode()).hexdigest()
    print(str(hash))
    
    # check the string up to the indexed difficulty and compare
    # note python string manipulation: '0'*5 = 00000; this is string multiplication
    if hash[:target] == '0'*target:
        print('Block Found!')
        break
        
    # end of range condition
    if nonce == 15: print('Block not found')

"""Our loop breaks after 12 iterations because we've satisfied the condition; in this case finding a single leading zero.
"""

# hash the block, not just a string
# !!caution!! - setting difficulty too high could result in waiting until the heat death of the universe to find your block
target = 4
nonce = 1
block_found = False

# this will loop until a block is found
while block_found == False:
    # add a nonce value to the block, here it is prepended
    work = hashlib.sha256(bytes(nonce) + pickled_block)
    
    # check to see if the hash meets the target
    if work.hexdigest()[:target] == '0'*target:
        block_found = True
        
        # output some data
        print('Target Difficulty: ' + str(target))
        print('Nonce: ' + str(nonce))
        print('Proof-of-work: ' + work.hexdigest())
        
    # update the nonce before looping
    # this ensures the block is different before it is hashed again    
    nonce += 1
    
# Add a system timer for analysis
target = 4
nonce = 1
block_found = False

# access the system clock and record the start time
start = time.time()
while block_found == False:
    work = hashlib.sha256(bytes(nonce) + pickled_block)
    if work.hexdigest()[:target] == '0'*target:
        end = time.time()
        block_found = True
        print('Target Difficulty: ' + str(target))
        print('Nonce: ' + str(nonce))
        print('Proof-of-work: ' + work.hexdigest())
        
        # calculate and print the time; this will output in seconds
        print('Elapsed time: ' + str(end - start))
    nonce += 1

# Generate random blocks
# secrets provides access to a secure random number generator
# Always be cautious when generating random data for important purposes like keys

# generate random data to append to a block
random_data = secrets.token_bytes(4)
target = 4
nonce = 1
block_found = False
start = time.time()
while block_found == False:
    # the block now contains 4 random bytes of data
    work = hashlib.sha256(bytes(nonce) + pickled_block + random_data)
    if work.hexdigest()[:target] == '0'*target:
        end = time.time()
        block_found = True
        print('Target Difficulty: '+ str(target))
        print('Nonce: ' + str(nonce))
        print('Proof-of-work: ' + work.hexdigest())
        print('Elapsed time: ' + str(end - start))
    nonce += 1


# Lets look at the probability of finding a block.

# one leading zero to start
diff = 1
prob = 1/16
print(prob)

# variable leading digits
diff = 2
prob = 1/(16**diff)
print(prob)

#loop through a range and print the results
#range(start,stop,step)
for diff in range(1,16,1):
  prob = 1/(16**diff)
  #formatted to show the relative value
  print("%.20f" % prob)

#same as above only stored in an array (python list) to plot
prob=[]
for diff in range(1,11,1):
  prob.append(1/(16**diff))
print(prob)

#plot using matplotlib
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_xlabel('difficulty')
ax.set_ylabel('probability')
ax.plot(prob,'r*')
plt.show()

# Difficulty
Up to this point we have used the term target difficulty to mean the number of leading bits that are zero in a hexidecimal format. When looking up difficulty you will get a different value, for example: the difficulty when Bitcoin block 642428 was mined was 16847561611550.27

#calculate bitcoin's difficulty
#the maximum number of values that can be output 
#from SHA256 are 2^256 -1, or approximately 
#0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
set_size = 0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(set_size)

#recently found block's proof of work (copied from web)
recent_PoW = 0x00000000000000000006a19bf1ef2f829baf3937d3ed11d6d545b947f3214aef
print(recent_PoW)

#calculate difficulty value
difficulty = set_size / recent_PoW
print(difficulty)