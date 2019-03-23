products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
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

