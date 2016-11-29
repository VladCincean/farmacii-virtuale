#pragma once
#include "Repository.h"
#include "Undo.h"

using namespace std;

class Controller {
private:
	Repository repoAll;
	Repository repoSpecialStorage;
	vector<UndoOperation*> operations;

public:
	Controller() {};
	Controller(Repository rAll, Repository rSpecial) {
		this->repoAll = rAll;
		this->repoSpecialStorage = rSpecial;
	}
	void movePainting(string artist, string title, int year);
	void removePainting(string artist, string title, int year);
	vector<Painting> getAll();
	vector<Painting> getAllSpecialStorage();

	void undo();
};