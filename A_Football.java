import java.util.Scanner;

public class A_Football {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String n = sc.next();   
        sc.close();

        if (n.contains("0000000") || n.contains("1111111")) System.out.println("YES");
        else {System.out.println("NO");}

    }
}