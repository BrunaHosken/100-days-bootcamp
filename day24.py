with open("./files/txt/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("./files/txt/my_file.txt", mode="a") as file:
    file.write("New text.")

with open("./files/txt/my_file_test.txt", mode="w") as file:
    file.write("New text test.")

