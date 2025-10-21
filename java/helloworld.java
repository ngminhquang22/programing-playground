import java.util.Scanner;

public class helloworld{
    public static void main(String[] agrs){
        Scanner scanner = new Scanner(System.in);
        String hello = scanner.nextLine();
        System.out.println(hello);
        scanner.close();
    }
}