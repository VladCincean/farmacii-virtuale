#include "Repository.h"

using namespace std;

void Repository::addPainting(Painting p) {
	for (int i = 0; i < this->repo.size(); i++) {
		Painting a = this->repo[i];
		if (a.getArtist() == p.getArtist() && a.getTitle() == p.getTitle() && a.getYear() == a.getYear())
			throw exception("Error. Already in repo.\n");
	}
	this->repo.push_back(p);
}

void Repository::removePainting(Painting p) {
	bool found = false;
	for (int i = 0; i < this->repo.size(); i++) {
		Painting a = this->repo[i];
		if (a.getArtist() == p.getArtist() && a.getTitle() == p.getTitle() && a.getYear() == a.getYear()) {
			found = true;
			this->repo.erase(this->repo.begin() + i);
		}
	}
	if (!found)
		throw exception("Error. Not found in repo.\n");
}

vector<Painting> Repository::getAll() {
	return this->repo;
}
