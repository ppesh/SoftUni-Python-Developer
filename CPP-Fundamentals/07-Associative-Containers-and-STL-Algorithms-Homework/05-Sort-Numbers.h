// Sort Numbers

// try:
// std::set<double> numbers;

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

    int number;

    vector<int> numbersVec;

    while (lineStream >> number) {
        numbersVec.push_back(number);
    }

    sort(numbersVec.begin(), numbersVec.end());

    for (vector<int>::iterator it = numbersVec.begin(); it != numbersVec.end() - 1; ++it) {
        cout << *it << " <= ";
    }

    cout << *(numbersVec.end() - 1) << endl;

    return 0;
}