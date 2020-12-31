// TITLE CASE 

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void capitalize(string& text)
{
	bool check;
	check = false;

	for (int i = 0; i < text.length(); i++)
	{
		if (check == false && (text.at(i) >= 'a' && text.at(i) <= 'z'))								// check if its a new word. 
			text.at(i) = text.at(i) + 'A' - 'a';													// check ASCII-table; 'a' at pos. 097, 'A' at pos 065 -> diff. = -32 (Space) -> turning small letter in to a capital one, from 032 to 065 - special symbols

		if ((text.at(i) >= 'a' && text.at(i) <= 'z') || (text.at(i) >= 'A' && text.at(i) <= 'Z'))	// you can also change this condition to check for a space in the string
			check = true;																			// if(str.at(i)!=' ')		
		else 																						// true... if character at i is an alphabet and false if not
			check = false;																			// it reiterates and changes the case of the next character depending on the condition
	}
}

int main()
{
	string text;
	getline(cin, text);

	capitalize(text);
	cout << text;


	return 0;
}