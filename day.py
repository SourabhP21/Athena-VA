import datetime

def executeDay():
    day = datetime.datetime.today().weekday()
    Day_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return day_of_the_week