// MATHEMATICAL EXPRESSION

#include <iostream>
using namespace std;

int main()
{
    char array[100];
    int  i = 0, countB = 0, countBB = 0;        // B: Bracket (, BB: other Bracket )
    cin.getline(array, 100);

    while (array[i] != '\0')                    // '\0' is the null termination character. It marks the end of the string
    {
        if (array[i] == '(')
        {
            countB++;
        }
        else if (array[i] == ')')
        {
            countBB++;
        }

        i++;

    }

    if (countB == countBB)
    {
        cout << "correct";
    }
    else
    {
        cout << "incorrect";
    }
    return 0;
}