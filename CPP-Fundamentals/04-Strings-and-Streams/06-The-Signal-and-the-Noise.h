// THE SIGNAL AND THE NOISE

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

/*
void print(vector <int> const& a) {
    cout << "The vector elements are : ";

    for (int i = 0; i < a.size(); i++)
        cout << a.at(i) << ' ';
}
*/

/*bool isNoise(char symbol) {
    
        if ((isdigit(symbol) == false )&& (isspace(symbol) == false)) {
            return true;
        }
        else {
            return false;
        }
    
}*/



int extractMaximum(string str)
{
    int num = 0, res = 0;

    for (int i = 0; i < str.length(); i++)
    { 
        if (str[i] >= '0' && str[i] <= '9')         // If a num value comes, start converting it into an int till there are consecutive num digits
            num = num * 10 + (str[i] - '0');
        else
        {
            res = max(res, num);
            num = 0;
        }
    }

    return max(res, num);
}

int main()
{
    string input;
    getline(cin, input);

    /*for (char ch : input) {
        if (isNoise(ch) == true) {

            input.erase(remove(input.begin(), input.end(), ch), input.end());
            //input.erase(input.find(ch), 1);
        }
        }*/

    string numstr="";
    for (unsigned i=0; i<input.length(); ++i) {
        if (isdigit(input.at(i))||isspace(input.at(i))) {
            
            numstr.push_back(input.at(i));
        }
    }


    //cout << input<<\n;
    //cout << numstr;

    cout << extractMaximum(numstr);
    

	return 0;
}