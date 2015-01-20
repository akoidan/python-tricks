from string import Template


class MyTemplate(Template):
	delimiter = '#'

def main():
	cart = []
	cart.append(dict(item="coke",price=8,qty=2))
	cart.append(dict(item="cake",price=22,qty=1))
	cart.append(dict(item="fish",price=24,qty=100))
	t = MyTemplate("#qty x #item = #price")
	total = 0
	print ("cart: ")
	for data in cart:
		print (t.substitute(data))
		total+=data["price"]
	print (total)
if __name__ == "__main__":
	main()

#
