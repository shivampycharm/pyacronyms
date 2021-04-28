string = input("Enter the Words : ")
split_str = string.split()
acronym = ""
for word in split_str:
    acronym += word[0].upper()
print(acronym)
