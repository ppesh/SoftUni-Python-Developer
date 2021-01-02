// Rust

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void readRust(vector<string>& outInput)
{
	int rows = 10;
	int cols = 10;

	outInput.resize(rows);
	for (int i = 0; i < rows; ++i)
	{
		outInput[i].resize(cols);
	}

	for (int row = 0; row < rows; ++row)
	{
		std::cin >> outInput[row];
	}
}

extern void printMatrix(const vector<string>& matrix);

void expandSingleRust(vector<string>& rustField,
	const int ROW,
	const int COL)
{
	if (COL < 0 || ROW < 0 || COL >= (int)rustField[0].size() ||
		ROW >= (int)rustField.size())
	{
		return;
	}

	if (rustField[ROW][COL] != '#')
		rustField[ROW][COL] = '!';
}

void expandRust(vector<string>& rustedMetal, vector<int> & rustX, vector<int> & rustY)
{
	for (size_t i = 0; i < rustX.size(); ++i)
	{
		int ROW = rustX[i], COL = rustY[i];

		expandSingleRust(rustedMetal, ROW - 1, COL);
		expandSingleRust(rustedMetal, ROW, COL - 1);
		expandSingleRust(rustedMetal, ROW, COL + 1);
		expandSingleRust(rustedMetal, ROW + 1, COL);
	}
}

extern void findMines(const vector<string>& matrix,
	vector<int>& minesX,
	vector<int>& minesY);


int main()
{
	//1) read input
	vector<string> rustedMetal;
	readRust(rustedMetal);

	int ticks; 
	cin >> ticks; // how many time ticks we need to calculate

	//3) expand rust 'ticks' times
	while (ticks--) {
		//cout << "TICK: " << ticks + 1 << endl;
		//cout << "====================";

		vector<int> rustX;
		vector<int> rustY;
		findMines(rustedMetal, rustX, rustY); // analyze and locate rust's coordinates

		// DEBUG INFO
		//for (int i = 0; i < rustX.size(); i++)
		//	cout << "(" << rustX[i] << ", " << rustY[i] << "),   ";

		expandRust(rustedMetal, rustX, rustY); // extend new rust on the rustedMetal
		//printMatrix(rustedMetal);
	}

	//4) print answer
	printMatrix(rustedMetal);

	return 0;
}

/*
=== 0 ===
..........
....!.....
..........
..........
..........
..........
..........
..........
..........
..........

=== 1 ===
....!.....
...!!!....
....!.....
..........
..........
..........
..........
..........
..........
..........



*/