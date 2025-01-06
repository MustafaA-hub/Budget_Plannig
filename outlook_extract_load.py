
import win32com.client
import pandas as pd #To capture data into a DataFrame

#Define the outlook object 
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#Print Outlook Folders
for folder in outlook.Folders:
     print("Folder Name:" + folder.Name)

#Define the folder you want to search (inbox default is 6)
inbox = outlook.GetDefaultFolder(6).Folders.Item("Testbed Alarms") 

#Fetch messages from the above defined folder                                    
messages = inbox.Items
print(messages)
print("Sub Folder Name in Inbox: " + str(inbox))

#Let us create empty lists to capture the data iteratively
#NOTE that there are many ways to doing the following task.
all_names=[]
all_time = []
all_error_message = []

#Iteratively go through our messages to extract desired information
#Here, I am looking for emails with subject "From Sreeni"
for i, message in enumerate(messages):
    
    if message.Subject == "First Alarm" and str(message.ReceivedTime)[:10] == "2025-01-01":     #Fetch all emails with this subject
        #print(message.SenderName)
        #date_time = message.LastModificationTime  #Extract the date & time the email was received
        print(str(message.ReceivedTime))
        
        text = message.Body  #Read the body of our email. 
        
        #Now extract the information we need from the message body
        ##Find the text "Name:" and read until it sees text "Company"
        #Repeat the same for other details
    
        name = text[text.rfind('<Testbed>')+9:text.find("\n", text.rfind('<Testbed>')+9)]
        time = text[text.rfind('<Time>')+6:text.find("\n", text.rfind('<Time>')+6)]
        error_message = text[text.rfind('<Message>')+9:]

        print('Testbed: '     + name) 
        print('Time: '        + time)
        print('Error Message: ' + error_message)
        print(' ')

        
        #Append identified text into our empty lists for each task. 
        all_names.append(name)
        all_time.append(time)
        all_error_message.append(error_message)
        

#Capture all information into pandas dataframe
extracted_info = pd.DataFrame(columns=["Name", "Time", "Error Message"])

extracted_info["Name"] = all_names
extracted_info["Time"] = all_time
extracted_info["Error Message"] = all_error_message

#Save the dataframe as an excel document. 
#extracted_info.to_excel("extracted_info.xlsx")