#pragma once
#include <string>
#include <istream>

class Player {
private:
	std::string name, nationality, team;
	int goals;

public:
	inline std::string getName() { return name; }
	inline std::string getNationality() { return nationality; }
	inline std::string getTeam() { return team; }
	inline int getGoals() { return goals; }

	friend std::istream& operator>>(std::istream& is, Player& p);

};
