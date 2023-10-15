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
        int ways = 0;
        for (int i = 1; i < 6; i++) {
            if ((ans + i) % (numOfFriends + 1) != 1) ways++;
        }     
        System.out.println(ways);
        
    }
}
