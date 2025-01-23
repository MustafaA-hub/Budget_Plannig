
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
    ]
}

class Categories:
    def __init__(self, table):

        """
        for category, subcategories in Primary_catogories.items():
            if "Opos Madinah Donation +1833" in subcategories:
                print(category)
        """

        transaction_descriptions = []
        for row in range(table.rowCount()):
            item = table.item(row, 3)
            transaction_descriptions.append(item.text())
        transaction_descriptions = transaction_descriptions[:3]
        print(transaction_descriptions)

        for description in transaction_descriptions:
            for category, subcategories in Primary_catogories.items():
                if description in subcategories:
                    print(category + ": " + description)

