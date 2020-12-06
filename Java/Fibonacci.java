
public class Fibonacci {

    public static void main(String[] args) {

        printFibis(1000);

    }

    public static void printFibis(int end) {
        if (end < 1) {
            return;
        }
        int currentNum = 1;
        int prevNum = 0;
        while(currentNum<=end) {
            System.out.println(currentNum);
            int temp = currentNum;
            currentNum += prevNum;
            prevNum = temp;
        }
    }
}