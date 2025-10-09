fruits = ["apple", "banana", "orange"]
prices = [1.99,2.99,3.99]
quantity = [1, 2, 3]
cart = [fruits, prices, quantity]

#tạo thành một mảng 2 chiều gồm 2 dòng 3 cột
# print(intnchar[2][1])
for i in cart:
    for j in i:
        print(j)

# chạy i trong cart -> với vòng lặp đầu i là list fruits -> j chạy trong list fruits