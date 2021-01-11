// 04. Mayan Calculator

#include <iostream>
#include <string>
#include <map>
#include <vector>
 
using namespace std;
 
int main() {
    int lineCount;
    cin >> lineCount;
    cin.ignore();
    vector <string> lines;
    for (int i=0; i<lineCount; ++i) {
        string line;
        getline(cin, line);
        lines.push_back(line);
    }
    string number;
    cin >> number;
    for (int i=0; i<lineCount; ++i) {
        map <char, string> codes;
        int step = lines[i].length() / 10;
        for (int j=0; j<=9; ++j) {
            char idx = j + '0';
            codes[idx] = lines[i].substr(j*step, step);
        }
 
        for (char c : number) {
            cout << codes[c];
        }
        cout << endl;
 
    }
    return 0;
}