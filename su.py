hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input ("Enter rate")
r = float(rate)
if h > 40.0:
	total = h * r * 1.5 - (40 * 0.5 * r) 
	t = float(total)
print (t)