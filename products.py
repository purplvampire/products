products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    # 第一種作法
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)

    # 第二種作法
    # p = [name, price]
    # products.append(p)

    # 第三種作法
    products.append([name, price])

print(products)

# 印出大清單 index=0 中的小清單 index=0 的字串
print(products[0][0])

# 條列式印出小清單
for product in products:
    print(product)
# 改成名稱對應價格
    print('商品', product[0], '的價格是', product[1], '元')

# 將資料儲存
with open('products.csv', 'w', encoding='utf-8') as f:    # 建立檔案並給予寫入(w)權限,設定編碼為通用模式(utf-8)
    f.write('商品,價格\n')      # 先加入欄位名稱
    for product in products:   # 取出清單中每筆資料
        f.write(product[0] + ',' + str(product[1]) + '\n')   # 將清單中每筆資料個別放入每行(\n)中,用+串聯字串與逗號(Excel分欄位用)


