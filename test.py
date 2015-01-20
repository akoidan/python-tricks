from itertools import cycle, islice, dropwhile
li = cycle ( [5,3]  )
for i in range(6):
	print ( next(li) )
