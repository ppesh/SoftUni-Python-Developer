// Shopping List

#include <iostream>
#include <vector>
#include <string>
#include <map>

struct items
{
    std::string itemName;
    double price;
    int count;
    double oneItemtotal;
};

int main()
{
    std::vector<items> item;
    double totalsum = 0;
    //std::map<std::string, double> oneItemtotal;
    //std::map<std::string, double>::iterator it = oneItemtotal.begin();
    int number;
    //std::cout << "Enter number of items : ";
    std::cin >> number;
    for (int i = 0; i < number; i++)
    {

        items temp;
        //        std::cout << "Enter the name of the item  :";
        std::cin >> temp.itemName;

        //        std::cout << "Enter the price  :";
        std::cin >> temp.price;

        //        std::cout << "Enter the count";
        std::cin >> temp.count;

        //        std::cout << "Enter average :";
        // std::cin >> average;
        //temp.Average = average;

        //totalprice= temp. count* temp.price;
        temp.oneItemtotal = temp.count * temp.price;
        item.push_back(temp);
        totalsum = totalsum + temp.oneItemtotal;

    }
    std::cout << "The total sum is: " << totalsum << " lv." << std::endl;
    // std::sort(oneItemtotal.begin(), oneItemtotal.end(), std::greater<double>());

      //sort(item.oneItemtotal.begin(), item.oneItemtotal.end());
     /*std::vector<items> sortitem;
     for( unsigned int i = 1 ; i < item.size(); i++ )
     {
             if( item.at(i-1).oneItemtotal >= item.at(i).oneItemtotal )
             {
                 sortitem.push_back(item.at(i-1));

             }

     }*/
    for (unsigned int i = 0; i < item.size(); i++) {
        for (unsigned int j = 0; j < item.size() - i - 1; j++) {
            if (item.at(j).oneItemtotal < item.at(j + 1).oneItemtotal) {
                items exchange = item[j];
                item[j] = item[j + 1];
                item[j + 1] = exchange;
            }
        }
    }

    //std::cout << std::endl;

    for (std::vector<items>::iterator it = item.begin(); it != item.end(); it++)
    {
        std::cout << it->itemName << ' ' << it->oneItemtotal << std::endl;
    }
    return 0;

}
   
