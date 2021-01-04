// Distance

#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

class Distance {


    class Point1{
    public:
        float x1 = 0;
        float y1 = 0;
        
        Point1(float x1_, float y1_):
            x1(x1_),
            y1(y1_)
        {}
        
    };

    class Point2 {
    public:
        float x2 = 0;
        float y2 = 0;
        
        Point2(float x2_, float y2_):
            x2(x2_),
            y2(y2_)
        {}
        
    };

public:
    Point1 pt1;
    Point2 pt2;

    Distance(float x1, float y1, float x2, float y2):
        pt1(x1, y1),
        pt2(x2, y2)
    {}

    void getEuclDist();
};


void Distance::getEuclDist() {
    float dx = pt1.x1 - pt2.x2;
    float dy = pt1.y1 - pt2.y2;
    float res = sqrt(dx * dx + dy * dy);
    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(3);
    cout << res;
}


int main()
{
    float x1, y1, x2, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;

    Distance new_dist(x1, y1, x2, y2);
    new_dist.getEuclDist();
    
}