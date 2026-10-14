public class ShoppingBill {

    public static double calculateElectronicsGST(double a, double b) {
        double total = a + b;
        double gst = total * 0.18;
        return total + gst;
    }

    public static double calculateFashionGST(double c, double d) {
        double total = c + d;
        double gst = total * 0.13;
        return total + gst;
    }

    public static double calculateFoodGST(double e) {
        double gst = e * 0.07;
        return e + gst;
    }

    public static double totalBill(double a, double b, double c, double d, double e) {
        double electronics = calculateElectronicsGST(a, b);
        double fashion = calculateFashionGST(c, d);
        double food = calculateFoodGST(e);
        return electronics + fashion + food;
    }

    public static double calculateDiscountedBill(double a, double b, double c, double d, double e) {
        double total = totalBill(a, b, c, d, e);
        double discount = total * 0.20;
        double finalAmount = total - discount;
        return finalAmount;
    }

    public static void main(String[] args) {
        double a = 100, b = 100, c = 100, d = 100, e = 100;
        
        double totalAfterGST = totalBill(a, b, c, d, e);
        double discount = totalAfterGST * 0.20;
        double finalPayable = calculateDiscountedBill(a, b, c, d, e);

        System.out.printf("Total after GST = %.2f | Discount = %.2f | Final payable amount = %.2f", totalAfterGST, discount, finalPayable);
    }
}
