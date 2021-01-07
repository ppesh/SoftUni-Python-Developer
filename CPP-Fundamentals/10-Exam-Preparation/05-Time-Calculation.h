// Time Calculation

#include<iostream>

using namespace std;

class Time {
private:
	int hours, min, sec;
public:
	Time(int hours_, int min_, int sec_) :
		hours(hours_),
		min(min_),
		sec(sec_) {

	}

	/*
	void calc() {
		cout << hours * 1 + min / 60 + sec / 3600 << endl
			 << hours * 60 + min / 60 + sec / 60 << endl
			 << hours * 3600 + min * 60 + sec;
	}
	*/

	int TotalHours() {
		int h;
		h = hours * 1 + min / 60 + sec / 3600;
		return h;
	}
	int TotalMinutes() {
		int m;
		m = hours * 60 + min / 60 + sec / 60;
		return m;
	}
	int TotalSeconds() {
		int s;
		s = hours * 3600 + min * 60 + sec;
		return s;
	}

};

int main() {
	int hours, min, sec;
	cin >> hours >> min >> sec;

	Time TotalTime(hours, min, sec);
	TotalTime.TotalHours();
	TotalTime.TotalMinutes();
	TotalTime.TotalSeconds();

	cout << TotalTime.TotalHours() << endl;
	cout << TotalTime.TotalMinutes() << endl;
	cout << TotalTime.TotalSeconds() << endl;



	return 0;
}