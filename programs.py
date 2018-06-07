# for i in range(1,21):
#     print("i is now {} ".format(i))
# to calculate range

# for i in range(0,100,5):
#     print(i)
#print table from 1 to 15
#
# for i in range(1,16):
#     for j in range(1,16):
#         print("{1:1} times {0:2} is {2:4} ".format(i,j,i*j))
#     print("==================")

# list="a","b","c","d","e","spam","f","j"
# for item in list:
#     if item=="spam":
#         continue  #bypasses, stop processing for that particular loop
#     print("buy "+item)

# list="a","b","c","d","e","milk","f","j"
# nasty_item=''
#
# for item in list:
#     if item=="spam":
#         nasty_item=item
#         break
# else:
#      print("i'll have that item please ")
#
# if nasty_item=="spam":
#      print("something else")

# number='0,82423,4324234,234324,3432,4323432'
# cleanednumber=''
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleanednumber+=number[i]
#
# newnumber=int(cleanednumber)
# print("the number is {} ".format(newnumber))

# ipAddress=input("enter the IP address: ")
# segment=1
# segment_length=0
# for char in ipAddress:
#     if char=='.':
#         print("segment {} contains {} characters".format(segment,segment_length))
#         segment+=1
#         segment_length=0
#     else:
#         segment_length+=1
#
# if char!='.':
#     print("segment {} contains {} characters".format(segment,segment_length))
#
# exits="north", "south","northeast"
# chosenexit=''
# while chosenexit not in exits:
#     chosenexit=input("please choose a direction: ")
# print("you got out")

# even=[2,4,6,8]
# odd=[1,3,5,7,9]
# numbers=even +odd
# print(sorted(numbers))
# menu=[]
# menu.append(["eggs","spam","bacon"])
# menu.append(["egg","sausage","bacon")
# # menu.append(["egg","spam"])
#
# list_=["mon","tue","wed","thur","fri"]
# iteration_=iter(list_)
#
# for i in range(0,len(list_)):
#     next_item=next(iteration_)
#     print(next_item)
#
# odd=range(1,10000,2)
# print(odd)
# print(odd[985])

r=range(0,100)
print(r)
for i in r[::-2]:
    print(i)


