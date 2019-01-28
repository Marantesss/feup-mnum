#include <iostream>
#include <iomanip>

using namespace std;

double fl(double x, double y) {
    return x + y;
}

void runge_kutta2(double h, double xn, double yn, double &xn1, double &yn1) {
    //1
    double yl = fl(xn, yn);

    //2
    double yll = fl(xn + h/2.0, yn + (h/2.0)*yl);

    //3
    yn1 = yn + h * yll;
    xn1 = xn + h;

    /* Or just this
    yn1 = yn + h * fl(xn + h/2.0, yn + (h/2.0)*fl(xn, yn));
    xn1 = xn + h;
    */
}

void runge_kutta4(double h, double xn, double yn, double &xn1, double &yn1) {
    //1
    double dy1 = h * fl(xn, yn);
    double dy2 = h * fl(xn + h/2.0, yn + dy1/2.0);
    double dy3 = h * fl(xn + h/2.0, yn + dy2/2.0);
    double dy4 = h * fl(xn + h, yn + dy3);

    //2
    yn1 = yn + (1/6.0)*dy1 + (1/3.0)*dy2 + (1/3.0)*dy3 + (1/6.0)*dy4;
    xn1 = xn + h;
}

int main() {
    double xn1, yn1;
    runge_kutta2(1,0,0,xn1, yn1);
    cout << "xn1 = " << fixed << setprecision(6) << xn1 << endl << "yn1 = " << fixed << setprecision(6) << yn1 << endl << endl;
    runge_kutta4(1,0,0,xn1, yn1);
    cout << "xn1 = " << fixed << setprecision(6) << xn1 << endl << "yn1 = " << fixed << setprecision(6) << yn1 << endl << endl;

    return 0;
}
