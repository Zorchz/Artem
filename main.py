# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from requests import get, status_codes

r = get("https://google.com")
print(r.status_code)
