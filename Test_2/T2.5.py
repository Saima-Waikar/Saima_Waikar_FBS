for i in range(0,5):
    price = int(input("Enter price of product:"))
gst = (price * 18)/100
total_price = price - gst
print(price)
print(total_price)