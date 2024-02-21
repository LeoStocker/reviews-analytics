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

new2 = []
for d in data:
	if 'good' in d:
		new2.append(d)
print('一共有', len(new2), '筆留言包含good')


#字典查詢
wc = {}
for d in data:
	word = d.split()
	for w in word:
		if w in wc:
			wc[w] += 1
		else:
			wc[w] = 1
while True:
	search = input('請輸入您要找的字: ')
	if search == '幹不查了':
		break
	elif search in wc:
		print(wc[search])
	else:
		print('沒有這個字喔!')
print('感謝您的查詢')

