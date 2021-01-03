// Odd Occurrences

#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main() {
    
    string str;
    getline(cin, str);

    stringstream ss;

    vector<pair <string, int>> myVector;
    
    ss << str;

    string temp;

    while (ss >> temp) {
        
        string lowString = "";
        bool is_exist = false;

        // превръщане в малки букви
        for (int i = 0; i < temp.size(); i++) {
            lowString += tolower(temp[i]);                  
            /* 
               tolower() converts input to its lowercase equivalent if input is an 
               uppercase letter and has a lowercase equivalent. If no such conversion 
               is possible, the value returned is input unchanged. 
            */
        }

        // проверка дали вече има подобен стринг
        for (int i = 0; i < myVector.size(); ++i) {
            if (myVector[i].first == lowString) {
                myVector[i].second++;                       // ако го има увеличавам втория пейр и брейквам, няма смисъл да продължавам да търся
                is_exist = true; break;
            }
        }
        if (is_exist == false) { 
            myVector.push_back(make_pair(lowString, 1)); 
        }   // ако го няма създавам нова двойка във вектора
    }

    // следва печат, не знам дали има друг метод, за добавяне на запетайки, без да се добави на последния елемент
    vector<string> outVector;   

    for (int i = 0; i < myVector.size(); i++) {
        if (myVector[i].second % 2 == 1) { 
            outVector.push_back(myVector[i].first);
        }
    }

    for (int i = 0; i < outVector.size() - 1; i++) {
        cout << outVector[i] << ", ";
    }

    cout << outVector[outVector.size() - 1] << endl;

}

 