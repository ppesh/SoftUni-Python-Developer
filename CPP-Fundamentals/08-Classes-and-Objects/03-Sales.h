// Sales

#include <iostream>
#include <string>
#include <map>
#include <iomanip>
#include<sstream>

using namespace std;

class sales
{
private:
    string city;
    string productType;
    double price;
    double quantity;
    map<string, double> citiesAndPrice;

public:
    //========================
    //initializer constructor
    //========================
    sales(string city_, string productType_, double price_, double quantity_);


    //========================
    //Methods
    //========================
    void setCity(string cityName);
    void setProduct(string product);
    void setprice(double priceProduct);
    void setquantity(double quantityProduct);
    void calculateProducts();
    string print();
};

void sales::setCity(string cityName)
{
    city = cityName;
}
void sales::setProduct(string product)
{
    productType = product;
}
void sales::setprice(double priceProduct)
{
    price = priceProduct;
}
void sales::setquantity(double quantityProduct)
{
    quantity = quantityProduct;
}

sales::sales(string city_, string productType_, double price_, double quantity_) :
    city(city_),
    productType(productType_),
    price(price_),
    quantity(quantity_)
{}

void sales::calculateProducts()
{
    double finalResult = price * quantity;
    citiesAndPrice[city] += finalResult;
}

string sales::print()
{
    ostringstream info;
    for (auto x : citiesAndPrice)
    {
        info << x.first << fixed << setprecision(2) << " -> " << x.second << endl;
    }
    return info.str();
}

int main()
{
    int numbers;
    cin >> numbers;
    string cityname;
    string productType;
    double price;
    double quantity;

    sales sale(cityname, productType, price, quantity);

    for (int i = 0; i < numbers; ++i)
    {
        cin >> cityname >> productType >> price >> quantity;
        cout << endl;
        sale.setCity(cityname);
        sale.setProduct(productType);
        sale.setprice(price);
        sale.setquantity(quantity);
        sale.calculateProducts();
    }
    cout << sale.print();

    return 0;
}