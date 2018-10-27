#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

#define PI acos(-1)

double fd(double x, double y) {
	return (pow(x, 2) + pow(y, 2));
}

double fSin(double x) {
	return sin(x);
}

double euler(double x0, double y0, double h, unsigned int num_iter) {
	double x = x0, y = y0;

	cout << "0: \tx = " << fixed << setprecision(6) << x << "\ty = " << fixed << setprecision(6) << y << endl;

	for (size_t i = 1; i <= num_iter; i++) {
		y += h * fd(x, y);
        x += h;

		cout << i << ": \tx = " << fixed << setprecision(6) << x << "\ty = " << fixed << setprecision(6) << y << endl;
	}

	cout << endl << "---------------------------" << endl << endl;

	return y;
}

int ex1() {
    double s, sl, sll;

	cout << "\tX" << "\tY" << "\tQC" << endl << endl;

	s = euler(0, 0, 0.1, 14);
	sl = euler(0, 0, 0.05, 28);
	sll = euler(0, 0, 0.025, 56);

	double qc = (sl - s) / (sll - sl);
	double e = (sll - sl)/1;

	cout << "s = " << s << endl;
	cout << "sl = " << sl << endl;
	cout << "sll = " << sll << endl;
	cout << "QC = " << qc << endl;
	cout << "E = " << e << endl;

	return 0;
}

int main() {
    ex1();
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started:
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
