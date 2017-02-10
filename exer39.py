# ++++++++++ key, value in dictionary +++++ #
things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things

stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

# you can add things to a dict
stuff['city'] = "San Francisco"
print stuff['city']

stuff[1] = "Wow"
stuff[2] = "Neato"

print stuff[1]
print stuff[2]

print stuff

# a dict you can only put things in is pretty stupid, so here's how you delete things, with the del keyword:
del stuff['city']
del stuff[1]
del stuff[2]
print stuff

# Mapping or Associating is the key concept in a dictionary!!!
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print 'NY state has: ', cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then the cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]) # do not need to put quotes around abbrev!!!

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is : %s" % city
