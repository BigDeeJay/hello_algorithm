# 2292
import sys

N = int(sys.stdin.readline().strip())
chk = 1
start = 2
i = 0
div = 6

while 1 :
	if N == 1 :
		print(1)
		exit()
	while i < div * chk :
		if start == N :
			print(chk+1)
			exit()
		else :
			start += 1
			i += 1
	i = 0
	chk += 1