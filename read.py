data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
print(sum_len)
print(sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
