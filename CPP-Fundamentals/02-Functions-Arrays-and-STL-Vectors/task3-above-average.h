//TASK 3 - ABOVE AVERAGE 

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;

void AboveAverage(int arr[], int length)
{
	// Find average of array element 
	int sum = 0;
	for (int i = 0; i < length; i++)
		sum += arr[i];
	double ave = sum / length;

	// Print elements greater than average 
	for (int i = 0; i < length; i++)
		if (arr[i] >= ave)
			cout << arr[i] << " ";

	return;
}


	int main()
	{
		int arr[maxLength] = {};
		int length;
		cin >> length;
		int sum = 0;

		for (int i = 0; i < length; i++) {
			cin >> arr[i];
		}

		AboveAverage(arr, length);

		return 0;
	}
	
-------------------------------------------------------------------------------------

