// 02. Square Manipulator

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
 
using namespace std;
 
int main() {
    vector <int> result;
    int rows, cols;
    cin >> rows >> cols;
    const int r=rows, c=cols;
    int matrix[r][c];
    for (int i=0; i<rows; ++i) {
        for (int j=0; j<cols; ++j) {
            cin >> matrix[i][j];
        }
    }
    int square, target;
    cin >> square >> target;
    for (int i=0; i<=rows-square; ++i) {
        for (int j=0; j<=cols-square; ++j) {
            int the_sum = 0;
            for (int m=i; m<i+square; ++m) {
                for (int n=j; n<j+square; ++n) {
                    the_sum += matrix[m][n];
                }
            }
            if (the_sum >= target) {
                result.push_back(trunc(the_sum/square/square));
            }
        }
    }
 
    sort(result.begin(), result.end());
    for (auto n : result) {
        cout << n << " ";
    }
    return 0;
}