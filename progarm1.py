try :
	a = open("sample.text","r")
except :
	print("file does not exist")
data = a.read()
print(data)