import java.util.Scanner;

public class A_Dubstep {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String remix = sc.nextLine();
        sc.close();
        
        String[] parts = remix.split("WUB");

        StringBuilder originalSong = new StringBuilder();

        for (String part : parts) {
            if (!part.isEmpty()) {
                originalSong.append(part).append(" ");
            }
        }
        System.out.println(originalSong.toString().trim());
    }
}
