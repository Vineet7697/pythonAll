# f=open('file.txt','a+')
# # f.write('''this is
# #         from file
# #         handling ''')
# f.writelines(['this\n','is\n','python\n'])
# f.close()
# # print(f.name)
# # print(f.mode)
# # print(f.readable())
# # print(f.writable())
# # print(f.closed)
# # print(f.encoding)

# f=open('file.txt','r')
# # data=f.read(10)
# # data=f.readline()
# data=f.readlines()
# print(data)
# f.close()


# f=open('file.txt','r')
# print(f.tell())
# f.close()

# f=open('file.txt','a')
# print(f.tell())
# f.close()

# f=open('file.txt','a')
# print(f.tell())
# data=f.read()
# print(data)
# f.close()

# f=open('file.txt','r')
# print(f.tell())
# data=f.read()
# print(data)
# f.close()

# f=open('f1.txt','x')
# print(f.tell())


# f=open('file.txt','w')
# data=f.read()
# print(data)


# f=open('file.txt','w')
# data=f.readline()
# print(data)
# f.close()


# f=open('file.txt','r')
# print(f.tell())
# data=f.read(5)
# print(data)
# print(f.tell())
# data=f.read(10)
# print(data)
# print(f.tell())



f=open('file.txt','rb')
print(f.tell())
f.seek(5)
print(f.tell())
f.seek(-5,1)
print(f.tell())









