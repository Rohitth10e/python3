# file = open("order.txt","w")
# try:
#     file.write("one masala chai please")
# except Exception as e:
#     print(e)
# finally:
#     print("write compelete")
#     file.close()

with open("order.txt", "w") as file:
    file.write("one ginger tea please")