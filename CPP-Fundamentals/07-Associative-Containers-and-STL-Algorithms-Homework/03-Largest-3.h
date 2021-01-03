// Largest 3

// try:
// std::set<double, std::greater<double>> numbers;

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string line;
    getline(cin, line);

    istringstream lineStream(line);

    double number;

    vector<double> numbersVec;

    while (lineStream >> number) {
        numbersVec.push_back(number);
    }

    sort(numbersVec.begin(), numbersVec.end());
    reverse(numbersVec.begin(), numbersVec.end());

    
    if (numbersVec.size() < 3) {
        for (vector<double>::iterator it = numbersVec.begin(); it != numbersVec.end() - 1; ++it) {

            cout << *it << " ";
        }
        cout << *(numbersVec.end() - 1) << endl;
    } 
    else {
        for (vector<double>::iterator it = numbersVec.begin(); it != numbersVec.begin() + 3; ++it) {

            cout << *it << " ";
        }
    }
    
    

    return 0;
}