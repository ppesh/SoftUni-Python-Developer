//PROBLEM 3 - QUADRATIC EQUATION

#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double a, b, c, d, x_1, x_2;
	cin >> a;
	cin >> b;
	cin >> c; 

	// cout << sqrt(a);

	d = b * b - 4 * a * c;

	if (d < 0) {
		cout << "no roots" << endl;
	}
	else if (d == 0) {
		x_1 = (-b + sqrt(d)) / (2 * a);
		x_2 = x_1;
		cout << x_1 << endl;
	}
	else {
		x_1 = (-b + sqrt(d)) / (2 * a);
		x_2 = (-b - sqrt(d)) / (2 * a);
		cout << x_1 << " " << x_2 << endl;
	}
	

	return 0; 
}