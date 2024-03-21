person_name = input().split()

if len(person_name) == 3:
    first_name, middle_name, last_name = person_name
    print(f'{last_name}, {first_name[0]}.{middle_name[0]}.')

elif len(person_name) == 2:
    first_name, last_name = person_name
    print(f'{last_name}, {first_name[0]}.')
