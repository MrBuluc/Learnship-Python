# 22.9

user = {"name": "Yunus", "surname": "Yıldırım", "mail": "yunusyildirim@gmail.com", "password": "123456"}

'döaşisd' "dlasödşil" # String

a = '''
dsaöldşiğasd
dşasiöçdişas
dölşais,öd
'''
print(a)

a = "Yunus"
print(a[0]) # Y
# a[1] = u
#a[1] = "a" hata

for letter in a:
    print(letter)
    
print(len(a)) # 5

a = "Yunus Learnship programında Python öğreniyor."
if "python" not in a:
    print("Yok")
    
print(a[-3:-1])

print(a.upper())
print(a.lower())
print(a)
a = a.upper()
print(a)

a = "    şdlöasi,şödi,şasö     "
print(a.strip())

a = "Yunus Learnship programında Python öğreniyor. Yunus"
print(a.replace("Yunus", "Hakkıcan"))

a = "1---FRNM3121049B---FP---2023-08-09T09:03:47+00:00"

print(a.split("---"))

print("Yunus" + " " + "Python")

age = 25
city = "Şanlıurfa"
name = "Yunus"
a = "{}'s age is {}. {}'s city is {}"
a = a.format(name, age, name, city)

print(a.count("Yunus"))

print(a.find("a"))
print(a.index(name))

a = False
print(bool({}))

print(10 % 2 == 0)
print(10 ** 2)
print(15 // 4)

b = 10
b += 5
b ^= 3
print(b)

a = 12
print(a is not b)

print((6 + 3) // (6 - 3))

c = ["Yunus", "Python", "Learnship"]
print(c)

c[1] = "C#"
print(c)

c = [1, 2, 3, 1, 3]
print(c)