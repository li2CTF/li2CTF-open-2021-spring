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

	for (int i = 0; i < 100; i++) {
		r4ndNumber = seed = r4nd0m(seed) % 10;
		coins += 10;
		printf("%d - %d\n", coins, r4ndNumber);
		if (coins == 200) {
			printf("The last one is %d", r4ndNumber);
			break;
		}
	}

	return 0;
}