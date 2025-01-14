from splitwise import Splitwise

consumer_key = "mER6vH7KGZhKK9vL6Uem8UOxM2oKDDZtYLZI9Sns"
consumer_secret = "JPXpWssbQeJfaNUl1n6ZSyOxLwiQiXSF0DQhL6qM"
api_keycode = "37taOEkOEYzzVfWLBAZAZQ7SNvZUMJscL5fLvTYg"

s = Splitwise(consumer_key,consumer_secret,api_key=api_keycode)

current = s.getCurrentUser()
#print("User: " + current.getFirstName())

friends = s.getFriends()
friends_id = friends[0].getId()
#print("Friend: " + friends[0].getFirstName())

expenses = s.getExpenses(friend_id = friends_id)
#print("Latest Expense: " + expenses[0].getCost())

groups = s.getGroups()
#print("Group: " + groups[0].getName())




