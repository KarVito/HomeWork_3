from datetime import datetime


def get_birthdays_per_week(users):
    
    users_next_week = []
    users_after_next_week = []
    today = datetime.now()
    Start_next_week= 4-today.weekday()
    
    Monday_list = "Monday: "
    Tuesday_list = "Tuesday: "
    Wednesday_list = "Wednesday: "
    Thursday_list = "Thursday: "
    Friday_list = "Friday: "
    
    for i in users:
        birthday_in_this_year = datetime(today.year, i["birthday"].month, i["birthday"].day, 0, 0)
             
        if (birthday_in_this_year-today).days >= Start_next_week and (birthday_in_this_year-today).days <= Start_next_week+6:
            users_next_week.append(i)
    #omega = len(users_next_week)
    #print(f'Birthbay week: From {(users_next_week[0])["birthday"].day}_{(users_next_week[0])["birthday"].month} Till {(users_next_week[omega-1])["birthday"].day}_{(users_next_week[omega-1])["birthday"].month} ')
    print("<<< NEXT WEEK Birthday list >>>")

    for i in users_next_week:
        birthday_in_this_year = datetime(today.year, i["birthday"].month, i["birthday"].day, 0, 0)

        if birthday_in_this_year.weekday() == 0 or birthday_in_this_year.weekday() == 5 or birthday_in_this_year.weekday() == 6:
            Monday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 1:
            Tuesday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 2:
            Wednesday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 3:
            Thursday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 4:
            Friday_list += i['name']+", "             
    
    print(Monday_list.removesuffix(", "))
    print(Tuesday_list.removesuffix(", "))     
    print(Wednesday_list.removesuffix(", "))
    print(Thursday_list.removesuffix(", "))
    print(Friday_list.removesuffix(", "))        
    

    Monday_list = "Monday: "
    Tuesday_list = "Tuesday: "
    Wednesday_list = "Wednesday: "
    Thursday_list = "Thursday: "
    Friday_list = "Friday: "
    
    for i in users:
        birthday_in_this_year = datetime(today.year, i["birthday"].month, i["birthday"].day, 0, 0)
             
        if (birthday_in_this_year-today).days >= Start_next_week+7 and (birthday_in_this_year-today).days <= Start_next_week+13:
            users_after_next_week.append(i)
    #omega = len(users_next_week)
    #print(f'Birthbay week: From {(users_next_week[0])["birthday"].day}_{(users_next_week[0])["birthday"].month} Till {(users_next_week[omega-1])["birthday"].day}_{(users_next_week[omega-1])["birthday"].month} ')
    print("<<< AFTER NEXT WEEK Birthday list >>>")

    for i in users_after_next_week:
        birthday_in_this_year = datetime(today.year, i["birthday"].month, i["birthday"].day, 0, 0)

        if birthday_in_this_year.weekday() == 0 or birthday_in_this_year.weekday() == 5 or birthday_in_this_year.weekday() == 6:
            Monday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 1:
            Tuesday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 2:
            Wednesday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 3:
            Thursday_list += i['name']+", "
        elif birthday_in_this_year.weekday() == 4:
            Friday_list += i['name']+", "             
    
    print(Monday_list.removesuffix(", "))
    print(Tuesday_list.removesuffix(", "))     
    print(Wednesday_list.removesuffix(", "))
    print(Thursday_list.removesuffix(", "))
    print(Friday_list.removesuffix(", "))            
        
                
get_birthdays_per_week([{'name': 'Iren', 'birthday': datetime(2010, 6, 23, 0, 0)},
                        {'name': 'Nadia', 'birthday': datetime(2002, 6, 24, 0, 0)},
                        {'name': 'Vadim', 'birthday': datetime(1878, 6, 25, 0, 0)},
                        {'name': 'Helga', 'birthday': datetime(2000, 6, 26, 0, 0)}, 
                        {'name': 'Igor', 'birthday': datetime(1981, 6, 27, 0, 0)}, 
                        {'name': 'Simon', 'birthday': datetime(1992, 6, 28, 0, 0)},
                        {'name': 'Mell', 'birthday': datetime(1984, 6, 29, 0, 0)}, 
                        {'name': 'Anna', 'birthday': datetime(1996, 6, 30, 0, 0)},
                        {'name': 'Ivan', 'birthday': datetime(1999, 7, 1, 0, 0)}, 
                        {'name': 'Sam', 'birthday': datetime(1977, 7, 2, 0, 0)},
                        {'name': 'Samantha', 'birthday': datetime(1960, 7, 3, 0, 0)},
                        {'name': 'Elza', 'birthday': datetime(1979, 7, 4, 0, 0)},
                        {'name': 'Alex', 'birthday': datetime(1988, 7, 5, 0, 0)},
                        {'name': 'Dan', 'birthday': datetime(2002, 7, 6, 0, 0)},
                        {'name': 'Gregor', 'birthday': datetime(2012, 7, 7, 0, 0)},
                        {'name': 'Mickle', 'birthday': datetime(2001, 7, 8, 0, 0)},
                        {'name': 'Laura', 'birthday': datetime(1998, 7, 9, 0, 0)},
                        {'name': 'Jane', 'birthday': datetime(1995, 7, 10, 0, 0)},
                        {'name': 'Tatiana', 'birthday': datetime(1957, 7, 11, 0, 0)}]
                        )