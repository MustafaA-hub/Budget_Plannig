from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

Primary_catogories = {
    "Utilities": [
        "Enbridge", "Bell Canada", "Opos Fido Macc 888-4"
    ],
    "Credit Card": [
        "Mb-Credit Card/Loc Pay."
    ],
    "Miscellaneous": [
        "Free Interac E-Transfer", "Ice Currency - Ticketi Missi", "Cppf Missi", 
        "Fpos Rcss #567 Winds", "Fpos Usat_wt133957 Missi", "Fpos Usat_wt133957",
        "Opos 1.00 Pyn*Lofree Onlin", "Coinamatic-1400 Ouelle Winds", 
        "Opos Immigration Canada Oottaw", "Opos Change.Org +1415", 
        "Opos Hdfund.Org +1248", "Interac E-Transfer Rtn", "Monthly Fees", 
        "Mto Drivetest D41 Winds"
    ],
    "Income": [
        "Lancesoft Canada", "Lancesoft Canad"
    ],
    "Gym": [
        "Movati Athletic Windsor", "Movati - Windsor Winds"
    ],
    "Groceries": [
        "Fpos Nizam Produce Winds", "Fpos Costco Wholesale W53winds", 
        "Fpos Walmart Store #3115 Winds", "Fpos Zehrs #529 Parkway Winds", 
        "Walmart Store #3115 Winds", "Freshco #9728 Winds", 
        "Metro 139 Winds", "Dollarama #542 Winds", "Dollarama #0300 Winds", 
        "Metro 147 Winds", "Rcss Dougai #2827 Winds", "Shoppers Drug Mart #11 Winds", 
        "Dollarama #1198 Winds", "Metro 136 Winds", "Staples #30 Winds", 
        "Dollarama #276 Winds", "Oriental Market Winds", "Dollarama #441 Winds", 
        "Amazing Bins Winds", "Real Canadian Superstore"
    ],
    "Rent": [
        "Lrl Rent"
    ],
    "Car Expense": [
        "Fpos 1st Auto Service Incwinds", "Shell C21954", "Esso Circle K Grave", 
        "Esso Windsor #2", "Pioneer Stn #89", "Ultramar #43202", 
        "Petro Canada009", "Petro Canada650", "Petro Canada487", 
        "Bear Creek", "Bear Creek Expr", "Shell C02964"
    ],
    "Home Decore": [
        "Opos 1004.00 Kickstarter.+1347", "Ikea North York North", 
        "Homesense 058 Winds", "Winners 261 Winds", "Goodwill Industries, W Winds"
    ],
    "Restraunt": [
        "Fpos Tim Hortons #1790 Winds", "Fpos Popeyes #14326 Winds", 
        "Napoli 2 For 1 Pizza & Winds", "Hakimo Donair & Sub Winds", 
        "Aloony Shawarma Inc. Winds", "Marigold Unique Flavou Hunts", 
        "Tea Station Bubble Tea Winds", "Eastside Shawarma Winds"
    ],
    "Entertainment": [
        "Cineplex #7257 Qps Winds", "Opos Playstationnetwork 877-9", 
        "Opos Fh* Grand Bend Parasgrand", "Niagara Speedway Go Kartsniaga"
    ],
    "Travel": [
        "Opos Toronto Parking Authtoron", "Presto Dundas S", 
        "Opos Via Rail Montr", "Hk Travel Centres L.P. Dutto"
    ],
    "Medical": [
        "Rose City Dental Wi"
    ],
    "Clothing": [
        "Opos Shein.Com Toron", "598 - Sephora Winds", 
        "Old Navy Ca 841 Winds", "Urban Planet #1533 Winds"
    ],
    "Donation": [
        "Opos Madinah Donation +1833", "Opos Penny Appeal Canada +1855"
    ],
    "None":[""]
}

