import time
import hashlib

def calculate_nonce(block_index, previous_hash, new_transaction):
    print(block_index,previous_hash,new_transaction)
    nonce = 0
    new_block = []
    new_block.append(str(block_index) + " " + str(time.time()) + \
        " " + new_transaction + " " + previous_hash + " ")
    print(new_block)    
    while nonce<=50001 :
        #print(nonce)
        new_block_str = new_block[-1] + " " + str(nonce) 
        sh256 = hashlib.sha256(new_block_str.encode()).hexdigest()
        bin_sh256 = bin(int(sh256,16))[2:]
        if len(bin_sh256.split('1',1)[0]) == 14 or nonce == 50001:
            file = open('blockchain.txt','a')
            #file.write('\n')
            file.write('\n' + str(block_index) + " " + str(sh256) + " " + str(nonce))
            file.close()
            print("nonce = ", nonce)
            break
        nonce += 1

def latest_transaction_index():
    file = open("transactions.txt","r")
    lineList = file.readlines()
    file.close
    return int(lineList[-1].split(" ",1)[0]) + 1

def get_choice():
    return input("Do you want to look for a new transaction(Y/N)?: ")

def main():
    # open the blockchain.txt file in append mode
    file = open("blockchain.txt","r")
    firstLine = file.read(1)
    file.close()
    #check if the file is empty
    current_tr_index = latest_transaction_index()
    if not firstLine:
        file = open("blockchain.txt","a")
        block = []
        data = "first block"
        block.append(str(0) + data + str(time.time()) + str(hashlib.sha256(data.encode()).hexdigest()))
        file.write(str(0) + " " + str(hashlib.sha256(data.encode()).hexdigest()) )
        file.close()     
    choice = get_choice()
    while choice == 'Y':
        if current_tr_index == latest_transaction_index():
            print("No new transaction detected!!")
            choice = get_choice()
        else:
            while current_tr_index < latest_transaction_index():
                file = open("transactions.txt","r")
                newLine = file.readlines()[current_tr_index]
                print(newLine)
                file.close()
                
                file = open("blockchain.txt","r")
                lineList_blck = file.readlines()
                file.close
                prev_hash = lineList_blck[-1].split(" ",1)[1]
                blc_indx = int(lineList_blck[-1].split(" ",1)[0])

                print(prev_hash, blc_indx)
                calculate_nonce(blc_indx+1, prev_hash, newLine)
                current_tr_index += 1 



if __name__ == "__main__":
    main()