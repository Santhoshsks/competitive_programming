import java.util.Scanner;

public class B_Xenia_and_Ringroad {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        int temp = sc.nextInt();
        int prev = temp;
        int ans = temp;
        for (int i = 0; i < m - 1; i++) {
            temp = sc.nextInt();
            if (temp == prev) {
                continue;
            } else if (temp < prev) {
                ans += (n - prev) + temp;
                prev = temp;
            } else {
                ans += temp - prev;
                prev = temp;
            }
        }
        sc.close();
        System.out.println(ans - 1);        
    }
}