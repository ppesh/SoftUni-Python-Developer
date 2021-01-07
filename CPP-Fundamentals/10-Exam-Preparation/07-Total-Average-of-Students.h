// Total Average of Students

#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
 
class Student {
public:
    Student(string name, string surname, double average) : name(name), surname(surname), average(average) {};
    pair <string, double> getInfo() {
        ostringstream info;
        info << name << " " << surname << " " << average << endl;
        pair <string, double> result = make_pair(info.str(), this->average);
        return result;
    }
 
private:
    string name;
    string surname;
    double average;
};
 
 
int main() {
    int numberOfStudents;
    cin >> numberOfStudents;
    vector <Student> students;
    double totalGPA = 0;
    for (int i=0; i<numberOfStudents; ++i) {
        string name, surname;
        double average;
        cin >> name >> surname >> average;
        Student student(name, surname, average);
        students.push_back(student);
    }
    for (auto student : students) {
        pair <string, double> info = student.getInfo();
        cout << info.first << endl;
        totalGPA += info.second;
    }
    cout << totalGPA / numberOfStudents << endl;
 
    return 0;
}