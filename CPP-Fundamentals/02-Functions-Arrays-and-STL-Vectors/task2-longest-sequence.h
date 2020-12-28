//TASK 2 - LONGEST SEQUENCE 

#include <iostream>
#include <vector>
 
using namespace std;
 
int main()
{
    int lenght;
    cin >> lenght;
    vector<int> vec = { 0 }; 
    int bestSequence = 0;
    int currentSequence = 0;
    int numberSequence = 0;
    for (int i = 0; i < lenght; i++)
    {
        int currentNum;
        cin >> currentNum;
        if (i == 0)
        {
            vec[i] = currentNum;
        }
        else
        {
            vec.push_back(currentNum);
        }
    }
    for (int i = 0; i < lenght - 1; i++)
    {
        if (vec[i] == vec[i + 1])
        {
            currentSequence++;
        }
        else
        {
            currentSequence = 0;
        }
        if (currentSequence >= bestSequence)
        {
            bestSequence = currentSequence;
            numberSequence = vec[i];
        }
    }
    if (bestSequence == 0)
    {
        numberSequence = vec[lenght - 1];
    }
    for (int i = 0; i <= bestSequence; i++)
    {
        cout << numberSequence << " ";
    }
 
    return 0;
}

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;

void getLongestSeq(int arr1[], int length1) {
	int maxTime = 1;		//the number of elements in a sequence 
	int max1 = arr1[0];		//current detected element in the sequence with most numbers
	int max2 = arr1[1];		//current element to test sequence
	int num = 1;			//count num

	for (int i = 0; i < length1; i++) {
		if (arr1[i] == max2) {
			num++;
			if (num >= maxTime) {
				maxTime = num;
				max1 = max2;
				max2 = arr1[i];
			}
		else {
			max2 = arr1[i];
			num = 1;
			}
	}

	if (maxTime > 1) {
		for (int k = 0; k < maxTime; k++) {
			cout << max1 << " " << endl;
		}
	}
	else {
		cout << arr1[length1-1] << endl;
	}

	return;

}

	


int main()
{
	int arr1[maxLength] = {};
	int length1;
	cin >> length1;

	for (int i = 0; i < length1; i++) {
		cin >> arr1[i];
	}


	getLongestSeq(arr1, length1);
	


	return 0; 
}



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;



int main()
{
	int arr1[maxLength] = {};
	int length1;
	cin >> length1;

	for (int i = 0; i < length1; i++) {
		cin >> arr1[i];
	}

	vector<int> seq;
	int count;

	for (int i = 0; i < length1; i++) {
		if (arr1[i] == arr1[i + 1]) {
			seq.push_back(arr1[i]);
			seq.push_back(arr1[i + 1]);
			count = sizeof(seq);
		}
		else {

		}
	}
	




	return 0; 
}





----------------------------------------------------------------------------------------------------------------------------------------------------------------



#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;

void getLongestSeq(int arr1[], int length1) {
	int maxIdx = 0, maxLen = 0, currIdx = 0, currLen = 0; 

	for (int k = 0; k < length1; k++) {
		if (arr1[k] == arr1[k+1]) {
			currLen++;
			currIdx = k;
				/*if (currLen > maxLen) {
					maxLen = currLen;
					maxIdx = currIdx;
				}*/
		}
		
	}

	if (currLen > 0) {
		cout << currLen << endl;
		cout << currIdx << endl;
		//cout << maxLen << endl;
		//cout << maxIdx << endl;
	}

	return;

}

	


int main()
{
	int arr1[maxLength] = {};
	int length1;
	cin >> length1;

	for (int i = 0; i < length1; i++) {
		cin >> arr1[i];
	}


	getLongestSeq(arr1, length1);
	


	return 0; 
}



----------------------------------------------------------------------------------------------------------------------------------------------------------


#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;

const int maxLength = 100;

void getLongestSeq(int arr1[], int length1) {
	int maxTime = 1, preElement = arr1[0], num = 0, ele = arr1[0]; 

	/* maxTime: length of a seq of same elements  
	   preElement: previous element in the array
	   num: the number of times one element repeats, for example [2 2 2] - 2 repeats 3 times*/

	for (int i = 1; i < length1; i++) {
		if (arr1[i] == preElement) {
			num++;
			//maxTime = max(maxTime, num);
			if (maxTime > num) {
				ele = preElement;
			}
			else if (maxTime < num) {
				maxTime = num;
			}
			else {
				ele = preElement;
			}
		}
		else {
			preElement = arr1[i];
			num = 0;
		}
	}

	
	if (maxTime > 1) {
		for (int k = 0; k < maxTime + 1; k++) {
			cout << ele << " " << endl;
		}
	}
	

	return;

}

	


int main()
{
	int arr1[maxLength] = {};
	int length1;
	cin >> length1;

	for (int i = 0; i < length1; i++) {
		cin >> arr1[i];
	}


	getLongestSeq(arr1, length1);
	


	return 0; 
}