import java.util.*; 

public class PrimeNumberGenerator{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter num> ");
        int num = sc.nextInt();
        boolean isTrue;
        if (num == 2) {
        	System.out.println(2);
        }
        for (int i = 2; i < num; i++) {
        	isTrue = isPrime(i);
        	if (isTrue) {
        		System.out.print(i + " ");
        	}
        }

    }

    public static boolean isPrime(int num1) {
    	for (int i = 2; i < num1; i++) {
    		if (num1 % i == 0) {
    			return false;
    		}
    	}
    	return true;
    }
}