i=2
while (i<10):
	j=2
	while (j<=i/j):
		if not (i%j):
			break
		j=j+1
	if (j>i/j):
		print i,"is prime number"
	i=i+1
