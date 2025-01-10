
import win32com.client
import pandas as pd #To capture data into a DataFrame
from datetime import datetime

#Define the outlook object 
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#Define the folder to want to search (inbox default is 6)
inbox = outlook.GetDefaultFolder(6).Folders.Item("Banking") 

#Fetch messages from the above defined folder                                    
messages = inbox.Items

#Empty lists to capture the data iteratively
transaction_description=[]
transaction_amount = []
message_date = []

# Define the date to filter emails
filter_date  = datetime.strptime("2025-01-08 00:00:00", "%Y-%m-%d %H:%M:%S")

#Iteratively go through our messages to extract desired information
for i, message in enumerate(messages):
    
    date_time = datetime.strptime(str(message.LastModificationTime)[:19], "%Y-%m-%d %H:%M:%S")  #Extract the date & time the email was received

    if message.Subject == "Last five transactions for your Day-to-Day accounts"and date_time > filter_date:     #Fetch all emails with this subject and date

        # Now extract the information we need from the message body  
        text = message.Body  # Read the body of our email. 
        lines = text.split('\n')  # Split the body into lines
        transactions = lines[7:13] # Extract the lines that contain the 5 transactions
        transactions = [item.replace("\r", "") for item in transactions] # Remove the '\r' character from the list of strings
        transactions = [item.replace("$", "") for item in transactions] # Remove the '$' character from the list of strings
        transactions = [(item.rsplit(' ', 1)[0], float(item.rsplit(' ', 1)[1].replace(',', ''))) for item in transactions if item] # seperate the transaction description and amountdolar amount and transaction description
        print(transactions)
        
        #Iteratively append the transaction description and amount into our empty lists
        for item in transactions:
            transaction_description.append(item[0])
            transaction_amount.append(item[1])
            message_date.append(date_time)

print(message_date)
#Capture all information into pandas dataframe
extracted_info = pd.DataFrame(columns=["Date", "Category", "Expense"])
extracted_info["Date"] = message_date
extracted_info["Category"] = transaction_description
extracted_info["Expense"] = transaction_amount

# Save the dataframe as an excel document.
file_path = "C:/Users/jasle/OneDrive/Desktop/Financial Planning/Budget.xlsx"

# Load the existing workbook into a DataFrame
existing_data = pd.read_excel(file_path, sheet_name='Daily Expense')
# Append the new data to the existing data
updated_data = pd.concat([existing_data, extracted_info], ignore_index=True)

# Write the updated DataFrame back to the Excel file
updated_data.to_excel(file_path, sheet_name='Daily Expense', index=False)
print("Data has been successfully extracted and loaded into the excel sheet")