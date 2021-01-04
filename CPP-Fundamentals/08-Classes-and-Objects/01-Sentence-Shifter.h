// Sentence Shifter

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

class Sentence {
private:
    vector<string>sentence;
    int number = 0;

public:
    Sentence(vector<string>sentence_, int number_);
    void getShiftedSentence(vector<string> sentence);
};

Sentence::Sentence(vector<string>sentence_, int number_) :
    sentence(sentence_),
    number(number_)
    {}

void Sentence::getShiftedSentence(vector<string> sentence) {
    vector<string> shiftsen;
    int t = sentence.size(); 
    for (unsigned i = (t - number); i <= t - 1 ; i++) {
        shiftsen.push_back(sentence[i]);
    }

    for (unsigned i = 0; i < sentence.size() - number; i++) {
        shiftsen.push_back(sentence[i]);
    }

    for (unsigned i = 0; i < shiftsen.size(); i++) {
        cout << shiftsen[i] << endl;
    }
}


int main()
{
    string input_sentence;
    getline(cin, input_sentence);
    istringstream input(input_sentence);
    string word;
    vector<string> sentence;
    while (input >> word) {
        sentence.push_back(word);
    }

    int number;
    cin >> number;

    Sentence new_sentence(sentence, number);
    new_sentence.getShiftedSentence(sentence);

}