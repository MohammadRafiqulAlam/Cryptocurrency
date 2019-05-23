import time
import hashlib

# function that calculates the nonce
def calculate_nonce(block_index, previous_hash, new_transaction):
    #print(block_index,previous_hash,new_transaction)
    # initialize nonce to 0
    nonce = 0
    # an empty block
    new_block = []
    # add data to the block
    new_block.append(str(block_index) + " " + str(time.time()) + \
        " " + new_transaction + " " + previous_hash + " ")
    # print(new_block)    
    while nonce<=50001 :
        #print(nonce)
        # append nonce to the block
        new_block_str = new_block[-1] + " " + str(nonce) 
        # get the sha256 hexdigest
        sh256 = hashlib.sha256(new_block_str.encode()).hexdigest()
        # convert sha256 into binary format 
        bin_sh256 = bin(int(sh256,16))[2:]
        # check if there is 14 zeros at the start or nonce is 50001
        if len(bin_sh256.split('1',1)[0]) == 14 or nonce == 50001:
            file = open('blockchain.txt','a')
            #file.write('\n')
            # write to the blockchain file
            file.write('\n' + str(block_index) + " " + str(sh256) + " " + str(nonce))
            file.close()
            print("nonce = ", nonce)
            break
        nonce += 1

# Retreives the latest transaction from the transaction file
def latest_transaction_index():
    file = open("transactions.txt","r")
    firstLine = file.read(1)
    file.close()
    if not firstLine:
        return 0
    else:  
        file = open("transactions.txt","r")      
        lineList = file.readlines()
        file.close()
        return int(lineList[-1].split(" ",1)[0]) + 1
    
    

# continuously ask for user choice
def get_choice():
    return input("Do you want to look for a new transaction(Y/N)?: ")

def main():
    # open the blockchain.txt file in append mode
    file = open("blockchain.txt","r")
    firstLine = file.read(1)
    file.close()
    # get the lates transaction index
    current_tr_index = latest_transaction_index()
    #check if the file is empty
    if not firstLine:
        file = open("blockchain.txt","a")
        block = []
        # first block data
        data = "first block"
        block.append(str(0) + data + str(time.time()) + str(hashlib.sha256(data.encode()).hexdigest()))
        file.write(str(0) + " " + str(hashlib.sha256(data.encode()).hexdigest()) )
        file.close()
    # get user choice         
    choice = get_choice()
    while choice == 'Y':
        # check if there is any new transaction added to trnsactions.txt file
        if current_tr_index == latest_transaction_index():
            print("No new transaction detected!!")
            choice = get_choice()
        else:
            while current_tr_index < latest_transaction_index():
                # read the transaction
                file = open("transactions.txt","r")
                newLine = file.readlines()[current_tr_index]
                #print(newLine)
                file.close()
                
                # read from the blockchain file
                file = open("blockchain.txt","r")
                lineList_blck = file.readlines()
                file.close()
                # get the previous hash
                prev_hash = lineList_blck[-1].split(" ",1)[1]
                # generate block index
                blc_indx = int(lineList_blck[-1].split(" ",1)[0])

                # print(prev_hash, blc_indx)
                # calculate nonce 
                calculate_nonce(blc_indx+1, prev_hash, newLine)
                current_tr_index += 1 

if __name__ == "__main__":
    main()