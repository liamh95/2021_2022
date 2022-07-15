
p = 561
for a in range(1, p):
	if pow(a, p, p) != a:
		print a
		break