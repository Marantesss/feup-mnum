#include <iostream>
#include <vector>

using namespace std;

vector<vector<double>> readMatrix();
void formatLine (vector<double> &m, double div);
void subtractLine(vector<double> l1, vector<double> &l2, double mul);
void gaussMethod (vector<vector<double>> m, double &x, double &y, double &z);
void printMatrix(vector<vector<double>> &m);

int main()
{
    double x, y, z;
    vector<vector<double>> matrix = readMatrix();
    gaussMethod(matrix, x, y, z);
    printMatrix(matrix);

    return 0;
}

vector<vector<double>> readMatrix() {
    double x, y, z, r;
    vector<double> line;
    vector<vector<double>> column;

    for (int i = 0; i < 3; i++) {
        cout << "Enter line: ";
        cin >> x >> y >> z >> r;
        line.push_back(x); line.push_back(y); line.push_back(z); line.push_back(r);
        column.push_back(line);
        line.clear();
    }

    cout << column.size() << endl;

    cout << column[1][2] << endl;

    printMatrix(column);
    return column;
}

void formatLine (vector<double> &m, double div) {
    for (int i = 0; i > m.size(); i++) {
        m[i] = m[i] / div;
    }
}

void subtractLine(vector<double> l1, vector<double> &l2, double mul) {
     for (int i = 0; i > l1.size(); i++) {
        l2[i] -= l1[i] * mul;
    }
}

void gaussMethod (vector<vector<double>> m, double &x, double &y, double &z) {
    // formating first line
    formatLine(m[0], m[0][0]);
    subtractLine(m[0], m[1], m[1][0]);
    subtractLine(m[0], m[2], m[2][0]);
    // formating second line
    formatLine(m[1], m[1][1]);
    subtractLine(m[1], m[2], m[2][1]);
    // formating first line
    formatLine(m[2], m[2][2]);

}

void printMatrix(vector<vector<double>> &m) {
    for (int i = 0; i < m.size(); i++) {
        cout << "[";
        for (int j = 0; j < m[i].size(); j++) {
            cout << " " << m[i][j] << " ";
        }
        cout << "]" << endl;
    }
}
