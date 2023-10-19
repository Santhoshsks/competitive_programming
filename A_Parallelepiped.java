import java.util.Scanner;

class A_Parallelepiped {
    public static int gcd(int a, int b) {
        int i = 1;
        if (a < b) 
            i = a;
        else 
            i = b;

        for(;i > 1; i--) {
            if (a % i == 0 && b % i == 0) {
                return i;
            }
        }
        return 1;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int gcdOfab = gcd(a,b);
        int gcdOfbc = b / gcdOfab;
        int gcdOfac = c / gcdOfbc;
        
        System.out.print(4 * (gcdOfab + gcdOfbc + gcdOfac));
    }
}