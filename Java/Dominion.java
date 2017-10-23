import java.util.Scanner;
import java.util.Random;

public class Dominion {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		double p1, p2, p3, pm, chance, cards = 5;
		int tries = 0, coins = 0;

		p1 = Double.parseDouble(scan.nextLine());
		p2 = Double.parseDouble(scan.nextLine());
		p3 = Double.parseDouble(scan.nextLine());
		pm = Double.parseDouble(scan.nextLine());

		Random rand = new Random();


		while(coins < 8) {
			chance = rand.nextDouble();
			System.out.println("heres the chance: " + chance);
			if (chance < pm) {
				cards = 3;
			}
			for (int i = 0; i < cards; i++) {

				if(chance < p1) {
					coins = coins + 1;
				}
				if (chance < p2) {
					coins = coins + 2;
				}
				if (chance < p3) {
					coins = coins + 3;
				}
			}
			tries++;
		}

		System.out.println(tries);

	}
}