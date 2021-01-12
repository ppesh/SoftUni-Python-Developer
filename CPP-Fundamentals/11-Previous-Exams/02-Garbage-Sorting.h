// 02. Garbage Sorting

#include <iostream>
#include<vector>
#include <list>
 
using namespace std;
 
int main()
{
    list<int>glass;
    list<int>metal;
    list<int>plastic;
 
    int n=0;
    cin >> n;
   
    int number = 1;
    for (int i = 1; i <= n; i++)
    {
        string first ="";
        string second="";
        cin >> first;
        cin >> second;
       
   
 
    if (first == "glass")
    {
        if (second == "front")
        {
            glass.push_front(number);
        }
        else
        {
            glass.push_back(number);
        }
    }
    else if (first == "metal")
    {
        if (second == "front")
        {
            metal.push_front(number);
        }
        else
        {
            metal.push_back(number);
        }
    }
    else if (first == "plastic")
    {
        if (second == "front")
        {
            plastic.push_front(number);
        }
        else
        {
            plastic.push_back(number);
        }
 
    }
    else
    {
        number--;
    }
    number++;
 
  }//for
    if (glass.size() >= 1)
    {
        cout << "glass - ";
    }
    for (auto it = glass.begin(); it != glass.end(); ++it)
        cout << *it << ' ';
    cout << endl;
 
    if (metal.size() >= 1)
    {
        cout << "metal - ";
    }
    for (auto it = metal.begin(); it != metal.end(); ++it)
        cout  << *it << ' ';
    cout << endl;
 
    if (plastic.size() >= 1)
    {
        cout << "plastic - ";
    }
    for (auto it = plastic.begin(); it != plastic.end(); ++it)
        cout << *it << ' ';
}