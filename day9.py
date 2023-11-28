#day8
#Dictonaries, Nesting and the secret auction

programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function":
    "A piece of code that you can easily call over and over again."
}

print(programming_dictionary)

#Retreiving a value from a dictionary
print(programming_dictionary["Bug"])

#Adding new iteam to a dictionary
programming_dictionary["Loop"] = "A part of a program that repeats."
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Loop"] = "A part of a program that repeats until a certain condition is met."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#Create an empty dictionary
empty_dictionary = {}

#Wipe an epmty dictionary
programming_dictionary = {}
print(programming_dictionary)

#Nesting Lists
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
  "United States": "Washington DC"
}

#Nesting a List in a Dicitionary
travel_log = {
  "France": ["Paris", "Eiffel Tower"],
  "Germany": ["Berlin", "Brandenburg Gate"],
  "United States": ["Washington DC", "White House"]
}

print(travel_log)

#Nesting Dictionary in a Dicitionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Eiffel Tower"],
    "total_visits": 12,
    "last_visit": "Paris"
  },
  "Germany": {
    "cities_visited": ["Berlin", "Brandenburg Gate"],
    "total_visits": 5,
    "last_visit": "Berlin"
  }
}

print(travel_log)

#Nesting Dictionary in a List
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Eiffel Tower"],
    "total_visits": 12,
    "last_visit": "Paris"
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Brandenburg Gate"],
    "total_visits": 5,
    "last_visit": "Berlin"
  }
]

print(travel_log)
