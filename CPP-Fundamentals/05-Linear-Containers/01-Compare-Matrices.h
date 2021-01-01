// Compare Matrices

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

bool areSame(vector<vector<int> > mat1, vector<vector<int> > mat2, int R, int R2, int C, int C2)
{
    // R:  number of rows, C: number columns
    if ((R == R2) && (C == C2)) {
        int row, col;
        for (row = 0; row <R; row++) {
            for (col = 0; col <C; col++) {
                if (mat1[row][col] != mat2[row][col]) {
                    return false;
                }
                
            }
        }
    }
    else {
        return true;
    }
    return true;
}


    int main(){

        int R = 0;                                           // r: row, c: columns
        cin >> R; 

        if((cin.get() =='\n') && (cin.peek() == '\n')) {
            cout << "not equal" << endl;
        }

        // initialize matrix A
        vector<vector<int> > matA;
        vector<int> input_r;int c,r=1;
       
        while (cin >> c) {
            //int count = 0;
            
            if(cin.get() != '\n') { 
                input_r.push_back(c);  
            }
            else {
              input_r.push_back(c);
              matA.push_back(input_r);
              input_r.clear();  
              ++r;
            }
         
              if (r > R)
                  break;
        }
        
        int C = matA[0].size();         // get size of columns
        //cout << C << endl;

        /*
        // print matrix A
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < matA[0].size(); col++) {
                cout << matA[row][col] << " ";
            }
            cout << endl;
        }
        */
       
        int R2 = 0;                                           
        cin >> R2;

        if ((cin.get() == '\n') && (cin.peek() == '\n')) {
            cout << "not equal" << endl;
        }
        // initialize matrix B
        vector<vector<int> > matB;
        vector<int> input_r2; int c2, r2 = 1;

        while (cin >> c2) {
            //int count = 0;

            if (cin.get() != '\n') {
                input_r2.push_back(c2);
            }
            else {
                input_r2.push_back(c2);
                matB.push_back(input_r2);
                input_r2.clear();
                ++r2;
            }

            if (r2 > R2)
                break;
        }

        int C2 = matB[0].size();

        /*
        // print matrix B
        for (int row = 0; row < R; row++) {
            for (int col = 0; col < matB[0].size(); col++) {
                cout << matB[row][col] << " ";
            }
            cout << endl;
        }
        */

        
        //areSame(matA, matB, R, R2, C, C2);
        if (areSame(matA, matB, R, R2, C, C2)) {
            cout << "equal" << endl;
        }
        else {
            cout << "not equal";
        }
        
        //cout << (areSame != 0) ? "equal" : "not equal" << endl;
        
        return 0;
    }
