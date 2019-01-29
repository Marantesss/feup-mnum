A = [[3,-1,1],
     [1,4,2],
     [0,2,5]]

b = [[7],
     [4],
     [5]]

# Para metodos iterrativos e necessario cumprir certas condicoes -> o sistema tem que ser diagonalmente donimante

def diagDomin(A): # verifica se uma matrix e diagonalmente dominante
    i = 0
    for row in A:
        s = 0
        for j in row:
            if j != row[i]:
                s += j
        if (s > row[i]):
            return False
        i += 1
    return True

### Metodo de Gauss-Jacobi ###

def GaussJacobi(A, b):
    if not diagDomin(A):
        print("A matriz nao e diagonalmente dominante!")
        return

    # primeiro guess
    x = y = z = 0
    # para passar na primeira condicao que nao importa :)
    old_x = old_y = old_z = 1
    iteration = 1
    row = 0
    while abs(x - old_x) > 1e-7 or abs(y - old_y) > 1e-7 or abs(z - old_z) > 1e-7:
        print(str(iteration))
        old_x = x
        old_y = y
        old_z = z
        x = (b[row][0] - A[row][1]*old_y - A[row][2]*old_z) / float(A[row][row])
        row += 1
        y = (b[row][0] - A[row][0]*old_x - A[row][2]*old_z) / float(A[row][row])
        row += 1
        z = (b[row][0] - A[row][0]*old_x - A[row][1]*old_y) / float(A[row][row])
        row = 0
        iteration += 1
        print("x: " + str(x) + "\ty: " +  str(y) + "\tz: " + str(z))

def GaussSeidal(A, b):
    if not diagDomin(A):
        print("A matriz nao e diagonalmente dominante!")
        return

    # primeiro guess
    x = y = z = 0
    # para passar na primeira condicao que nao importa :)
    old_x = old_y = old_z = 1
    iteration = 1
    row = 0
    while abs(x - old_x) > 1e-7 or abs(y - old_y) > 1e-7 or abs(z - old_z) > 1e-7:
        print(str(iteration))
        old_x = x
        old_y = y
        old_z = z
        x = (b[row][0] - A[row][1]*old_y - A[row][2]*old_z) / float(A[row][row])
        row += 1
        y = (b[row][0] - A[row][0]*x - A[row][2]*old_z) / float(A[row][row])
        row += 1
        z = (b[row][0] - A[row][0]*x - A[row][1]*y) / float(A[row][row])
        row = 0
        iteration += 1
        print("x: " + str(x) + "\ty: " +  str(y) + "\tz: " + str(z))

print("Gauss-Jacobi")
GaussJacobi(A,b)
print("Gauss-Seidal")
GaussSeidal(A,b)

'''Output
1
x: 2.33333333333        y: 1.0  z: 1.0
2
x: 2.33333333333        y: -0.0833333333333     z: 0.6
3
x: 2.10555555556        y: 0.116666666667       z: 1.03333333333
4
x: 2.02777777778        y: -0.0430555555556     z: 0.953333333333
5
x: 2.0012037037 y: 0.0163888888889      z: 1.01722222222
6
x: 1.99972222222        y: -0.00891203703704    z: 0.993444444444
7
x: 1.99921450617        y: 0.00334722222222     z: 1.00356481481
8
x: 1.99992746914        y: -0.00158603395062    z: 0.998661111111
9
x: 1.99991761831        y: 0.000687577160494    z: 1.00063441358
10
x: 2.00001772119        y: -0.000296611368313   z: 0.999724969136
11
x: 1.9999928065 y: 0.000133085133745    z: 1.00011864455
12
x: 2.00000481353        y: -5.75238983197e-05   z: 0.999946765947
13
x: 1.99999857005        y: 2.54136445473e-05    z: 1.00002300956
14
x: 2.00000080136        y: -1.11472925955e-05   z: 0.999989834542
15
x: 1.99999967272        y: 4.88238847457e-06    z: 1.00000445892
16
x: 2.00000014116        y: -2.14763895445e-06   z: 0.999998047045
17
x: 1.99999993511        y: 9.41188408488e-07    z: 1.00000085906
18
x: 2.00000002738        y: -4.13304160451e-07   z: 0.999999623525
19
x: 1.99999998772        y: 1.81393279453e-07    z: 1.00000016532
20
x: 2.00000000536        y: -7.95917658447e-08   z: 0.999999927443
21
x: 1.99999999766        y: 3.49393546872e-08    z: 1.00000003184
22
x: 2.00000000103        y: -1.53321487728e-08   z: 0.999999986024
Gauss-Seidal
1
x: 2.33333333333        y: 0.416666666667       z: 0.833333333333
2
x: 2.19444444444        y: 0.0347222222222      z: 0.986111111111
3
x: 2.0162037037 y: 0.00289351851852     z: 0.998842592593
4
x: 2.00135030864        y: 0.00024112654321     z: 0.999903549383
5
x: 2.00011252572        y: 2.00938786009e-05    z: 0.999991962449
6
x: 2.00000937714        y: 1.67448988342e-06    z: 0.999999330204
7
x: 2.00000078143        y: 1.39540823618e-07    z: 0.999999944184
8
x: 2.00000006512        y: 1.16284020191e-08    z: 0.999999995349
9
x: 2.00000000543        y: 9.69033520093e-10    z: 0.999999999612
'''
