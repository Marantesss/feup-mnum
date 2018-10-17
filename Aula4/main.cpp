#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <fstream>

using namespace std;

const float PI = acos(-1);

float f(float x)
{
    return sin(x);
}

float trapezios(float x1, float x2, int nmax)
{
    float sum = 0;
    float h = (x2-x1)/nmax;
    for (unsigned int n = 1; n < nmax; n++)
    {
        sum += f(x1 + n*h);
    }
    sum *= 2;
    sum += f(x1)+f(x2);
    return h/2*sum;
}

void printTrapezios(float x1, float x2, vector<int> iterations)
{
    ofstream outStream;
    outStream.open("C:\\Users\\gonca\\Desktop\\MNUM-Aula4\\Errors.txt");
    for (unsigned int n = 0; n < iterations.size(); n++)
    {
        float value = trapezios(x1, x2, iterations.at(n));
        outStream << setprecision(8) << abs(2-value) << endl;
    }
    outStream << endl;
}

float SimpsonsRule(float x1, float x2, int nmax)
{
    float sum = f(x1)+f(x2);
    float h = (x2-x1)/nmax;
    for (unsigned int n = 1; n < nmax; n+=2)
    {
        sum += 4*f(x1 + n*h) + 2*f(x1 + (n+1)*h);
    }
    return h/3*sum;
}

void printSimpsonsRule(float x1, float x2, vector<int> iterations)
{
    ofstream outStream;
    outStream.open("C:\\Users\\gonca\\Desktop\\MNUM-Aula4\\Errors.txt");
    for (unsigned int n = 0; n < iterations.size(); n++)
    {
        float value = SimpsonsRule(x1, x2, iterations.at(n));
        outStream << setprecision(8) << abs(2-value) << endl;
    }
}

float controloErroTrap(float lower, float upper, float a, float b, float c)
{
    float s = trapezios(lower, upper, a);
    float sl = trapezios(lower, upper, b);
    float sll = trapezios(lower, upper, c);
    return (sl-s)/(sll-sl);
}

float controloErroSimp(float lower, float upper, float a, float b, float c)
{
    float s = SimpsonsRule(lower, upper, a);
    float sl = SimpsonsRule(lower, upper, b);
    float sll = SimpsonsRule(lower, upper, c);
    return (sl-s)/(sll-sl);
}

float ErroTrap(float lower, float upper, float a, float b, float c)
{
    float sl = trapezios(lower, upper, b);
    float sll = trapezios(lower, upper, c);
    return (sll-sl)/(4-1);
}

float ErroSimp(float lower, float upper, float a, float b, float c)
{
    float sl = SimpsonsRule(lower, upper, b);
    float sll = SimpsonsRule(lower, upper, c);
    return (sll-sl)/(16-1);
}

int main()
{
    float lower = 0, upper = PI;
    vector<int> iterations = {2,4,8,10,12,20,24,40,48};

    //printTrapezios(lower, upper, iterations);
    //printSimpsonsRule(lower, upper, iterations);
    //Trapezios
    cout << "2 4 8 - Ordem: " << setprecision(8) << controloErroTrap(lower, upper, 2, 4, 8) << ";  Erro: " << ErroTrap(lower, upper, 2, 4, 8) << endl;
    cout << "10 20 40 - Ordem: " << setprecision(8) << controloErroTrap(lower, upper, 10, 20, 40) << ";  Erro: " << ErroTrap(lower, upper, 10, 20, 40) << endl;
    cout << "12 24 48 - Ordem:  " << setprecision(8) << controloErroTrap(lower, upper, 12, 24, 48) << ";  Erro: " << ErroTrap(lower, upper, 12, 24, 48) << endl;
    cout << "trap(48) = " << trapezios(lower, upper, 48);
    //Simpsons
    cout << endl;
    cout << "2 4 8 - Ordem: " << setprecision(8) << controloErroSimp(lower, upper, 2, 4, 8) << ";  Erro: " << ErroTrap(lower, upper, 2, 4, 8) << endl;
    cout << "10 20 40 - Ordem: " << setprecision(8) << controloErroSimp(lower, upper, 10, 20, 40) << ";  Erro: " << ErroTrap(lower, upper, 10, 20, 40) << endl;
    cout << "12 24 48 - Ordem: " << setprecision(8) << controloErroSimp(lower, upper, 12, 24, 48) << ";  Erro: " << ErroTrap(lower, upper, 12, 24, 48) << endl;
    cout << "simp(48) = " << SimpsonsRule(lower, upper, 48);
    return 0;
}
