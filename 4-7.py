import os # operating system
products = []
if os.path.isfile('products.csv'):#檢查檔案
	print('yeah! 我找到檔案了!')
# 讀取檔案

	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續此迴圈不坐
			name, price = line.strip().split(',') #切割 strip()把換行用掉
			products.append([name,price])
	print(products)

else:
	print('找不到檔案.......')

# 讓使用輸入
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
#印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])
#寫入檔案
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'
with open('products.csv', 'w' , encoding = 'utf-8') as f:# with關閉程式會異動close
	f.write('商品,價格\n')  # 前要加編碼才不會亂碼
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')# 串再一起要型別一樣