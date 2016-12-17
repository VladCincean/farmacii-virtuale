#include "Controller.h"

using namespace std;

void Controller::movePainting(string artist, string title, int year) {
	Painting p{ artist, title, year };
	this->repoAll.removePainting(p);
	// ^^ if not found it will throw an exception
	this->repoSpecialStorage.addPainting(p);
	// ^^ if already here it will throw an exception
	UndoOperation* o = new UndoMoveOperation{this->repoAll, this->repoSpecialStorage};
	this->operations.push_back(o);
}

void Controller::removePainting(string artist, string title, int year) {
	Painting p{ artist, title, year };
	this->repoAll.removePainting(p);
	// ^^ if not found it will throw an exception
	UndoOperation* o = new UndoRemoveOperation{this->repoAll, p };
	this->operations.push_back(o);
}

vector<Painting> Controller::getAll() {
	return this->repoAll.getAll();
}

vector<Painting> Controller::getAllSpecialStorage() {
	return this->repoSpecialStorage.getAll();
}

void Controller::undo() {
	if (this->operations.empty())
		throw exception("..");
	UndoOperation* o = this->operations.back();
	this->operations.pop_back();
	o->executeUndo();
}
