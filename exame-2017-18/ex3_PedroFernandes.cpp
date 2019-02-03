#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;

double ppMaior(double x)
{
	return log(5 + x);
}

double f(double x)
{
	return pow(exp(1),x) - x - 5;
}

double diff(double x)
{
	return pow(exp(1),x) - 1;
}

void picardPeano(double pp(double), int numIt, double guess)
{
	for (int i = 0; i < numIt; ++i)
	{
		guess = pp(guess);
		cout << "It: " << i << "\t x = " << guess << endl;
	}
}

void newton(double f(double), double diff(double), int numIt, double x)
{
	//Completar um numero suficiente de iteracoes
	for (int i = 0; i < numIt; ++i)
	{
		x -= f(x) / diff(x);
		cout << "It: " << i << "\t x = " << x << endl;
	}
}


int main()
{
	cout << fixed << setprecision(5);

	cout << "PicardPeano" << endl;
	picardPeano(ppMaior, 10, 3.0);

	cout << endl << endl << "Newton" << endl;
	newton(f, diff, 10, 3.0);

	return 0;
}
