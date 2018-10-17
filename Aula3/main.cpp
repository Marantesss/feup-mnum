#include <iostream>
#include <cmath>

using namespace std;

#define PI acos(-1)

double sinIntegralTrapezes(int trapNumb);
double sinIntegralSimpson(int trapNumb);

int main()
{
    // Trapezes rule
    cout << "------ TRAPEZES RULES ------" << endl;
    cout << "Sin Integral(10): " << sinIntegralTrapezes(10) << endl;
    cout << "Sin Integral(20): " << sinIntegralTrapezes(20) << endl;
    cout << "Sin Integral(50): " << sinIntegralTrapezes(50) << endl;
    cout << "Sin Integral(100): " << sinIntegralTrapezes(100) << endl;
    cout << "Sin Integral(500): " << sinIntegralSimpson(500) << endl;
    cout << "Sin Integral(1000): " << sinIntegralSimpson(1000) << endl;
    // Simpsons rule
    cout << endl << "------ SIMPSONS RULES ------" << endl;
    cout << "Sin Integral(10): " << sinIntegralSimpson(10) << endl;
    cout << "Sin Integral(20): " << sinIntegralSimpson(20) << endl;
    cout << "Sin Integral(50): " << sinIntegralSimpson(50) << endl;
    cout << "Sin Integral(100): " << sinIntegralSimpson(100) << endl;
    cout << "Sin Integral(500): " << sinIntegralSimpson(500) << endl;
    cout << "Sin Integral(1000): " << sinIntegralSimpson(1000) << endl;
    return 0;
}

double sinIntegralTrapezes(int trapNumb)
{

    double xValue = PI/(double)trapNumb; // Value of each individual trap base
    double xNewValue = PI/(double)trapNumb; // Value of each X coordinate
    double integral = 0;
    /*
    for (int i = 1; i < trapNumb; i++) {
        integral += (abs(sin(xNewValue)) + abs(sin(xNewValue - xValue))) * (xValue/2.0);
        xNewValue += xValue;
    }
    return integral;
    */
    for (int i = 1; i < trapNumb - 1; i++) {
        integral += sin(i * xValue);
    }
    integral = ((integral * 2) + sin(0) + sin(PI)) * (xValue/2.0);
    return integral;
}

double sinIntegralSimpson(int trapNumb)
{
    double xValue = PI/(double)trapNumb; // Value of each individual trap base
    double integral = 0;
    for (int i = 1; i < trapNumb - 1; i++) {
        if ( i % 2 == 0) // Even number
            integral += 2 * sin(i * xValue); // Even i's are multiplied by 2
        else
            integral += 4 * sin(i * xValue); // Odd i's are multiplied by 4
    }
    integral = (integral + sin(0) + sin(PI)) * (xValue/3.0);
    return integral;
}
