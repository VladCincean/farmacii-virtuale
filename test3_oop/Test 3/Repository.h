#pragma once
#include "Player.h"
#include <vector>

class Repository {
private:
	std::vector<Player> data;

public:
	Repository(std::string filename);
	~Repository();
	std::vector<Player> getAll();

	/*
	Provides the number of players having a given nationality
	Input: nationality (string)
	Ouput: the number of players gaving the given nationality
	*/
	int playersByNationality(std::string nationality);
};
