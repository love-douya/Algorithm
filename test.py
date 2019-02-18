# dhaifhiqhfeihf
# import calendar
# import time
# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# string = str("123")
# print("ada" , string)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
# cal = calendar.month(2018, 1)
# print("here is the calendar:")
# print(cal)

# #python字符串转换

# # bytes object 
# b = b"example"
 
# # str object 
# s = "example"
 
# # str to bytes 
# bytes(s, encoding = "utf8") 
 
# # bytes to str 
# str(b, encoding = "utf-8") 
 
# # an alternative method 
# # str to bytes 
# str.encode(s) 
 
# # bytes to str 
# bytes.decode(b)

# a = 5.0000
# print("%.3f" %a)

# li = [lambda x:x for x in range(10)]
# res = li[1](2)
# print(res)

# import functools

# def ip(li):
#     return functools.reduce(lambda x, y: x + y, li)

# print(li)


# li = [1, 2, 3]
# lp = li[0:3]
# print(lp)

a = [1,2,3,4]
print(a[-1:-3:-1])
