// INVALID OUTPUT 

#include <iostream>
#include <string>
#include <vector>
//#include <regex>
 
using namespace std;
 
//bool isNumber( std::string token ) {
//    return regex_match( token, regex( ( "((\\+|-)?[[:digit:]]+)(\\.(([[:digit:]]+)?))?" )));
//}
 
vector<string> split(const string& str, const string& delimiter) {
    vector<string> tokens;
    size_t prev = 0, pos = 0;
    do {
        pos = str.find(delimiter, prev);
        if (pos == string::npos) pos = str.length();
        string token = str.substr(prev, pos-prev);
        if (!token.empty()) tokens.push_back(token);
        prev = pos + delimiter.length();
    } while (pos < str.length() && prev < str.length());
    return tokens;
}
 
int main() {
    string input;
    getline(cin, input);
 
    string delimiter = " ";
 
    vector<string> vecStr = split(input, delimiter);
    vector<string> vecOut;
    double theSum = 0;
 
    for (string s : vecStr) {
        try {
            theSum += stod(s);
        }
        catch (exception& e) {
            vecOut.push_back(s);
        }
    }
//
//    for (string s : vecStr) {
//        if (isNumber(s)) {
//            theSum += stod(s);
//        } else {
//            vecOut.push_back(s);
//        }
//    }
 
    cout << theSum << endl;
 
    for (string s : vecOut) {
        cout << s << " ";
    }
 
    return 0;
}