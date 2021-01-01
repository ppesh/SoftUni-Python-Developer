// Merge Trains

#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>           // last-in, first-out structure
#include <queue>

using namespace std;


    int main(){

        list<int> railcarA;
        int input;
        while ((cin >> input) && (cin.get() != '\n')) {      
            railcarA.push_back(input);
        }
        railcarA.push_back(input);

        list<int> railcarB;
        while ((cin >> input) && (cin.get() != '\n')) {
            railcarB.push_back(input);
        }
        railcarB.push_back(input);
        

        stack<int> train;
        priority_queue<char> AB_sequence;

        
        //railcarA.merge(railcarB);
        //railcarA.sort();

        
        for (int i : railcarA) { 
            train.push(i); 
        }

        for (int i : railcarB) { 
            train.push(i); 
        }
        
        
        while (!train.empty()) {
            if (find(railcarA.begin(), railcarA.end(), train.top()) != railcarA.end()) {
                AB_sequence.push('A');
            }
            else {
                AB_sequence.push('B');
            }
            train.pop();
        }
        

        while (!AB_sequence.empty()) {
            cout << AB_sequence.top();
            AB_sequence.pop();
        }

        while (!train.empty()) {
            int t = train.top();
            cout << t;
            train.pop();
        }
        


       /* merge(railcarA.begin(), railcarA.end(), railcarB.begin(), railcarB.end(), train.begin());

        sort(train.begin(), train.end(), greater<int>());

        for (auto n : train) {
            cout << n << " "; 
        }*/

        return 0;
    }