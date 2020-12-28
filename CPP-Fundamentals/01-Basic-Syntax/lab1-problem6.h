//PROBLEM 6 - GREATEST COMMON DIVISOR

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;


int main()
{
	int x, y;
	cin >> x;
	cin >> y;

	int m = min(x, y);
	int GCD = 1;

	for (int i = 1; i <= m; i++) {
		if (x % i == 0 && y % i == 0) {
			GCD = max(GCD, i);
		}
	}

	cout << GCD;

	return 0; 
}