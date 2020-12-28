//TASK 1 - COMPARE ARRAYS

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;

bool areEqual(int arr1[], int length1, int arr2[], int length2) {
	if (length1 != length2) {
		return false;
	}
	else {
		for (int i = 0; i < length1; i++) {
			if (arr1[i] != arr2[i]) {
				return false;
			}

		}
	}

	return true;
}

int main()
{
	int arr1[maxLength] = {};
	int length1;
	cin >> length1;

	for (int i = 0; i < length1; i++) {
		cin >> arr1[i];
	}


	int arr2[maxLength] = {};
	int length2;
	cin >> length2;

	for (int j = 0; j < length2; j++) {
		cin >> arr2[j];
	}

	if (areEqual(arr1, length1, arr2, length2) == 1) {
		cout << "equal" << endl;
	}
	else {
		cout << "not equal" << endl;
	}

	return 0; 
}