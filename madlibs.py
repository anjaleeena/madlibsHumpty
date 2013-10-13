import string

Humpty = """
Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't make Humpty Dumpty together again
"""

character1 = raw_input("Give me the name of a movie star.")
object1 = raw_input("Give me the name of an object.")
authorities = raw_input("Give me a job title.")
creatures = raw_input("Give me a plural creature.")
adjective = raw_input("Give me a food adjective.")

Humpty = string.replace(Humpty,"Humpty Dumpty", character1)
Humpty = string.replace(Humpty, "wall", object1)
Humpty = string.replace(Humpty, "king", authorities)
Humpty = string.replace(Humpty, "horses", creatures)
Humpty = string.replace(Humpty, "together", adjective)

print Humpty


#print """

#%s sat on a %s. %s had a great fall. All the %s's %s and all the %#s's men couldn't make %s %s again.
#""" % (character1, object1, character1, authorities, creatures, #authorities, character1, adjective)

