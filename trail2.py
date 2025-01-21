
person = {"name": "henry", "age": 12}

class printer:
    def __init__(self):
        #print("Hello " + person["name"] + " " + str(person["age"]))
        keys = [key for key, value in person.items() if value == "henry"]
        print(keys)
