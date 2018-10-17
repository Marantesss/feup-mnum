#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double funcao(double x)
{
    return (x - x*x); //function x - x^2 = 0
}

int main()
{
    const unsigned int RESULT_PRECISION = 100;
    // [a,b] tem que ter apenas uma raiz
    double a, b;
    a = 0.5;
    b = 1.4;
    double m;

    for (int i = 0; i < 80; i++) {
        m = (a+b)/2;
        if ((funcao(m) > 0 && funcao(a) > 0) || (funcao(m) < 0 && funcao(a) < 0))
           a = m;
        else if (funcao(m) < 0 && funcao(b) < 0 || (funcao(m) > 0 && funcao(b) > 0))
            b = m;
    cout << setprecision(RESULT_PRECISION) << "a = " << a << endl << "b = " << b << endl << "m = " << m << endl << endl;
    }

    m = (a+b)/2.0;
    cout << setprecision(RESULT_PRECISION) << m << endl;
    return 0;
}

