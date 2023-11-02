import java.util.Arrays;
import java.util.Scanner;

public class A_Business_trip {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();  
        int[] a = new int[12];  

        for (int i = 0; i < 12; i++) {
            a[i] = sc.nextInt();
        }

        int result = minMonthsToWaterFlower(k, a);
        System.out.println(result);

        sc.close();
    }

    public static int minMonthsToWaterFlower(int k, int[] a) {
        Arrays.sort(a);
        int temp = 0;
        if (k == 0) return 0;
        else {
            for (int i = a.length - 1; i >= 0; i--) {
                temp += a[i];
                if (temp >= k) {
                    return a.length - i;
                }
            }
        }
        return -1; 
    }
}