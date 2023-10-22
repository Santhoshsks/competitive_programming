import java.util.Scanner;

public class A_Little_Elephant_and_Rozdil {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean flag =true;
        int position = 0;
        double temp = Math.pow(10, 9) + 1;
        for (int i = 0; i < n; i++) {
            double inp = sc.nextInt();
            if (temp > inp) {
                temp = inp;
                position = i + 1;
                flag = true;
            } else if (temp == inp) {
                flag = false;
            }
        }
        if (flag) {
            System.out.println(position);
        } else {
            System.out.println("Still Rozdil");
        }
    }
}