
file = open("students.txt", "w")

file.write("Siva\n")

file.write("Vardha\n")

file.write("Vishnu\n")

#Read

file = open("students.txt", "r")
file.readline()


#append
file = open("students.txt", "a")

file.write("Meena\n")

file.close()


file = open("students.txt", "r")
print(file.read())


#context manager
with open("students.txt", "w") as file:
    file.write("Siva\n")
    file.write("Vardha\n")
    file.write("Vishnu\n")
    file.write("Meena\n")


file = open("students.txt", "r")
print(file.read())