#include <ctype.h>
#include <stdio.h>

unsigned int seed = 0;

unsigned int r4nd0m(unsigned int prev) {
    return prev * 1664523U + 1013904227U;
}

int main() {
	int coins = 100;
	unsigned int r4ndNumber = 0;
	seed = 0xFADECAFE;

	printf("There is a sequence of commands to earn 200 coins: ");
	for (int i = 0; i < 100; i++) {
		r4ndNumber = seed = r4nd0m(seed) % 10;
		coins += 10;
		printf("p%d", r4ndNumber);
		if (coins == 200) {
			printf("s\nThe last one is: %d\n", r4ndNumber);
			break;
		}
	}

	return 0;
}