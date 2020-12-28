//PROBLEM 5 - MIN & MAX

#include <iostream>
#include <math.h>
#include <vector>
#include<algorithm>

using namespace std;


int main()
{
	int N, p;
	cin >> N;
	vector<int> v;

	for (int i = 1; i < N+1; i++) {
		cin >> p;
		v.push_back(p);
		//cout << p << " ";
	}
	

	cout << *min_element(v.begin(), v.end()) << " " << *max_element(v.begin(), v.end()) << endl;

	return 0; 
}