#Python Question oriented

#Lists
#1
people_names = ["Bryan", "Elton", "Cynthia", "Joanne", "Moses", ]
print("----------------------------------")
#2
print("The 2nd item in the list is", people_names[1])
print("----------------------------------")
#3
people_names.append("Petero")
print("The new list of names of people is", people_names)
print("----------------------------------")

#4
people_names.insert(2, "Bathel")
print("The new list of names of people is", people_names)
print("----------------------------------")

#5
people_names.remove(people_names[3])
print("The new list of names of people is", people_names)
print("----------------------------------")

#6
print("The last item in the list is", people_names[-1])
print("----------------------------------")

#7
number_list = [1, 2, 3, 4, 5, 6, 7,]
print("The 3rd, 4th and 5th items in the list are", number_list[2:5])
print("----------------------------------")

#8
african_countries = ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "Somalia", "Eritrea", "Djibouti"]
african_countries_copy = african_countries.copy()
print("The new copied list of African countries is ", african_countries_copy)

#9
for country in african_countries:
    print(country)
print("----------------------------------")

#10
animal_list = ["Lion", "Tiger", "Leopard", "Cheetah", "Hyena", "Jackal", "Fox", "Wolf", "Wild Dog", "Wild Cat"]
print("The sorted animal list (ascending order) is", sorted(animal_list))
print("The sorted animal list (descending order) is", sorted(animal_list, reverse=True))
print("----------------------------------")

#11
for animal in animal_list:
    if 'a' in animal:
        print(animal)
print("----------------------------------")

#12
first_names_list = ["Sekidde", "Ssenabulya", "Mukalazi", "Aliddkei"]
second_names_list = ["Bryan", "Reagan", "Ashiraf,", "Benard", "Francis"]
joined_list = first_names_list + second_names_list
print("The joined list is", joined_list)
print("----------------------------------")






