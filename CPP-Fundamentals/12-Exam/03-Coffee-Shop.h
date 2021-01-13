// Coffee Shop

#include <iostream>
#include <vector>
#include <string>
#include <map>


using namespace std;

class Coffee
{
public:
    string name;
    double price;
    double rating;
   

public:
    //Coffee() {};
    Coffee(string name_, double price_, double rating_) :
        name(name_),
        price(price_),
        rating(rating_) {
    }

    // Methods:
    string addNew()
    {
        return name;
    }

    double getRating()
    {
        return rating;
    }

    double getPrice()
    {
        return price;
    }
};

// Functions:

vector<Coffee> changePrice(vector<Coffee> menu) {
    //vector<Coffee>::iterator it = menu.begin();
    for (unsigned i = 1; i < menu.size(); ++i)
    {
        double rate = menu.at(i).getRating();
        if (( rate>=4) && (rate <= 5.99)) {
            Coffee temp = menu.at(i);
            temp.price = 0.9 * temp.price;
            menu.at(i) = temp;
        }
    }
    return menu;
}


vector<Coffee> deleteDrinks(vector<Coffee> menu) {
    vector<Coffee> newmenu;
    for (int i = 0; i < menu.size(); ++i)
    {

        double rate = menu.at(i).getRating();
        if ( rate >=4) {
            newmenu.push_back(menu.at(i));
        }
    }
    menu = newmenu;
    return menu;
}



int main()
{
    int n;                                   // number of drinks
    cin >> n;

    vector<Coffee> menu;
    for (int i = 0; i < n; ++i) {
        string name;
        double price;
        double rating;

        cin >> name >> price >> rating;

        Coffee product(name, price, rating);
        menu.push_back(product);
    }

     menu= changePrice(menu);
     menu = deleteDrinks(menu);

    vector<Coffee>::iterator it = menu.begin();
    for (; it != menu.end(); ++it)
    {
        cout << it->addNew() << " " << it->price << " " << endl;
    }

    return 0;
}