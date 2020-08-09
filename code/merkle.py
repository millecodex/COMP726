# lets get a merkle tree up and running
# todo: file I/O
# what is the 'proper' ordering?
import hashlib
root = ''


def hash_leaves(child1, child2):
    parent=hashlib.sha256((child1+child2).encode())
    return parent.hexdigest()


def merkle (tx):
    tree=[]
    if len(tx) %2 == 1:
        tx.append('')
    while len(tx) > 1:     
        child1=tx.pop()
        child2=tx.pop()
        parent = hash_leaves(child1,child2)
        tree.append(parent)
    if len(tree)>1:
        new_tree=tree.copy()
        return merkle(new_tree)
    elif len(tree) == 1:
        return tree[0]


# main flow
# if there is only 1 tx, then the root is just the tx hash
def make_tree(tx_list):
    if len(tx_list) == 0:
        root = 'null'
    elif len(tx_list) == 1:
        root = tx[0]
    else:
        temp_tx = tx_list.copy()
        root = merkle(temp_tx)
    return root


#TX list
tx = [  
    "3c1995689fe1f1a5d19b4e55a111bde55212eab8394dfba9a495452b23f7d5ca",
	"c9e89e198b72772c9dd93d4ae3e1c64f32de1a672bf4109f747e5f8e436650f3",
	"3f10da700c8d294b15872f367fb8d05b93482366682317637e8e4a7360bb8278",
	"e645efaec28e8bf093a4e20f157a2b8f0e14f20c51dd5e5919290e0e0b059d96",
	"546767ae6b6704d50ac3baf3acb159650c9974b38b339c581334976a5276af86",
	"ff64ba03f61260b85285942c1d33dad21c031f2ba5bc8f10c758501338822617",
	"64eb48e744a28f407f1207680ff118030073075720a2fc12f029cc3811ebe23e",
	"11816dc3f1bca0ce6b65d363b0a149a47b25ac00057ce64c830834c7c6a2d257",
	"de63d532a60f4ae4e660e7e999420bd8ce22738442134e935d38419a9cf1fd71",
	"bf7aafae10a6b5f0655425418d0cb285746304644b17b1d0d30bb5b3b67d31c0",
	"e0da60ed06c3e36eb80636183b74c01b6057e7ddb6dce12735a5ff5f3e1d2851",
	"391787228c2fd91e1ac92ef7324202b2063925eb7c84568620e79919805b435a",
	"fd27ffa0ebe064b30c282ac9bc24667f022701cea8f8d637f3cbe2c01559571e"
    ]


# Find the Merkle root
root=make_tree(tx)
print('Merkle Root is: ')
print(root)