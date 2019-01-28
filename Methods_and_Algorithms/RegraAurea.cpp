#include <iostream>
#include <iomanip>
#include <cmath>

/*
 * QUICK FYI: Nao sei ate que ponto e que isto esta bem ou mal, pretty sure que esta um lodo...
 * please dont quote my code :)
 */

using namespace std;

float f(float x) {
	return 0.28 * x *x + 0.5 * x + 2;
}

int main() {
	
	float x1 = -1;
	float x2 = 0;
	float x3, x4;
	float B = (sqrt(5) - 1) / 2;
	float A = B * B;

	x3 = A * (x2 - x1) + x1;
	x4 = B * (x2 - x1) + x1;
	
	while (abs(x2-x1) > 0.00001) { // Condicao de paragem
	//for(int i = 0; i < 24; i++) {
		if (f(x3) < f(x4)) {
			x2 = x4;
			// FORMA ESTUPIDA DO SOEIRO
			// x4 = x3;
			// x3 = B * (x4 - x1) +  x1;
		}
		else {
			x1 = x3;
			// FORMA ESTUPIDA DO SOEIRO
			// x3 = x4;
			// x4 = B * (x2 - x3) +  x3;
		}
		// FORMA COMO UMA PESSOA NORMAL FARIA :)
		x3 = A * (x2 - x1) + x1;
		x4 = B * (x2 - x1) + x1;
		//cout << x1 << endl << x2 << endl;
		//cout << x3 << endl << x4 << endl;
	}

	cout << "minimo " << endl;

	cout << x1 << endl << x2 << endl;
	cout << x3 << endl << x4 << endl;

	// system("pause");

	return 0;
}
