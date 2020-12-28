//TASK 5 - CARTESIAN PRODUCT

#include <iostream>
#include <vector>
using namespace std;

const int maxLength = 100;

int main() {
	int arr[maxLength] = {};

	int length;
	cin >> length;

	int r;
	for (int i = 0; i < length; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i < length; i++) {
		for (int j = 0; j < length; j++) {
			int r = arr[i] * arr[j];
			cout << r <<" ";
		}
	}

    return 0;
}