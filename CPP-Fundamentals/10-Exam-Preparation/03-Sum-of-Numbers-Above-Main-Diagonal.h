// Sum of Numbers Above Main Diagonal

#include <iostream>
#include <vector>
 
using namespace std;
 
int main() {
    cout << "Enter size of matrix:";
    unsigned size;
    cin >> size;
    vector <vector <int>> matrix;
    int temp;
	
    for (int i=0; i<size; ++i)  {
        matrix.emplace_back();
        for (int j=0; j<size; ++j)  {
            cout << "Enter matrix[" << i << "][" << j << "]=";
            cin >> temp;
            matrix[i].push_back(temp);
        }
    }
	
    cout << "The MATRIX is: " << endl;
	
    for (int i=0; i<size; ++i)  {
        for (int j=0; j<size; ++j)  {
            cout << " " << matrix[i][j];
        }
        cout << endl;
    }
	
    int sum = 0;
	
    for (int i=0; i<size; ++i)  {
        for (int j=i+1; j<size; ++j)  {
            sum += matrix[i][j];
        }
    }
	
    cout << "Sum of numbers above diagonal is: " << sum << endl;
	
    return 0;
}