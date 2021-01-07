// Students Information

using namespace std;
 
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
 
class Students
{
private:
    string firstName;
    string surname;
    double grade;
 
public:
 
    Students(string firstName_ , string surname_ , double grade_ ) :
        firstName(firstName_),
        surname(surname_),
        grade(grade_)
        {}    
 
        string getFirstName()
        {
            return firstName;
        }
        string getSurname()
        {
            return surname;
        }
        double getgrade()
        {
            return grade;
        }
};
 
 
int main(){
 
    vector<Students> studInfo;
 
    int numOfIter;
    cin >> numOfIter;
 
    for (int i = 0; i < numOfIter; ++i)
    {
        string firstNameOfStud;
        string surnameOfStud;
        double gradeOfStud;
        cin >> firstNameOfStud >> surnameOfStud >> gradeOfStud;
 
        studInfo.push_back(Students(firstNameOfStud, surnameOfStud, gradeOfStud));
    }
	
    vector<Students>::iterator it = studInfo.begin();
    for (; it != studInfo.end(); ++it)
    {
        cout << it->getFirstName() << " " << it->getSurname() << " " << it->getgrade() << endl;
    }
	
 
    return 0;
}