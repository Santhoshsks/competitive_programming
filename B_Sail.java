import java.util.Scanner;

public class B_Sail {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int x0 = scanner.nextInt();
        int y0 = scanner.nextInt();
        int x1 = scanner.nextInt();
        int y1 = scanner.nextInt();
        scanner.nextLine(); 
        String dir = scanner.nextLine();
        scanner.close(); 
        int ans = -1;
        
        for (int i = 0; i < t; i++) {
            char direction = dir.charAt(i);

            switch(direction) {
                case 'E':
                    if (x0 - x1 < 0) {
                        x0 = x0 + 1;
                    }
                    break;
                case 'W':
                    if (x0 - x1 > 0) {
                        x0 = x0 - 1;
                    }
                    break;
                case 'S':
                    if (y0 - y1 > 0) {
                        y0 = y0 - 1;
                    }
                    break;
                default:
                    if (y0 - y1 < 0) {
                        y0 = y0 + 1;
                    }
            }
            if (x0 == x1 && y0 == y1) {
                ans = i + 1;
                break;
            }
        }
        System.out.println(ans);
    }
}