//TASK 6 - CLOSEST NUMBERS

#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdlib.h>

using namespace std;

const int maxLength = 100;


	int main()
	{
		int arr[maxLength] = {};

		int length;
		cin >> length;

		for (int i = 0; i < length; i++) {
			cin >> arr[i];
		}

        sort(arr, arr + length);

        int k = INT_MAX;
        int m;

        if (length > 1) {
            for (int i = 0; i < length - 1; i++) {
                m = abs(arr[i] - arr[i + 1]);

                if (m < k) {
                    k = m;
                }
            }
        }
        else if (length == 1) {
            //k = abs(arr[0]);
            k = 0;
        }
        cout << endl;
        cout << k << endl;

		return 0;
	}