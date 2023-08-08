import os
import pandas as pd
import pdfplumber

#TODO: handle a case where the output folder does not exist
#TODO: decide on a default output folder
def extract_all_pdfs(input_folder, output_folder):
    """
    function to extract all pdfs in a folder.
    Parameters:
    - path: path to the folder containing the pdfs
    - output_path: path to the folder where the csv will be saved
    Returns:
    - None
    """

    #iterate over all pdfs in the folder
    for file in sorted(os.listdir(input_folder)):
        all_text = ""
        summ = 0
        file_path = input_folder + "/" + file
        if file.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    # # print(repr(text))
                    # summ += len(text)
                    all_text += text #make one long string for all pages of the pdf

        #flags to check for first instance
        account_no = None
        car_provider = None
        inv_num = None
        inv_date = None
        travel_date = None
        reservation_no = None
        passanger_name = None
        gross_amt = None
        vat = None
        commission = None
        Nett_amt = None 
        Currency = None
        pay_type = None 
        destination = None 

        if "avis" in all_text:

            #agency account number 
            account_no = 269994521
            # print(account_no)
            # #car provider
            car_provider = "ZI C"
            # print(car_provider)
            # # currency
            Currency = "GBP"
            # print(Currency)
            # # payment type 
            pay_type = "Agency"
            # print(pay_type)

            for row in all_text.split('\n'): 
            #Printing invoice number
                # if row.startswith('Invoice No.') and row[-1].isnumeric() and (inv_num is None):
                if 'Invoice No.' in row and row[-1].isnumeric() and (inv_num is None):
                    #we only need the first instance
                    Inv  = row.split()[-1]
                    inv_num = Inv
                    # print("invoice no: ", inv_num) 
                    
            # #invoice date
                if row.startswith('Invoice Date') and (inv_date is None):
                    #we only need the first instance
                    date = row.split()[-1]
                    inv_date = date
                    # print("inv date: ", inv_date)
                
            #Travel date
                if row.startswith('Check-out date') and (travel_date is None):
                    Rdate = row.split()[3]
                    travel_date = Rdate
                    # print("travel date: " , travel_date)
                
            # #Reservation number
                if "Reservation No" in row:
                    Rno = row.split()[-1]
                    reservation_no = Rno
                    # print("reservation number: ", reservation_no)
            # #passanger name

                if row.startswith('Rented by'):
                    rentedby= row.split (':',1)[1].split('Total')[0].strip()
                    passanger_name = rentedby
                    # print("rented by: ", passanger_name)

            # Gross amount 
                if "Net Amount Due" in row:
                    gross_amt = row.split()[-1]
                    # print("gross amt: " , gross_amt)
            # Vat %
                if row.startswith('VAT Charge on Taxable'):
                    vat = row.split("@",1)[1].split()[0]
                    # print("vat: ", vat)
            # comm
                if "Commission @" in row:
                    com = row.split('@')[1].split(' ')[0]
                    commission = com
                    # print("commission: ",commission)
                    
            # nett amount
                if row.startswith('This Invoice is due for payment by'):
                    nett = row.split()[-1]
                    Nett_amt = nett
                    # print("nett amt: " , Nett_amt)
            
            
            # destination
                if row.startswith('Start location'):
                    dest = row.split(':')[1].split('Check-out')[0].strip()
                    destination = dest
                    # print("destination: " , destination)

        if "Enterprise" in all_text:

            #agency account number 
            account_no = 269994521
            # print(account_no)
            # #car provider
            car_provider = "ET C"
            # print(car_provider)
            # # currency
            Currency = "GBP"
            # print(Currency)
            # # payment type 
            pay_type = "Agency"
            # print(pay_type)

            for row in all_text.split('\n'): 
            #Printing invoice number
                if row.startswith('Invoice #') and row[-1].isnumeric() and (inv_num is None):
                    #we only need the first instance
                    Inv  = row.split()[-1]
                    inv_num = Inv
                    # print("invoice no: ", Inv)
                    
            # #invoice date
                if row.startswith('Invoice Date') and (inv_date is None):
                    #we only need the first instance
                    date = row.split()[-1]
                    inv_date = date
                    # print("inv date: ", inv_date)
                
            #Travel date
                if "Check Out" in row:
                    Rdate = row.split()[-2]
                    travel_date = Rdate
                    # print("travel date: " , travel_date)
                
            # #Reservation number
                if row.startswith('Reservation #') and (reservation_no is None):
                    Rno = row.split()[2]
                    reservation_no = Rno
                    # print("reservation number: ", reservation_no)
            # #passanger name

                if "Attn:" in row:
                    passanger_name= row.split("Attn:")[1]
                    # print("rented by: ", passanger_name)

            # # Gross amount 
                if "Gross Invoice Total:" in row:
                    gross_amt = row.split()[-1]
                    # print("gross amt: " , gross_amt)

            # Vat %
                if row.startswith('VAT Rate%'):
                    vat = row.split()[-1]
                    # print("vat: ", vat)


            # comm
                if row.startswith('Total Comission & VAT(GBP)'):
                    commission = row.split()[-1]
                    # print("commission: ",commission)
                    
            # nett amount
                if row.startswith('Balance Due(GBP)') and (Nett_amt  is None):
                    nett = row.split()[2]
                    Nett_amt = nett
                    # print("nett amt: " , Nett_amt)

            # destination
                if row.startswith('Location:') and (destination is None):
                    dest = row.split("Location:")[1]
                    destination = dest
                    # print("destination: " , destination)

        if "hertz" in all_text:

            #agency account number 
            account_no = 269994521
            # print(account_no)
            # #car provider
            car_provider = "ZE C"
            # print(car_provider)
            # # currency
            Currency = "GBP"
            # print(Currency)
            # # payment type 
            pay_type  = "Agency"
            # print(pay_type)

            
            #setting variables for writing
            # inv_num = None
            # inv_date = None
            # travel_date = None
            # reservation_no = None
            # balance_due = None
            # gross_amt = None
            # vat = None
            # location = None

            for row in all_text.split('\n'): 
            #Printing invoice number

                if "Invoice No:" in row and (inv_num is None):
                    #we only need the first instance
                    Inv  = row.split()[-1]
                    inv_num = Inv
                    # print("invoice no: ", Inv)
                    
            # #invoice date
                if row.startswith('Invoice Date:') and (inv_date is None):
                    #we only need the first instance
                    date = row.split()[-1]
                    inv_date = date
                    # print("inv date: ", inv_date)
                
            #Travel date
                if "Rented On:" in row:
                    Rdate = row.split()[-2]
                    travel_date = Rdate
                    # print("travel date: " , travel_date)
                
            # Reservation number
                if row.startswith('Reservation ID:') and (reservation_no is None):
                    Rno = row.split()[2]
                    reservation_no = Rno
                    # print("reservation number: ", reservation_no)
            # #passanger name

                if row.startswith("Renter:"):
                    passanger_name= row.split("Renter:")[1]
                    # print("rented by: ", passanger_name)

            # # Gross amount 
                if row.endswith("GBP") and (gross_amt is None):
                    gross_amt = row.split()[-2]
                    # print("gross amt: " , gross_amt)

            # Vat %
                if 'A @' in row:
                    if row.startswith('A @') and (vat is None):
                        vat = row.split(' ')[2]
                        # print("vat: ", vat)
                elif vat is None: 
                    vat = "0.00%"
                    # print("vat: ", vat)
                
            # comm
                if "COMMISSION" in row:
                    commission= row.split()[-2]
                    # print("commission: ",commission)
                    
            # nett amount
                if 'Please Pay:' in row and row.endswith('GBP'):
                    Nett_amt = row.split()[-2]
                    # print("nett amt: " ,Nett_amt )
            
            # destination
                if row.startswith('Frequent Traveler: ') :
                    destination = " ".join(row.split()[3:])
                    # destination = row[23:]
                    # print("destination: " , destination)
                elif 'Frequent Traveler' not in all_text and row.startswith('IATA/TACO: '):
                    destination = row[20:]
                    # print("destination:", destination)

        if "EUROPCAR" in all_text:

            #agency account number 
            account_no = 269994521
            # print(account_no)
            #car provider
            car_provider = "NULL"
            # print(car_provider)
            #currency
            Currency = "GBP"
            # print(Currency)
            #payment type 
            pay_type = "Agency"
            # print(pay_type)
            passanger_name = "NULL"
            # print(passanger_name)

            for row in all_text.split('\n'): 
            #Printing invoice number
                if row.startswith('Invoice') and (inv_num is None):
                    #we only need the first instance
                    Inv  = row.split()[-1]
                    inv_num = Inv
                    # print("invoice no: ", Inv)
                    
            #invoice date
                if row.startswith('Invoice date') and (inv_date is None):
                    #we only need the first instance
                    date = row.split()[-1]
                    inv_date = date
                    # print("inv date: ", inv_date)
                
            #Travel date
                if "Check-out" in row:
                    Rdate = row.split()[-4]
                    travel_date = Rdate
                    # print("travel date: " , travel_date[:-5])

            #Reservation number
                if row.startswith('Reservation No'):
                    reservation_no = row.split()[-1]
                    # print("reservation number: ", reservation_no)


            # #passanger name

            #     if "Attn:" in row:
            #         passanger_name= row.split("Attn:")[1]
            #         # print("rented by: ", passanger_name)

            # # Gross amount 
                if row.startswith("Total Charges:"):
                    gross_amt = row.split()[-2]
                    # print("gross amt: " , gross_amt)

            # Vat %
                if "Commission VAT" in row:
                    vat = row.split()[-2]
                    # print("vat: ", vat)


            # comm
                if "Total Commission" in row:
                    comm = row.split('Total Commission')[1].split('Exchange')[0]
                    commission = str(comm)[:-4]
                    # print("commission: ",commission) 
                    
            # nett amount
                if row.startswith('Invoice Total'):
                    Nett_amt = row.split()[2]
                    # print("nett amt: " , Nett_amt)

            # destination
                if row.startswith('Check-out Station'):
                    dest = row.split("Check-out Station")[1].split("Days")[0]
                    destination = ""
                    for i in dest.split():
                        if i.isalpha():
                            destination = " ".join([destination ,i]).strip()
                    # destination = dest
                    # print("destination: " , destination)
    
        if inv_num is None:
            #TODO: print this in frontend (or display a message saying inconsistent files not deleted)
            print("No invoice number found")
            print("Please check the file")
            print(file)
            print("and try again")
        
        else:
            #Writing to excel
            #Creating a dataframe to write data to excel file
            data = [[account_no, car_provider, inv_num, inv_date, travel_date, reservation_no, passanger_name, gross_amt, vat, commission,Nett_amt, Currency, pay_type,destination ]]
            df = pd.DataFrame(data, columns=['account_no', 'car_provider', 'inv_num', 'inv_date', 'travel_date', 'reservation_no', 'passanger_name', 'gross_amt', 'vat', 'commission','Nett_amt', 'Currency', 'pay_type','destination'])

            # appending the data of df after the data of demo1.xlsx

            if os.path.exists(output_folder + "/Report3.xlsx"):
                # print('Updating excel file...')
                with pd.ExcelWriter(output_folder + "/Report3.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                    df.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
                os.remove(path=file_path)
            else:
                # print('\nCreating Report.xlsx for saving all the performance data\n')
                df.to_excel(output_folder + "/Report3.xlsx",index=False)
                os.remove(path=file_path)

    # print("Done")