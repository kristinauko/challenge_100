"""
Given an unordered list of flights taken by someone, each represented as 
(origin, destination) pairs, and a starting airport, compute the person's 
itinerary. If no such itinerary exists, return null. If there are multiple 
possible itineraries, return the lexicographically smallest one. All flights 
must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), 
('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should 
return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting 
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
 even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, 
 the first one is lexicographically smaller.
"""


def intinerary(llist, start):
    """Take the list of possible destinations and return intinerary list"""
    
    itinerary_list = []
    itinerary_list.append(start)

    while len(llist) >= 1:
        current = None
        directions = {}

        for item in llist:
           
            if item[0] == start:
                directions[item[0]] = item[1]

        if len(directions) >= 1:
            current = min(directions.values())
            remove_tuple = (start, current)

        try:
            llist.remove(remove_tuple)
            itinerary_list.append(current)
            start = current
        except:
            return "not valid intinerary"

    return itinerary_list


print(intinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 
    'YUL'))

print(intinerary([('SFO', 'COM'), ('COM', 'YYZ')], 
    'COM'))

print(intinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 
    'A'))



