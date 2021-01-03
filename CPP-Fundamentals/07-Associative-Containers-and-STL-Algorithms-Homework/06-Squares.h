// Squares

#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>

using namespace std;

bool isPerfectSquare(long double x)
{
    // Find floating point value of square root of x. 
    long double sr = sqrt(x);

    // If square root is an integer 
    return ((sr - floor(sr)) == 0);
}

int main()
{
    string numbers;
    getline(cin, numbers);

    long double n;
    istringstream iss(numbers);

    multiset<int> squares;
   
    while (iss >> n) {
        if (isPerfectSquare(n)) {
            squares.insert(n);
        }
    }

    if (squares.size() > 0) {
        for (multiset<int>::reverse_iterator rit = squares.rbegin(); rit != --squares.rend(); ++rit) {     // it != --squares.end(); - за да не се печата последния елемент
            cout << *rit << " ";
        }
        cout << *(--squares.rend());
    }



    return 0;
}