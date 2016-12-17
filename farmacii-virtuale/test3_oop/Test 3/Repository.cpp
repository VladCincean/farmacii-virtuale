#include "Repository.h"
#include <fstream>

using namespace std;

Repository::Repository(std::string filename) {
	ifstream f(filename);
	Player p;
	while (f >> p)
		this->data.push_back(p);
	f.close();
}

Repository::~Repository() {
}

vector<Player> Repository::getAll() {
	return this->data;
}

int Repository::playersByNationality(std::string nationality) {
	int count = 0;
	for (Player p : this->data)
		if (p.getNationality() == nationality)
			count++;
	return count;
}
