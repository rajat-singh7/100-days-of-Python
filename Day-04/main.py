#Basic time greeting app mini-project:
time = int(input("Enter hour in 24 hour format, ex-0-23:"))
if(time >= 4 and time < 12):
    print("Good Morning 🌄")
elif(time >= 12 and time < 17):
    print("Good Afternoon 🌅")
elif(time >= 17 and time < 20):
    print("Good evening 🌆")
else:
    print("good night 🌃")
#Level up
import datetime
now = datetime.datetime.now()
hour = now.hour
exact_time = now.strftime("%I:%M:%S %p") 
current_day = now.strftime("%A")
current_date = now.strftime("%D %B %Y")
name = input("Enter your name:")
if(hour >= 4 and hour < 12):
    greeting = "Good morning!🌄"
    message = "New Day,New opportunities to conquer."
elif(hour >= 12 and hour < 17):
    greeting = "Good Afternoon!🌅"
    message = "Half day is over, It's time to do something crazy."
elif(hour >= 17 and hour < 20):
    greeting = "Good Evening!🌆"
    message = "Take a cup of tea."
else:
    greeting = "Good night!🌃"
    message = "Have sweet dreams."
if current_day in ["Saturday","Sunday"]:
    day_msg = "It's weekend bro, Go have some fun."
else:
    day_msg = f"Today is {current_day} go on work"
print("\n" + "-"*30)
print("Hello",greeting,name)
print("Message:",message)
print("Time:",exact_time)
print("Date:",current_date)
print(day_msg)
print("-"*30) 