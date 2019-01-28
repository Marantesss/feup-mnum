#include <iostream>

using namespace std;

double funcao(double x, double y) {
    return x * y;
}

double simpsonsFormula (double hx, double hy, double sum0, double sum1, double sum2) {
    return ((hx*hy)/9.0)*(sum0+4*sum1+16*sum2);
}

double calculateH(double a, double b) {
    return (b - a)/2.0;
}

int main() {
    // Limits of the two integrals
    double xLimInf = 0, xLimSup = 1;
    double yLimInf = 0, yLimSup = 1;
    // Calculating h's
    double hx =  calculateH(xLimInf, xLimSup);
    double hy =  calculateH(yLimInf, yLimSup);
    // Calculating sums
    double sum0 = funcao(xLimInf, yLimInf) + funcao(xLimInf, yLimSup) + funcao(xLimSup, yLimInf) + funcao(xLimSup, yLimSup);
    double sum1 = funcao(xLimInf, yLimInf + hy) + funcao(xLimInf + hx, yLimSup) + funcao(xLimInf + hx, yLimInf) + funcao(xLimSup, yLimInf + hy);
    double sum2 = funcao(xLimInf + hx, yLimInf + hy);
    // Applying the formula
    cout << simpsonsFormula(hx,hy,sum0,sum1,sum2) << endl;

    return 0;
}
