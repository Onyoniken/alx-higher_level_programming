#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * main - main function
 * @argc: arg no
 * @argv: arg pass
 *
 * Return: 0 success, 1 failure
 */
int main(int argc, char *argv[])
{
	unsigned int j, k;
	size_t a, b;
	char *c = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char p[7] = "      ";

	if (argc != 2)
	{
		printf("Correct usage: ./keygen5 username\n");
		return (1);
	}
	a = strlen(argv[1]);
	p[0] = c[(a ^ 59) & 63];
	for (j = 0, b = 0; j < a; j++)
		b += argv[1][j];
	p[1] = c[(b ^ 79) & 63];
	for (j = 0, k = 1; j < a; j++)
		k *= argv[1][j];
	p[2] = c[(k ^ 85) & 63];
	for (k = argv[1][0], j = 0; j < a; j++)
		if ((char)k <= argv[1][j])
			k = argv[1][j];
	srand(k ^ 14);
	p[3] = c[rand() & 63];
	for (k = 0, j = 0; j < a; j++)
		k += argv[1][j] * argv[1][j];
	p[4] = c[(k ^ 239) & 63];
	for (k = 0, j = 0; (char)j < argv[1][0]; j++)
		k = rand();
	p[5] = c[(k ^ 229) & 63];
	printf("%s\n", p);
	return (0);
}
