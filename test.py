import calendar
import time


string = str("123")
print("ada" , string)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
cal = calendar.month(2018, 1)
print("here is the calendar:")
print(cal)

#python字符串转换

# bytes object 
b = b"example"
 
# str object 
s = "example"
 
# str to bytes 
bytes(s, encoding = "utf8") 
 
# bytes to str 
str(b, encoding = "utf-8") 
 
# an alternative method 
# str to bytes 
str.encode(s) 
 
# bytes to str 
bytes.decode(b)