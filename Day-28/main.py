# Function Caching
# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5

# print(fx(20))
# print("Done For 20")
# print(fx(2))
# print("Done For 2")
# print(fx(5))
# print("Done For 5")
# print(fx(6))
# print("Done For 6")


# print(fx(20))
# print("Done For 20")
# print(fx(2))
# print("Done For 2")
# print(fx(5))
# print("Done For 5")
# print(fx(61))  # THIS TAKES TIME
# print("Done For 61")

# # EXAMPLE NO.02
# from functools import lru_cache
# @lru_cache(maxsize=5)
# def fib(n):
#    print(f"Calculating fib({n})")
#    if n < 2:
#        return n
#    return fib(n-1) + fib(n-2)
# print(fib(10)) # First call computes values
# print(fib(10)) # Second call retrieves from cache
# print(fib.cache_info()) # Shows hits, misses, size

# NEWS API
# import requests
# import json

# query = input("What type of news are you interested?")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-14&sortBy=publishedAt&apiKey=8133faf5ef4f4842832d08b3aec36c9f"
# r = requests.get(url)
# news = json.loads(r.text)
# # print(news,type(news))
# for article in news["articles"]:
#     print(article["title"])
#     print(article["description"])
# Water Reminder Program
# This program sends a desktop notification every 1 hours.


import time
from plyer import notification


interval = 3600

while True:
    notification.notify(
        title="💧 Water Reminder",
        message="Time to drink some water and stay hydrated!",
        app_name="Water Reminder",
        timeout=10
    )

    print("Reminder sent: Drink water!")
    time.sleep(interval)


