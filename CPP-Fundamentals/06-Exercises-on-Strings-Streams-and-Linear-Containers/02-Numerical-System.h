// Numeral System

#include <iostream>
#include <string>
#include <vector>

using namespace std;

string intToSystemNumber(const string baseInput, const int number)
{
	//abcdefghij
	//300
	string answer;
	string numberStr = to_string(number);				// to_string() returns a string with the representation of val.
	answer.resize(numberStr.size());					// resize() resizes the string to a length of n characters. 

	for (size_t i = 0; i < numberStr.size(); ++i)
	{
		const int index = numberStr[i] - '0';

		answer[i] = baseInput[index];
	}

	return answer;
}

int numberSystemToInt(const vector<int>& allValues, const string valueStr) // numberSystemToInt(abcdefghij, cba)
{
	int answer = 0;

	int multiplier = 1;

	const int SIZE = (int)valueStr.size();					// SIZE = 3
	for (int i = SIZE - 1; i >= 0; --i)						// i = 3 -1 = 2										i = 1				i = 0
	{
		const int index = valueStr[i];						// index = valueStr[2] = cba[2] = a = 97			index = 98			index = 99

		answer += (multiplier * allValues[index]);			// answer = 0 + (1 * abcdefghij[a]) = 0				answer = 10			answer = 210
		multiplier *= 10;									// multiplier = 1 									multiplier = 10		multiplier = 100
	}

	return answer;
}

int main()
{
	string baseInput;						// abcdefghij
	getline(cin, baseInput);

	string firstNumberStr;					// cba
	getline(cin, firstNumberStr);

	string secondNumberStr;					// ja
	getline(cin, secondNumberStr);

	vector<int> numberValues(255, 0);
	for (size_t i = 0; i < baseInput.size(); ++i)		// i = 0
	{
		//abcdefghij
		const unsigned char letter = baseInput[i];		// letter = baseInput[0] = a 

		numberValues[letter] = i;						// numberValues[a] = i = 0; 
		// vector[] - access element. Returns a reference to the element at position n in the vector container.
	}

	const int firstNumberInt = numberSystemToInt(numberValues, firstNumberStr);

	const int secondNumberInt = numberSystemToInt(numberValues, secondNumberStr);

	const int answerInt = firstNumberInt + secondNumberInt;

	//	cout << answerInt << endl;

	cout << intToSystemNumber(baseInput, answerInt);

	return 0;
}

