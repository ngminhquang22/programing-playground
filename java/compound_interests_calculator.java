import java.util.Scanner;


public class compound_interests_calculator{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double principal, rate, amount;
        int timesCompound,years;

        System.out.println("Enter the principal amount: ");
        principal = scanner.nextDouble();
        scanner.nextLine();
        System.out.println("Enter the interests rate (in %): ");
        rate = scanner.nextDouble()/100;
        scanner.nextLine();
        System.out.println("Enter the # of times compounded per year: ");
        timesCompound = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter the number of years: " );
        years = scanner.nextInt();
        scanner.nextLine();
        
        amount = principal * Math.pow(1+rate/timesCompound, timesCompound * years);
        System.out.println("The amount after "+  years + " is: $"+ amount);


        scanner.close();

    }
}