import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static class Intervals {
        int start;
        int end;

        public Intervals(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int get_start() {
            return this.start;
        }
        public void change_start(int start) {
            this.start = start;
        }
        public void change_end(int end) {
            this.end = end;
        }
        public int get_end() {
            return this.end;
        }
        public String toString() {
            return "[" + start + ", " + end + "]";
        }
    }
    public static class Merger {
        List<Intervals> intervals = new ArrayList<>();

        public void add_intervals( int a, int b) {
            intervals.add(new Intervals(a,b));
        }
        public void print_intervals() {
            for(Intervals interval:intervals) {
                System.out.print(interval);
            }
        }

        public boolean is_empty() {
            return this.intervals.size() == 0;
        }
        public Intervals get_last() {
            return this.intervals.get(this.intervals.size()-1);
        }
        public void sort_intervals() {
            intervals.sort((o1, o2) -> {
                if (o1.get_start() < o2.get_start()) {
                    return -1;
                } else if (o1.get_start() > o2.get_start()) {
                    return 1;
                } else {
                    return 0;
                }
            });
        }
        public void merge() {
            System.out.print("Intervals:");
            this.print_intervals();
            sort_intervals();
            System.out.print("Sorted:");
            this.print_intervals();
            System.out.print("Answer:");
            Merger answer = new Merger();

            for(int i = 0; i < intervals.size(); i++) {
                if (answer.is_empty() || intervals.get(i).get_start() > answer.get_last().get_end())
                    answer.add_intervals(intervals.get(i).get_start(),intervals.get(i).get_end());
                else
                    answer.get_last().change_end(Math.max(intervals.get(i).get_end(), answer.get_last().get_end()));
            }
            answer.print_intervals();
        }
    }

    public static void main(String[] args) {
        Merger merger_obj = new Merger();

        Scanner scanner_obj = new Scanner(System.in);

        System.out.print("Enter number of intervals:");
        int number_of_intervals = scanner_obj.nextInt();
        scanner_obj.nextLine();

        for(int i = 0; i < number_of_intervals; i++) {
            System.out.print("Start:");
            int start = scanner_obj.nextInt();
            System.out.print("End:");
            int end = scanner_obj.nextInt();
            merger_obj.add_intervals(start,end);
        }

        merger_obj.merge();
    }
}
