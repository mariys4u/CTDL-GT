def foo(array):  # ham foo co tham so la mang
    sum = 0  # khoi tao bien sum = 0
    product = 1  # khoi tao bien product = 1
    for i in array:  # duyet mang array
        sum += i  # sum = sum + i
    for i in array:  # duyet mang array
        product *= i  # product = product * i
    print("Sum = " + str(sum) + ", Product = " + str(product))  # In ra kết quả tổng và sản phẩm của mảng array


foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # goi ham foo -> trả kết quả ra màn hình Sum = 55, Product = 3628800