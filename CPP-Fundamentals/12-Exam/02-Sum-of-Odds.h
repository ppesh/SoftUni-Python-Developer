// Sum of Odds

#include<iostream>
int main()


{
    const int n = 100;
    unsigned int matrix[n][n];
    int size = 0;
  //  std::cout << "size : " ;
    std::cin >> size;

    for ( int i = 0; i < size; i++)
    {
        for ( int j = 0; j < size; j++)
        {
           // std::cout << "matrix["<<i<<"]["<<j<<"]= ";
            std::cin >> matrix[i][j];
        }
    }


    int sum = 0;
    for ( int i = 0; i < size; i++)
    {
        for ( int j = 0; j < size; j++)
        {
           if ( (i != j) && (i+j!=size-1))
           {
               unsigned int number = matrix[i][j];
               

               if (number%2 == 1 )
               {
                  
                   sum=number+sum;

               }
             
           }
        }
    }

    std::cout << "The sum is: " << sum << std::endl;


    return 0;
}
