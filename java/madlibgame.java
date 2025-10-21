import java.util.Scanner;

public class madlibgame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String adj1, adj2, adj3;
        String verb1, verb2;
        String noun1;

        System.out.println("Enter an adjective describing the zoo: ");
        adj1 = scanner.nextLine();
        System.out.println("Enter the name of the animal: ");
        noun1 = scanner.nextLine();
        System.out.println("Enter an adjective describing the animal: ");
        adj2 = scanner.nextLine();
        System.out.println("Enter the animal's action: ");
        verb1 = scanner.nextLine();
        System.out.println("Enter your reaction: ");
        adj3 = scanner.nextLine();

        System.out.println("today i went to a "+  adj1 +" zoo");
        System.out.println("In an exhibit, i saw "+  noun1 +".");
        System.out.println(noun1 + " was " + adj2 + " and " + verb1 + "!");
        System.out.println("i was "+ adj3 + "." );

        scanner.close();
    }
}
