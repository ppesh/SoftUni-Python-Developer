// Area and Perimeter of a Rectangle

#include<iostream>
 
using namespace std;
class Rectangle
{
private:
    int a;
    int b;
 
public:
    Rectangle() {};
    Rectangle(int a_, int b_)
    {
        a = a_;
        b = b_;
    }
    int GetArea()
    {
        return a * b;
    }
    int GetPerimeter()
    {
        return (2 * (a + b));
    }
 
};
 
int main()
{
    int a, b;
    cin >> a >> b;
    Rectangle rec(a,b);
    cout << rec.GetArea() << endl;
    cout << rec.GetPerimeter() << endl;
   
 
    return 0;
}