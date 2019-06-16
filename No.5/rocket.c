#include <stdio.h>

int main() {
	double m, fuel, gravity;
	m = 500;
	gravity = 9.81;
	double engine = 300 * 9.81;
	double a = 0;
	double v0 = 0;

	a = (engine*4 - m * g) / m;

	double x = 0;

/*	x = -0.5 * a * t * t + v0 * t;   */

	int i;

	for (i = 0; i < 1000; i++) {
		x = -0.5 * a * i * i + v0 * i;
	}
}