import time 
def transaction_data():
    from_val = input("From: ")
    to_val = input("To: ")
    amount_val = input("Amount: ")
    return from_val, to_val,amount_val  
#def create_output_file():Y

def main():
    choice = input("Do you want to add a new transaction(Y/N)?: ")
    file = open("transactions.txt","r")
    lineList = file.readlines()
    file.close

    counter = int(lineList[-1].split(" ",1)[0]) + 1
    file = open("transactions.txt","a")  
    while choice == 'Y': 
        frm, to, amnt = transaction_data()
        file.write(str(counter) + " From: "+frm+ " To: "+to+ " Amount: "+ amnt) #+ " Timestamp: " + str(time.time()) )
        file.write("\n") 
        counter += 1    
        choice = input("Do you want to add a new transaction(Y/N)?: ")
    file.close()
if __name__ == "__main__":
    main() 