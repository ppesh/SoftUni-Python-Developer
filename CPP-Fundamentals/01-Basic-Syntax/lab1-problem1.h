//PROBLEM ONE - ORDER TWO NUMBERS

#include <iostream>
using namespace std;

int main()
{
	int x, y;
	//cout << "Enter two numbers" << endl;
	cin >> x;
	cin >> y;

	if (x > y) {
		cout << y << " " <<  x << endl;
	}
	else {
		cout << x << " " << y << endl;
	}

	return 0; 
}