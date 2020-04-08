def hydrate(drink_string):
	count=0
	count=sum(int(i) for i in drink_string if i.isdigit())
	return ("{} glass of water".format(count)) if count==1 else ("{} glasses of water".format(count))
	
print(hydrate("1 beers"))
print(hydrate("1 beers, 2 wine, 3 beers"))

# посчитать количество стаканов воды в зависимости от выпитого алкоголя.

			