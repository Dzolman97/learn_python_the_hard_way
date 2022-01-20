from sys import argv #Importing from the terminal or shell

script, filename = argv #Args needed for the terminal or shell when you run the program

#Talk to the user to let them know what will happen.
print(f"We're going to erase {filename}")
print("If you don't wnat that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER or RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

#Truncate or Empty the file.
print("Truncating the file. \n...\n...\n...\nGoodbye!")
target.truncate()

# User writes new lines into the terminal
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these into the file.")

target.write(line1, "\n")
target.write(line2, "\n")
target.write(line3, "\n")

# Close the file
print("And finally, we close it.")
target.close()