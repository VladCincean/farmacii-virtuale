#include "Player.h"
#include <sstream>

using namespace std;

std::istream& operator>>(std::istream& is, Player& p) {
	string temp;
	stringstream ss;
	getline(is, temp);
	ss = stringstream(temp);

	getline(ss, temp, '|');
	p.name = temp;

	getline(ss, temp, '|');
	p.nationality = temp;

	getline(ss, temp, '|');
	p.team = temp;

	//getline(ss, temp);
	//p.goals = stoi(temp);

	ss >> p.goals;

	return is;
}
