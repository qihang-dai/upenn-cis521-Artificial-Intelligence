## Tricky Part

PriorityQueue in python is hard to use a custom comparator. I have to use a tuple to store the value and the index of the value. Then I can use the index to compare the value.

PQ would compare evey entry in tuple, if tuple[0] is equal, then it will compare tuple[1], [2] and so on.  However Object can not be compared though list can be compared. Maybe tuple can be compared too. This time i use an extra increasing index to avoid the compare between two objects. 