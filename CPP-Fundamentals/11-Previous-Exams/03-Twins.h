// 03. Twins

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int times = 0;
	vector <string> clientsPepi;
	vector <size_t> serviceTimePepi;
	vector <string> clientsMimi;
	vector <size_t> serviceTimeMimi;
	string name, client;
	size_t servicetime = 0;
	cin >> times;
	while (times--) {
		cin >> name >> client >> servicetime;
		if (name == "Pepi") {
			clientsPepi.push_back(client);
			serviceTimePepi.push_back(servicetime);
		}
		else {
			clientsMimi.push_back(client);
			serviceTimeMimi.push_back(servicetime);
		}
	}

	cin >> servicetime;

	unsigned turnP = 0, turnM = 0;
	for (size_t j = 0; j < servicetime; j++) {

		cout << "Pepi ";
		if (turnP >= clientsPepi.size()) {
			cout << "Idle" << endl;
		}
		else {
			if (serviceTimePepi[turnP] == 0)
				turnP++;
			if (turnP >= clientsPepi.size()) {
				cout << "Idle" << endl;
			}
			else {
				cout << "processing " << clientsPepi[turnP] << endl;
				serviceTimePepi[turnP]--;
			}
		}

		cout << "Mimi ";
		if (turnM >= clientsMimi.size()) {
			cout << "Idle" << endl;
		}
		else {
			if (serviceTimeMimi[turnM] == 0)
				turnM++;
			if (turnM >= clientsMimi.size()) {
				cout << "Idle" << endl;
			}
			else {
				cout << "processing " << clientsMimi[turnM] << endl;
				serviceTimeMimi[turnM]--;
			}
		}
	}
	return 0;
}