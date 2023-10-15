import java.util.Scanner;

public class A_Dima_and_Friends {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOfFriends = scanner.nextInt();
        long ans = 0;
        for (int i = 0; i < numOfFriends; i++) {
            int s = scanner.nextInt();
            ans += s;
        }
        scanner.close();
        if (ans % 2 == 0 && numOfFriends % 2 != 0) System.out.println(2);
        else System.out.println(3);      
        
    }
}
