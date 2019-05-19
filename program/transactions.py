def transaction_data():
    from_val = input("From: ")
    to_val = input("To: ")
    amount_val = input("Amount: ")
    return from_val, to_val,amount_val  
#def create_output_file():

def main():
    choice = input("Do you want to add a new transaction(Y/N)?: ")
    file = open("transactions.txt","w")
    while choice == 'Y': 
        frm, to, amnt = transaction_data()
        file.write("From: "+frm+ " To: "+to+ " Amount: "+ amnt)
        file.write("\n") 
        choice = input("Do you want to add a new transaction(Y/N)?: ")
    file.close()
if __name__ == "__main__":
    main() 