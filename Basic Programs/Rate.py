hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Rate/hours :")
rph = float(rate)

if hrs > 40 :
	extrahrs = h - 40
	default = 40 * rph
	special = extrahrs * rph * 1.5
	total = default + special
	print (total)
else :
	total = h * rph
	print (total)
