//PROBLEM 2 - PRODUCT SIGN

#include <iostream>
using namespace std;

int main()
{
	double x, y, z;
	cin >> x;
	cin >> y;
	cin >> z;

	double a[3] = {x, y, z};
	int n = 0;

	for (int i = 0; i < 3; i++) {
		if (a[i] < 0) {
			n++;
		}
		else if (a[i] == 0) {
			cout << "+" << endl;
			n = 5;
			break;
		}
	}

	if (n == 1 || n == 3) {
		cout << "-" << endl;
	}
	else if (n == 2) {
		cout << "+" << endl;
	}


	//cout << x << " " << y << " " << z << endl;

	

	return 0; 
}