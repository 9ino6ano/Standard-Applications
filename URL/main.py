import pyshorteners

url=input("Enter your link: ")
s=pyshorteners.Shortener()
print(s.tinyurl.short(url))
