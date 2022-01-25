import imp


import os

print(os.getcwd())

f = open("C:\Users\618-16\Desktop\Python_AI-main\sources\따라하며 배우는 파이썬과 데이터과학\CH8\hello.txt", 'r')
s = f.read()
print(s)
f.close()

#한글 경로 들어가면 안된다!!