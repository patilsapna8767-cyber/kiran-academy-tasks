def calculateElectronicsGST(a, b):
    # my first PR by sapna
    total = a + b
    gst = total * 0.18
    return total + gst

def calculateFashionGST(c, d):
    total = c + d
    gst = total * 0.13
    return total + gst

def calculateFoodGST(e):
    gst = e * 0.07
    return e + gst

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    final_amount = total - discount
    return final_amount

def main():
    a, b, c, d, e = 100, 100, 100, 100, 100
    total_after_gst = totalBill(a, b, c, d, e)
    discount = total_after_gst * 0.20
    final_payable = calculateDiscountedBill(a, b, c, d, e)
    print(f"Total after GST = {total_after_gst:.2f} | Discount = {discount:.2f} | Final payable amount = {final_payable:.2f}")
    return final_payable

if __name__ == "__main__":
    main()
