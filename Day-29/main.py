# MULTI-THREADING---> Used to Petformn multiple tasks concurrently(multi-tasking) 
# Good for I/Obbound tasks like reading files or fetching data from APIs thrading.
# Thread(target=my_function)
import threading
import time
import requests

# def func(seconds):
#     print(f"Sleeping for {seconds} second")
#     time.sleep(seconds)

# time1 = time.perf_counter()
# NORMAL CODE
# func(4)
# func(2)
# func(1) 


# SAME CODE USING THREAD 
# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])
# t3 = threading.Thread(target=func,args=[1])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# CALCULATING TIME
# time2 = time.perf_counter()
# print(time2-time1)

# EXAMPLE NO.02
def walk_dog():
    time.sleep(6)
    print("You finishing walk the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_email():
    time.sleep(4)
    print("You get the email")

# Normal Code
# walk_dog()
# take_out_trash()
# get_email()

# Using thread
chore1 = threading.Thread(target=walk_dog)
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_email)
chore3.start()
# Firstly take out trash will finsh then get the email and last walking the dog finish

chore1.join()
chore2.join()
chore3.join()

# REAL WORLD USE

def download_file(url,filename):
    print(f"Downloading start {filename}")
    r = requests.get(url)
    open(f"img_{filename}.jpg",'wb').write(r.content)
    print("Done!")

url ="https://picsum.photos/200/300"
for file in range(10):
    d = threading.Thread(target=download_file,args=[url,file])
    d.start()




