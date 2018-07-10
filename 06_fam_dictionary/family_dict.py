# 1. Define a dictionary that contains information about several members of your family.

my_family = {
    'sister': {
        'name': 'Nicole',
        'age': 32
    },
    'brother': {
        'name': 'Justin',
        'age': 29
    },
    'father': {
        'name': 'Rod',
        'age': 56
    },
    'mother': {
        'name': 'Cindy',
        'age': 57
    },
    'fiance': {
        'name': 'Megan',
        'age': 27
    }
}

# 2. Using a dictionary comprehension, produce output that looks like the following example.
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)
my_sentence_family = set()
for relation, relation_values in my_family.items():
    my_sentence_family.add(f"{relation_values['name']} is my {relation} and is {str(relation_values['age'])} years old.")

# print(my_sentence_family)


def single_member(relation):
        print(f"{my_family[relation]['name']} is my {relation} and is {my_family[relation]['age']} years old.")


# single_member("father")

family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

print("My family!", family_stuff)