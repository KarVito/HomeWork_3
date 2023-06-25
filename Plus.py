# Turn Str object in to datetime.datetime object in "birthday" 

from datetime import datetime

def get_birthdays_per_week(users):
    
    users_BD = []
    for i in users:
        BD = datetime.strptime(i["birthday"], '%Y-%m-%d')
        i["birthday"] = BD
        users_BD.append(i)
    print(users_BD)
    return users_BD

get_birthdays_per_week([{'name': 'Helga', 'birthday': '2000-07-07'}, {'name': 'Igor', 'birthday': '1981-10-10'}, {'name': 'Simon', 'birthday': '1992-03-30'}])
