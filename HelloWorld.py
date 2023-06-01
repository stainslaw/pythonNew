my_name = "omar hakim"
my_age = 19
sum = my_age * 2

print(sum)
print(my_name, my_age)

print("Hello, my name is " + my_name + "and my age is " + str(sum) + ".")

# -----

s1 = """lots and lots of
text surrounded by 
triple quotation marks"""

print(s1)

s2 = "lots and lots of " \
    "text surrounded by" \
    "triple quotation marks"
print(s2)

s3 = "Everyone can do testing, but only a tester can do good testing."
if "test" in s3:
    print("string is present")
else:
    print("string is not present")


s4 = "Everyone can do testing, but only a tester can do good testing."
if "blues" not in s4:
    print("\"test\" is not present")
else:
    print("\"test\" is present")

s5 = "Test it until you break it"
s6 = s5.count("t")
print(s5[5])
print(s6)

s7 = "it's not vitally important to get it right the first time"
print(s7[:9])
print(s7[9:])
print(s7[:-9])
print(s7[-9:])

s8 = "it's not vitally important to get it right the first time"
s9 = s8.split()
print(s9)

s10 = ["it's", 'not', 'vitally', 'important', 'to', 'get', 'it', 'right', 'the', 'first', 'time']
print(' '.join(s10))

s11 = "Don't split us apart!"
splitPhrase = s11.split("s", 1)
print(splitPhrase)
print(type(splitPhrase))

backTogether = "s".join(splitPhrase)
print(backTogether)

s12 = "Estio"
print(s12[3])

s13 = "Apprenticeship"
for i in s13:
    print(i)

s14 = "I love python"
print(len(s14))

s15 = "Drink plenty of water"
if "tea" in s15:
    print("Let's have a cup of tea")
else:
    print("We'll make do with water")

s16 = "Apprenticeship"
print(s16[10:14])

s17 = "hello"
print(s17.upper())

s18 = "hello"
print(s18.capitalize())

s19 = "lower"
print(s19.capitalize())

s20 = "   lower    "
print(s20.strip())


text = "hello"
uppercase = text.upper()
print(uppercase)

text2 = "hello"
capital = text2.capitalize()
print(capital)

text3 = "NYC"
lowercase = text3.lower()
print(lowercase)

text4 = "   Hello everyone!    "
remove = text4.strip()
print(remove)

text4 = "   Hello everyone!    "
remove = text4.strip(" He! ")
print(remove)

first = "john"
last = "watts"
full = first + " " + last
print(full)