import java.util.Scanner;

public class A_Petr_and_Book {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] pagesPerDay = new int[7];

        for (int i = 0; i < 7; i++) {
            pagesPerDay[i] = sc.nextInt();
        }

        int remainingPages = n;
        int day = 0;

        while (remainingPages > 0) {
            remainingPages -= pagesPerDay[day];
            day = (day + 1) % 7;
        }

        // Adjust for 0-based indexing of days and handle Sunday (0 -> 7)
        if (day == 0) {
            day = 7;
        }

        System.out.println(day);
    }
}