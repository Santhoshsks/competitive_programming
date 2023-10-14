import java.util.Scanner;

public class A_Petya_and_Strings {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        s1 = s1.toUpperCase();
        s2 = s2.toUpperCase();
        int ans = s1.compareTo(s2);
        if (ans < 0) {
            System.out.println("-1");
        } else if (ans > 0) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
    }
}
