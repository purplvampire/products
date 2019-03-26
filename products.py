import os
# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
            for line in f:      # 取出每行字串
                if '商品,價格' in line:
                    continue    # 略過迴圈中的其他指令,跳到下一個迴圈
                s = line.strip().split(',') # 先將每行字串清除換行符號,再以逗點切割成清單,存成s變數
                # name = s[0]
                # price = s[1]
                products.append(s)  # 將每行小清單存成一個大清單
                # 進階寫法
                # name, price = line.strip().split(',')   # 將split切割的清單依序套用到變數name跟price中
                # products.append([name, price])          # 建立[name, price]清單並加到products大清單中 
    print(products)
    return products 

# 讓使用者新增商品
def user_input(products):
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
    print(products[0][0]) # 印出大清單 index=0 中的小清單 index=0 的字串
    return products

# 印出所有購買紀錄
def print_products(products):
    for product in products:
        print('商品', product[0], '的價格是', product[1], '元')

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:    # 建立檔案並給予寫入(w)權限,設定編碼為通用模式(utf-8)
        f.write('商品,價格\n')      # 先加入欄位名稱
        for product in products:   # 取出清單中每筆資料
            f.write(product[0] + ',' + str(product[1]) + '\n')   # 將清單中每筆資料個別放入每行(\n)中,用+串聯字串與逗號(Excel分欄位用)
# 檢查檔案在不在

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  
        print('Yeah!找到檔案了!')
        products = read_file(filename) # 將回傳的products存到變數products
    else:
        print('找不到檔案....')
    products = user_input(products)      # 將輸入的值套用到products
    print_products(products)
    write_file(filename, products)

main()