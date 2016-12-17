#pragma once
#include "DynamicVector.h"
#include "Car.h"
#include <assert.h>

class Repository {
private:
	DynamicVector<Car> repo{};

public:
	Repository() {}

	void addCar(const Car& c);

	void delCar(int pos);

	int findCar(const std::string& model, int year);

	Car getAtPos(int pos);

	DynamicVector<Car> getAll() { return repo; }
};

/*
Adds a car to repository
Input: c - Car to be added to repo
*/
void Repository::addCar(const Car& c) {
	this->repo.add(c);
}

/*
Deletes a car from repository given by its position
Input: pos (int) - car's position
*/
void Repository::delCar(int pos) {
	if (pos == -1)
		return;
	this->repo.del(pos);
}

int Repository::findCar(const std::string& model, int year) {
	if (this->repo.getSize() == 0)
		return -1;
	for (int i = 0; i < this->repo.getSize(); i++) {
		Car c = this->repo[i];
		if (c.getModel() == model && c.getYear() == year)
			return i;
	}
	return -1;
}

Car Repository::getAtPos(int pos) {
	if (pos == -1)
		return Car{};
	Car c = this->repo[pos];
	return c;
}


void testRepo() {
	Repository r{};
	assert(r.getAll().getSize() == 0);
	Car c{ "Fiat", "Bravo", 2007, "red" };
	r.addCar(c);
	assert(r.getAll().getSize() == 1);
	int pos = r.findCar("Bravo", 2007);
	r.delCar(pos);
	assert(r.getAll().getSize() == 0);
}
