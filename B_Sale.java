import java.util.Arrays;
import java.util.Scanner;

public class B_Sale {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        int ans = 0;
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();
        Arrays.sort(a);

        for (int i = 0; i < m; i++) {
            if (a[i] < 0) {
                ans -= a[i];
            } else {
                break;
            }
        }
        System.out.println(ans);
    }
}