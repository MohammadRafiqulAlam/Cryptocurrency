import time 

# function to get transaction input from user
def transaction_data():
    from_val = input("From: ")
    to_val = input("To: ")
    amount_val = input("Amount: ")
    return from_val, to_val,amount_val  

# the main function 
def main():
    choice = input("Do you want to add a new transaction(Y/N)?: ")
    # read from the trnsaction.txt file
    file = open("transactions.txt","r")
    # get how many transactions are recorded?
    firstLine = file.read(1)
    if not firstLine:
        counter = 0
    else: 
        lineList = file.readlines()
        # variable used for tracking number of transactions
        counter = int(lineList[-1].split(" ",1)[0]) + 1
    # close the tranaction file 
    file.close()
    
    while choice == 'Y':
        file = open("transactions.txt","a")  
        # get transaction data  
        frm, to, amnt = transaction_data()
        # write to transaction file
        if counter > 0:
            file.write("\n") 
        
        file.write(str(counter) + " From: "+frm+ " To: "+to+ " Amount: "+ amnt)
        # increment the counter     
        counter += 1    
        file.close()
        choice = input("Do you want to add a new transaction(Y/N)?: ")
if __name__ == "__main__":
    main() 

