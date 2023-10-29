import java.util.Scanner;

public class A_Bicycle_Chain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        double temp = 0;
        int ans = 0;
        double[] a = new double[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.nextLine();
        int m = sc.nextInt();
        sc.nextLine();
        double[] b = new double[m];
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                double ratio = b[j] / a[i];
                if (isInteger(ratio) && ratio > temp) {
                    temp = ratio;
                    ans = 1;
                } else if (isInteger(ratio) && ratio == temp) {
                    ans += 1;
                }
            }
        }

        System.out.println(ans);
    }

    public static boolean isInteger(double number) {
        return number == (int) number;
    }
}
