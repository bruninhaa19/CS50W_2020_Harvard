people = [
    {"name": "Bruna", "house": "verde"},
    {"name": "Ana", "house": "azul"},
    {"name": "Zeide", "house": "marrom"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

#ou
# people = [
#    {"name": "Bruna", "house": "verde"},
#    {"name": "Ana", "house": "azul"},
#    {"name": "Zeide", "house": "marrom"}
# ]


# people.sort(key=lambda person: person["name"])

# print(people)

