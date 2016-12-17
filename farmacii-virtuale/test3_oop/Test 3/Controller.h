#pragma once
#include "Repository.h"

class Controller {
private:
	Repository repo;

public:
	Controller(Repository& r) : repo(r) {}
	~Controller() {}

	inline std::vector<Player> getAll() { return repo.getAll(); }

	/*
	Provides the number of players having a given nationality
	Input: nationality (string)
	Ouput: the number of players gaving the given nationality
	*/
	inline int playersByNationality(std::string nationality) { return repo.playersByNationality(nationality); }

	/*
	Provides all players in sorted order by team
	Input: -
	Output: vector of players in sorted order by team
	*/
	std::vector<Player> getAllSorted();
};
