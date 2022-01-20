#Escape Sequences

print("I am 6'2\" tall") # escape double-quote inside string
#Expected output: I am 6'2" tall
print('I am 6\'2" tall') # escape single-quote inside string
# Expected output: I am 6'2" tall

tabby_cat = "\tI'm tabbed in" # \t tabs the output in.
persian_cat = "I'm split\non a line" # \n splits the line or starts a new line
backslash_cat = "I'm \\ a \\ cat" # Just a backsplash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)