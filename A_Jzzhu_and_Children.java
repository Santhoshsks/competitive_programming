import java.util.Scanner;

public class A_Jzzhu_and_Children {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine();
        int ans = 0;
        double comp = 0;
        for (int i = 1; i <= n; i++) {
            
            double inp = scanner.nextInt();
            if (Math.ceil(inp / m) >= Math.ceil(comp / m)) {
                ans = i;
                comp = inp;                
            }  else if (comp == 0) {
                ans = i;
            }
        }
        System.out.print(ans);
        scanner.close();        
    }
}