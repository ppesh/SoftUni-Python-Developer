// REPLACE ALL

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void findAndReplaceAll(string& text, string word, string replacement)
{
	// Get the first occurrence
	size_t pos = text.find(word);								// size_t: unsigned int type

	// Repeat till end is reached
	while (pos != string::npos)
	{
		// Replace this occurrence of Sub String
		text.replace(pos, word.size(), replacement);
		// Get the next occurrence from the current position
		pos = text.find(word, pos + replacement.size());
		/* 
		   string.length(): returns the length of the string, in terms of bytes
		   string.size(): returns the number of characters
		*/
	}
}

int main()
{
	string text, word, replacement;
	getline(cin, text);
	cin >> word;
	cin >> replacement;


	findAndReplaceAll(text, word, replacement);
	cout << text << endl;


	return 0;
}

