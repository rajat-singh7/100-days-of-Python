# MULTI-PROCESSING
# For Mac
# import multiprocessing
# import requests

# def DownloadFile(url,name):
#     print(f"Started downloading {name}")
#     r = requests.get(url)
#     open(f"Random/{name}.jpg",'wb').write(r.content)
#     print(f"Finished downloading {name}")

# url = "https://picsum.photos/200/300"
# pros = []
# for i in range(25):
#     # DownloadFile(url,i)
#     p = multiprocessing.Process(target=DownloadFile,args=[url,i])
#     p.start()#
#     pros.append(p)

# for p in pros:
#     p.join()


# For Windows

import multiprocessing
import requests
import os

def DownloadFile(url,name):
    print(f"Started downloading {name}")
    r = requests.get(url)
    os.makedirs("Random",exist_ok=True)
    open(f"Random/{name}.jpg",'wb').write(r.content)
    print(f"Finished downloading {name}")

if __name__== "__main__":
    url = "https://picsum.photos/200/300"
    pros = []
    for i in range(25):
        # DownloadFile(url,i)
        p = multiprocessing.Process(target=DownloadFile,args=[url,i])
        p.start()#
        pros.append(p)

    for p in pros:
        p.join()
# Async I/O
import asyncio
async def greet():
   print("Hello!")
   await asyncio.sleep(2) # Simulates a non-blocking delay
   print("Welcome to Async Python!")
# Running the async function
asyncio.run(greet())

# HERE I END MY 100 DAYS OF PYTHON PLAYLIST