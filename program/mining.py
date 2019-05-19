import time
import hashlib

def calculate_nonce(block):
    nonce = 0
    while nonce<=50001 :
        block[0] = block[0] + str(nonce)
        sh256 = hashlib.sha256(block[0].encode()).hexdigest()
        #if the message digest has 14 zeros:
        #   update the BC with the successful hash
        #   Break
        #print("hello")
        #if nonce = 500001:
            # Update the BC
        #    break
        nonce += 1

def detect_new_transaction():
    return 1
#        , data = " + "first block" + ", timestamp = " +str(time.time()) +
 


def main():
    file = open("blockchain.txt","w")
    block = []
    block.append(str(0) + "first block" + str(time.time()) + str(hashlib.sha256("first block".encode()).hexdigest()))
    file.write("index = "+str(0)+ \
        ", hash =" + str(hashlib.sha256("first block".encode()).hexdigest()) )
    while detect_new_transaction() == 1:
         # previous block
        calculate_nonce(block)


if __name__ == "__main__":
    main()