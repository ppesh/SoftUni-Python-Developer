// Compare Arrays Again

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;


int main()
{

	vector<int>arr1;
	int input1;
	while ((cin >> input1) && (cin.get() != '\n')) {      // push_back in and outside of the array because when the while-condition is not fullfilled the last number is not pushed back
		arr1.push_back(input1);
	}
	arr1.push_back(input1);

		
	vector<int>arr2;
	int input2;
	
	while ((cin >> input2) && (cin.get() != '\n')) {
		arr2.push_back(input2);
	}
	arr2.push_back(input2);
	if (arr1 == arr2) {
		cout << "equal" << endl;
	}
	else {
		cout << "not equal" << endl;
	}

	return 0;
}