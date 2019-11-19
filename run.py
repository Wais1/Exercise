#3.4

guestList = ['Albert Einstein', 'Elon Musk', 'Arnold Schwarzenegger', 'Kevin Systrom', 'Warren Buffet']
for person in guestList:
    print("Dear " + person + ", you are invited to a dinner gathering")

#3.5

print(guestList[0] + " cannot attend the dinner because he's too busy")
guestList[0] = "Reid Hoffman"
for person in guestList:
    print("Dear " + person + ", you are invited to a dinner gathering")

#3.6
print("A bigger dinner table has been found")
guestList.insert(0,"Mom")
guestList.insert(int(len(guestList)/2), "Dad")
guestList.append("Dave Chappelle")
for person in guestList:
    print("Dear " + person + ", you are invited to a dinner gathering")


#3.7
print("Unfortunately, only two people can attend this dinner")
while len(guestList)>2:
    print(guestList.pop() + ", Sorry that you can't attend")
for person in guestList:
    print("Dear " + person + ", you are welcome to join the dinner")
del guestList[0:2]
print(guestList)

#3.8

locations = ['France', 'Italy', 'San Diego', 'Los Angelos', 'Greece']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse = True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

