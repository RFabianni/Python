def computepay(h,r):
    return 498.75

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate")
r = float(rate)
if h > 40.0:
	pay = h * r * 1.5 - (40 * 0.5 * r) 
	p = float(pay)
print p