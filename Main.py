import datetime

to_day = datetime.datetime.now().strftime("Date: %Y-%m-%d Time: %I:%M %p")

Journal_Entry = input("What are you feeling today?")

print(to_day,'\n  \n', Journal_Entry)