Primary_catogories2 = {
    "Utilities": [
        "Enbridge", "Bell Canada", "Fido"
    ],
    "Credit Card": [
        "Mb-Credit Card/Loc Pay."
    ],
    "Miscellaneous": [
        "Interac E-Transfer", "Ice Currency", "Cppf", "Fpos Usat_wt133957 Missi", 
        "Fpos Usat_wt133957", "Opos Immigration Canada Oottaw", "Opos Change.Org +1415", 
        "Monthly Fees", "Drivetest", "Mecp-Westgate-Algonqui   Whitn", "Ptc Adil" , 
        "Henrietta'S Huntsville   Hunts", "Opos Tgtg Bet8e0kx7tr81  Vanco", 
        "Opos Fh* Splash Waterspor+1855 ", "Sq *Waterfront Ice Cre", "Singlekey", 
        "Opos Town Of Milton - Parmilto", "Save Tax Solutions","Change.Org", "Hdfund.Org", 
        "Siam Centre-Vil", "Couche-Tard", "Drogheria Fine", "Boulangerie Des Copain",
        "O Mont -Creperie Inc.", "Iccm Milton", "Remitly", "Toniagara* R4xmuhe" 
    ],
    "Income": [
        "Lancesoft"
    ],
    "Personal development": [
        "Movati", "Udemy"
    ],
    "Groceries": [
        "Nizam Produce", "Costco", "Walmart", "Zehrs", "Freshco", "Food Basics",
        "namaste indian", "Metro", "Rcss", "Shoppers Drug Mart", "Grocers", "Farm", 
        "7-Eleven", "bread","Oriental Market", "Amazing Bins", "Real Canadian Superstore", 
        "Food Market", 'Asian Food Imports',"Marigold Unique", "Pharmacy", "Convenience",
        "Grocery", "Groceries", "Grocer" "Supermarket", "Superstore", "Market", "Mart", 
        "Drug Mart", "Drugstore", "Drug Store", "Drug", "Pharmacy","Store", "Shop"
    ],
    "Rent": [
        "Lrl Rent"
    ],
    "Car Expense": [
        "1st Auto Service", "Shell", "Esso","Pioneer ", "Ultramar", 
        "Petro", "Bear Creek", "Gas", "Fuel", "Fuels", "Cumberland", 
        "Onroute", "Gasoline", "Gas Station"
    ],
    "House Hold Items": [
        "Opos 1004.00 Kickstarter.+1347", "Ikea", "Amzn", "Amazon", "Staples",
        "Homesense", "Winners", "Goodwill", "Think Kitchen", "Lofree",
        "Dollarama", "Dollar", "Home Depot", "Marshalls", 'Giant Tiger', "Hardware"
        ],
    "Restraunt": [
        "Tim Hortons", "Popeyes", "Pizza", "Pizzeria", "Donair", 'Restaurant',
        "Shawarma", "Marigold Unique Flavou Hunts", "Tea Station", "Grill", 
        "Little Ceasers", "Fork & Knife", "Starbucks","Mcdonald", "Dairy Queen", 
        "Royal Paan", "Bakery", "Cafe", "Caffe", "Sushi", "Subway","Cinnabon", 
        "Dennys", "Dinner", "Ice Cream","Bubble Teas", "Uncle Tetsu", "Ramen",
        "Burger", "Pita", "Bites", "Punjabi", "Biryani", "KFC", "Taco", "Pasta", 
        "Wings", "Culture Crust","Mr. Puffs", "Baskin Robbins", "Krispy Kreme", 
        "Doughnuts", "Poutine", "Brewery", "Bar", "Pub","Indiawalleh", "Chocolate",
        "Chocolates", "Dessert", "Rangeela Paan", "Sweet Heat", 'Chatime',"Cuisine", 
        "Kitchen", "Dhesi Swaad", "Hakka", "Gona Cha", "Sumaq", "Karhai", "Kufiya House", 
        "Italian", "tea","Osmows", "Taka Japanese & Thai", "bbq"
    ],
    "Entertainment": [
        "Cineplex", "Playstationnetwork", "Splash", "Playstationnetwork",
        "Niagara Speedway Go Kartsniaga", "Watersports" 
    ],
    "Travel": [
        "Parking", "Presto", "Airbnb",
        "Via Rail", "Travel", "Airlines"
    ],
    "Medical": [
        "Rose City Dental"
    ],
    "Clothing": [
        "Shein.Com", "Sephora", "Coinamatic",
        "Old Navy", "Urban Planet", "Cleaners", "Laundry", "Laundromat"
    ],
    "Donation": [
        "Madinah Donation", "Penny Appeal Canada", "Islamic Relief",
        "Charity", "Donation", "Relief"
    ],
    "Not Specified":[
        "None"
        ]
}

class Categories:
    def __init__(self, table):
        
        # Get the transaction descriptions from the table
        transaction_descriptions = []
        for row in range(table.rowCount()):
            item = table.item(row, 2)
            transaction_descriptions.append(item.text())
            transaction_descriptions = [s.strip() for s in transaction_descriptions]
    
        # Determine category based on transaction description
        for index, description in enumerate(transaction_descriptions):
            repeat = 0
            for category, subcategories in Primary_catogories2.items():
                for sub in subcategories:
                    if sub.lower() in description.lower():
                        table.setItem(index, 0, QTableWidgetItem(str(category)))
                        repeat += 1
                        break
            #if repeat >= 2: print(description + " :" + str(repeat))

        # Check to see if any category row is left empty
        for row in range(table.rowCount()):
                item = table.item(row, 0)
                if item is None or item == "None" or not item.text().strip():
                    #print("Uncetgorized Items: " + table.item(row,2).text())
                    table.setItem(row, 0, QTableWidgetItem(str("Un-Categorized")))
