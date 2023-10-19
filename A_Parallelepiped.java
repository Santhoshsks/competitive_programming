import java.util.Scanner;

public class A_Parallelepiped {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int ans = (int)(4 * (Math.sqrt((a*b)/c) + Math.sqrt((c*b)/a) + Math.sqrt((c*a)/b)));
        System.out.print(ans);
    }
}