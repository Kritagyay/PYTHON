# with open("my_text.txt", mode='w') as file:
#     file.write("HEllo this is me ")


with open ("/Users/hp/Desktop/my_text.txt",mode='w') as file:
    file.write("HI everyone")

with open("/Users/hp/Desktop/my_text.txt") as file:
    content=file.read()
    print(content)

