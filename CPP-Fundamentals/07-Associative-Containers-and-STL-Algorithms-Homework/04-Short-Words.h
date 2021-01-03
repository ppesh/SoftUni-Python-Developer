// Short Words

#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
    string text;
    getline(cin, text);

    istringstream iss(text);

    string word;

    set<string> words;
   
    while (iss >> word) {
        if (word.size() < 5)
        {
            transform(word.begin(), word.end(), word.begin(), ::tolower);
            words.insert(word);
        }
    }

    if (words.size() > 0) {
        for (set<string>::iterator it = words.begin(); it != --words.end(); ++it) {			// it != --words.end(); - за да не се печата последния елемент
            cout << *it << ", ";
        }
        cout << *(--words.end());
    }



    return 0;
}