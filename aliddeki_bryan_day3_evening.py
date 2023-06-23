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

#Exercise2: tuples
#1
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite brand is", x[0])
print("----------------------------------")

#2
print("The second item using negative indexing is", x[-3])
print("----------------------------------")

#3
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("The new tuple is", x)
print("----------------------------------")


#4
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print("The new tuple is", x)
print("----------------------------------")


#5
for phone in x:
    print(phone)
print("----------------------------------")

#6
x_list = list(x)
x_list.remove(x_list[0])
x = tuple(x_list)
print("The new tuple is", x)
print("----------------------------------")

#7
ugandan_cities_list = ["Kampala", "Jinja", "Entebbe",  "Kasese"]
uganda_cities = tuple(ugandan_cities_list)
print("The tuple of Ugandan cities is", uganda_cities)
print("----------------------------------")

#8
a, b, c, d = uganda_cities
print("The first city is", a)
print("The second city is", b)
print("The third city is", c)
print("The fourth city is", d)
print("----------------------------------")

#9
print("The 2nd, 3rd,and 4th cities in the tuple is", uganda_cities[1:4])
print("----------------------------------")

#10
first_names_tuple = ("Sekidde", "Ssenabulya", "Mukalazi", "Aliddkei")
second_names_tuple = ("Bryan", "Reagan", "Ashiraf,", "Benard", "Francis")
joined_tuple = first_names_tuple + second_names_tuple
print("The joined tuple is", joined_tuple)
print("----------------------------------")

#11
color_tuple = ("red", "blue", "green", "yellow", "white", "brown")
color_tuple_multiplied = color_tuple * 3
print("The multiplied tuple is", color_tuple_multiplied)
print("----------------------------------")

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
z = 0
for number in thistuple:
    if number == 8:
        z += 1

print("The number of times 8 appears in the tuple is", z)


#Exercise3: Sets
#1
favorite_beverages = set([ "milk", "tea", "soda"])
print("My favorite beverages are", favorite_beverages)
print("----------------------------------")

#2
favorite_beverages.add("coffee")
favorite_beverages.add("water")
print("My favorite beverages now are", favorite_beverages)

#3


        








