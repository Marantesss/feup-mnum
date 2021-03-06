#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double fd(double x) {
	return pow(x, 3);
}

double f(double x) {
	return pow(x, 4)/4;
}

double euler(double x0, double y0, double h, unsigned int num_iter) {
	double x = x0, y = y0;

	cout << "0: \tx = " << fixed << setprecision(6) << x << "\ty = " << fixed << setprecision(6) << y << endl;

	for (size_t i = 1; i <= num_iter; i++) {
		y += h * fd(x);
        x += h;

		cout << i << ": \tx = " << fixed << setprecision(6) << x << "\ty = " << fixed << setprecision(6) << y << endl;
	}

	cout << endl << "---------------------------" << endl << endl;

	return y;
}

int main() {
	double s, sl, sll;

	cout << "\tX" << "\tY" << "\tQC" << endl << endl;

	s = euler(0, 0, 0.5, 40);
	sl = euler(0, 0, 0.25, 80);
	sll = euler(0, 0, 0.125, 160);

	double qc = (sl - s) / (sll - sl);
	double e = (sll - sl)/1;

	cout << "s = " << s << endl;
	cout << "sl = " << sl << endl;
	cout << "sll = " << sll << endl;
	cout << "QC = " << qc << endl;
	cout << "E = " << e << endl;

	return 0;
}
