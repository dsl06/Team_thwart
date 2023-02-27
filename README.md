# Basic implementation of blockchain using python
This is a simple implementation of blockchain working using python 

In this we used the basic concepts of blockchain which are:
1.genisis_block
2.Hashing
3.consensus
4.nonce

Working of this program:
in this program we stored an some dummy keys for transactions , we use those keys while running the program
the keys are = ['12345678','1235678','345678']

when you run the program it will ask for the select options,
the options are 
1. Show Blockchain:
    it will show the cuurrent blocks in the blockchain
2. Make transactions: 
    in this option we can do some dummy transactions , by entering reciever key ( which are already in the list ), after the key enter it will verify the key in the list, then initiate the transaction, it will send to the miner to verify ( here in mining we have used the hashcash algorithm for the generation of nonce with difficulty level 4 ). After the successfull verification of transaction, the block will be added to the network.
3. Alter a block :
    in this step we can try to alter a block , it will give some imbalanced output of the blockchain.

block consists of:
1. Hash of Previous block 
2. Transaction details
3. time stamp
4. hash of the block
5. nonce
