// Brackets

#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>           
#include <queue>

using namespace std;

int main()
{
    stack<char> brackets;
    string input;

    getline(cin, input);

    bool isValid = true;

    for (char i : input)
    {
        switch (i)
        {
        case '(':
            brackets.push(')');
            break;
        case '{':
            brackets.push('}');
            break;
        case '[':
            brackets.push(']');
            break;
        case ')':
        case '}':
        case ']':
            if (brackets.empty() || brackets.top() != i)
            {
                isValid = false;
            }
            else
            {
                brackets.pop();
            }
            break;
        default:
            break;
        }

        if (!isValid)
        {
            break;
        }
    }

    if (isValid && brackets.empty())
    {
        cout << "valid" << endl;
    }
    else
    {
        cout << "invalid" << endl;
    }

    return 0;
}