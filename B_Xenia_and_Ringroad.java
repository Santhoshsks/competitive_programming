import java.util.Scanner;

public class B_Xenia_and_Ringroad {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int prev = 1; 
        long ans = 0;

        for (int i = 0; i < m; i++) {
            int ai = sc.nextInt();
            if (ai >= prev) {
                ans += ai - prev;
            } else {
                ans += n - prev + ai;
            }
            prev = ai;
        }
        
        sc.close();
        System.out.println(ans);
    }
}