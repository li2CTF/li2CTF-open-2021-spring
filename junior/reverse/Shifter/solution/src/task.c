#include <stdio.h>
#include <string.h>

const char check[] = {96, 102, 91, 97, 117, 47, 98, 43, 96, 49, 43, 104, 97, 89, 43, 47, 89, 46, 102, 47, 42, 89, 101, 104, 42, 113, 104, 89, 46, 47, 89, 93, 46, 45, 47, 46, 108, 89, 93, 43, 106, 98, 45, 108, 119};

void print_banner() {
	printf("========= Welcome to the flag checker =========\n");
	printf("Enter the flag to check, young reverser\n[+]> _____________________________________________\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b");
}

int check_flag(char input[], unsigned int length) {
	if (length < 45) {
		return 0;
	}
	for (int i = 0; i < length; i++) {
		if (input[i] != check[i] + 6) {
			return 0;
		}
	}
	return 1;
}

int main() {
	char input[46] = {0};
	print_banner();
	scanf("%45s", input);
	unsigned int length = strlen(input);
	if (check_flag(input, length)) {
		printf("Nice, take your flag, young reverser: %s\n", input);
	}
	else {
		printf("Flag is incorrect\n");
	}
	return 0;
}