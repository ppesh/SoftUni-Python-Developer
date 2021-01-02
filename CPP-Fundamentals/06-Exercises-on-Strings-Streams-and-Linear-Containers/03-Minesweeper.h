// Minesweeper

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void readInput(vector<string>& outInput)
{
	int rows = 0;
	int cols = 0;

	cin >> rows >> cols;

	outInput.resize(rows);
	for (int i = 0; i < rows; ++i)
	{
		outInput[i].resize(cols);
	}

	for (int row = 0; row < rows; ++row)
	{
		cin >> outInput[row];
	}
}

void printMatrix(const vector<string>& matrix)
{
	for (size_t row = 0; row < matrix.size(); ++row)
	{
		cout << matrix[row] << endl;
	}
}

void findMines(const vector<string>& matrix, vector<int>& minesX, vector<int>& minesY)
{
	for (size_t row = 0; row < matrix.size(); ++row)
	{
		for (size_t col = 0; col < matrix[row].size(); ++col)
		{
			//found mine
			if ('!' == matrix[row][col])
			{
				minesX.push_back(row);
				minesY.push_back(col);
			}
		}
	}
}

void expandSingleMine(vector<string>& mineField, const int ROW, const int COL)
{
	if (COL < 0 || ROW < 0 || COL >= (int)mineField[0].size() || ROW >= (int)mineField.size())
	{
		return;
	}

	mineField[ROW][COL] += 1;
}

void expandMines(vector<string>& mineField, const vector<int>& minesX, const vector<int>& minesY)
{
	for (size_t i = 0; i < minesX.size(); ++i)
	{
		const int ROW = minesX[i];
		const int COL = minesY[i];
		//expand mine


		expandSingleMine(mineField, ROW - 1, COL - 1);
		expandSingleMine(mineField, ROW - 1, COL);
		expandSingleMine(mineField, ROW - 1, COL + 1);

		expandSingleMine(mineField, ROW, COL - 1);
		expandSingleMine(mineField, ROW, COL);
		expandSingleMine(mineField, ROW, COL + 1);

		expandSingleMine(mineField, ROW + 1, COL - 1);
		expandSingleMine(mineField, ROW + 1, COL);
		expandSingleMine(mineField, ROW + 1, COL + 1);
	}
}

int main()
{
	// example:
	//	5 5
	//	.....
	//	...!.
	//	.....
	//	.....
	//	.....

	//1) read input
	vector<string> mineField;
	readInput(mineField);

	//2) find mines
	vector<int> minesX;
	vector<int> minesY;
	findMines(mineField, minesX, minesY);

	vector<string> mineFieldValues(mineField.size(), string(mineField[0].size(), '0'));

	//3) expand mines
	expandMines(mineFieldValues, minesX, minesY);

	//4) print answer
	printMatrix(mineFieldValues);

	return 0;
}
