ls1 = [1,2,3,4,5,6,7,8,9,10]

# in phần tử trong list 1->10
for i in ls1:
    print(i)

print("-"*10)

# in trong các phần tử trong list bỏ qua số 7
for i in ls1:
    if i == 7:
        continue
    else:
        print(i)

print("-"*10)

# in bình thường từ 1->9
for i in range(1,10):
    print(i);
print("-"*10)

#in nhảy bước 2 từ 1 -> 9
for i in range(1,10,2):
    print(i);
print("-"*10)


#in ngược từ 10 -> 2
for i in range(10,1,-1):
    print(i)
print("-"*10)