# Python `requests` Module 

## Introduction

The `requests` module is one of the most popular Python libraries used for sending HTTP requests. It allows us to interact with websites, APIs, and web servers easily.

## Installation

pip install requests
```

## Importing the Module 

import requests

## Sending a GET Request

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)
```

## Sending a POST Request

```python
import requests

data = {
    "username": "rajat",
    "password": "1234"
}

response = requests.post(
    "https://example.com/login",
    data=data
)

print(response.status_code)
```

## Important Response Attributes

```python
response.status_code   # Status code of the request
response.text          # Response as string
response.content       # Response in bytes
response.headers       # Headers received
response.url           # Final URL
```

## Working with JSON Data

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

data = response.json()

print(data)
print(data["title"])
```

## Sending Query Parameters

```python
import requests

params = {
    "page": 1,
    "limit": 10
}

response = requests.get(
    "https://example.com/api",
    params=params
)

print(response.url)
```

## Sending Custom Headers

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    "https://example.com",
    headers=headers
)

print(response.status_code)
```

## Handling Exceptions

```python
import requests

try:
    response = requests.get(
        "https://example.com",
        timeout=5
    )

    response.raise_for_status()

    print(response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
```

## Common HTTP Methods

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Retrieve data         |
| POST   | Send new data         |
| PUT    | Update existing data  |
| PATCH  | Partially update data |
| DELETE | Delete data           |

## Useful Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

## Why Use `requests`?

* Simple and beginner-friendly syntax.
* Works with APIs and websites.
* Supports GET, POST, PUT, PATCH, and DELETE requests.
* Easily handles JSON data.
* Supports headers, cookies, and authentication.
* Provides exception handling.

## Summary

The `requests` library makes HTTP requests easy in Python. It is widely used for API development, web scraping, automation, and backend applications.
