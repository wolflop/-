# -*- coding:utf-8 -*-
from collections import Counter
def jugeEqule(Alist, Blist):
	Alist_1 = Counter(sorted(Alist))
    Blist_1 = Counter(sorted(Blist))
	counter = 0
	if len(Alist_1) != len(Blist_1):
  		print("Alist and Blist is not euqle.")
	else:
		while (counter < len(Alist_1)):
			if Alist[counter] != Blist[counter]:
				print("Alist and Blist is not euqle.")
				break
			else:
				counter += 1
				if counter == len(Alist_1):
					print("Alist and Blist is equle")

if __name__ == '__main__':
	Alist = []
	Blist = []
	jugeEqule(Alist, Blist)
