#include "Controller.h"
#include <algorithm>

using namespace std;

bool myFunction(Player a, Player b) {
	//return (a.getTeam().compare(b.getTeam()));
	return (a.getTeam() < b.getTeam());
}

/*
Provides all players in sorted order by team
Input: -
Output: vector of players in sorted order by team
*/
vector<Player> Controller::getAllSorted() {
	vector<Player> all = this->repo.getAll();
	sort(all.begin(), all.end(), myFunction);
	return all;
}
