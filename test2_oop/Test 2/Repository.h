#pragma once
#include "Painting.h"
#include <vector>

using namespace std;

class Repository {
private:
	vector<Painting> repo;

public:
	Repository() {};
	void addPainting(Painting p);
	void removePainting(Painting p);
	vector<Painting> getAll();
};
