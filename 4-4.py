products = []
while True:
	name = input("請輸入商品名稱: ")
	if name == 'q':
		break
	price = input('清輸入商品價格: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'
with open('products.csv', 'w' , encoding = 'utf-8') as f:# with關閉程式會異動close
	f.write('商品,價格\n')  # 前要加編碼才不會亂碼
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')# 串再一起要型別一樣