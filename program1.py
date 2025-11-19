class Calculator {

    double calculate(double a, double b, String operation) {
        switch (operation.toLowerCase()) {
            case "add":
                return a + b;

            case "sub":
            case "subtract":
                return a - b;

            case "mul":
            case "multiply":
                return a * b;

            case "div":
            case "divide":
                if (b == 0) {
                    System.out.println("Cannot divide by zero!");
                    return 0;
                }
                return a / b;

            default:
                System.out.println("Invalid operation");
                return 0;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator c = new Calculator();

        double a = 10;
        double b = 5;

        System.out.println("Addition: " + c.calculate(a, b, "add"));
        System.out.println("Subtraction: " + c.calculate(a, b, "sub"));
        System.out.println("Multiplication: " + c.calculate(a, b, "mul"));
        System.out.println("Division: " + c.calculate(a, b, "div"));
    }
}
