// Positions Of

#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;

// function returns if a given element exists in the matrix
/*
bool does_exist(const vector< vector<int> >& v, int item) {

    vector< vector<int> >::const_iterator row;

    for (row = v.begin(); row != v.end(); row++) {
        if (find(row->begin(), row->end(), item) != row->end())
           return true;
        
    }

    return false;
}
*/


void findNum(vector<vector<int> > mat, int num, int R, int C) {

    int row, col, count = 0;
    for (row = 0; row < R; row++) {
        for (col = 0; col < C; col++) {
            if (mat[row][col] == num) {
                cout << row << " " << col << '\n';
            }
            else {
                count++;
            }

        }
    }

    if (count == col * row) {
        cout << "not found" << endl;
    }

}


    int main(){

        int R, C;                                           // R: number of rows, C: number of columns
        cin >> R >> C;

        // initialize matrix mat
        vector<vector<int> > mat;

        for (int row = 0; row < R; row++) {
            vector<int>input_row;
            for (int col = 0; col < C; col++) {
                int element;
                cin >> element;
                input_row.push_back(element);
            }
            mat.push_back(input_row);
        }
        
        /*
        // print matrix mat
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < mat[0].size(); col++) {
                cout << mat[row][col] << " ";
            }
            cout << endl;
        }
        */
       
        int num;
        cin >> num;

        /*
        if (does_exist(mat, num))
            cout << "exist" << endl;
        else
            cout << "not found" << endl;
        */

        findNum(mat, num, R, C);
        
        return 0;
    }