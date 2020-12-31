// The Noise and the Signal

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

int main()
{
    string input;
    getline(cin, input);

    string noisestr = ""; 
    int charnum = 0;

    for (unsigned i = 0; i < input.length(); ++i) {
        if (!isdigit(input.at(i))) {
            noisestr.push_back(input.at(i));
        }
    }
    // is only digit and space
    if (noisestr.find_first_not_of(" ")==string::npos)
      cout << "no noise";
    else{
  
    int findid = 0; string noise1, string2, noise2; int firstspc1, firstspc2=0, length2, length1, noiseleng = 0, totallength = 0;
    bool loop = true;
    while (loop) {
        int condition1 = (noisestr.find(" ", findid) == string::npos);
        if (noisestr.find(" ", findid+1) == string::npos) {// when there is no space in the first string
            noise1 = noisestr.substr(findid, noisestr.length());
            loop = false;
        }       
            
        else {
            firstspc1 = noisestr.find(" ", findid);
            
            string string1 = noisestr.substr(findid, firstspc1 - findid);
            length1 = string1.length();
            totallength = totallength + length1;
            int condition2 = (noisestr.find(" ", firstspc1+1) == string::npos);


            if (noisestr.find(" ", firstspc1+1) == string::npos) {//when the second string can not be found
                string2 = noisestr.substr(firstspc1 + 1, noisestr.length());
                length2 = string2.length();
                loop = false;
            }
            else {
                firstspc2 = noisestr.find(" ", firstspc1 + 1);
                string2 = noisestr.substr(firstspc1 + 1, firstspc2 - firstspc1 - 1);
                length2 = string2.length();
            }

            findid = firstspc2 + 1;
            //assume length1 is the bigger one

            //get the noise between current two strings :noise1
            if (length1 < length2) {
                noise1 = string2;
            }      
            else if ((length1 == length2)) {

                if (string1 > string2)
                    noise1 = string2;
                else
                    noise1 = string1;
            }
            else {
                noise1 = string1;
            }
        }
       
        //the current noise with previous  
        if (noise1.length() > noise2.length())
            noise2 = noise1;
        else if (noise1.length() == noise2.length()) {
            if (noise1 > noise2)
                noise2 = noise2;
            else
                noise2 = noise1;
        }
        else
            noise2 = noise2;

    }
    
    cout << noise2;
    }
	return 0;
}