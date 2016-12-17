#pragma once
#include "Repository.h"
#include <string>
#include <assert.h>

using namespace std;

class Controller {
private:
	Repository repo{};
public:
	Controller() {};
	Controller(const Repository& r) : repo(r) {}

	int addCtrl(const string& name, const string& model, int year, const string& color);
	int delCtrl(const string& model, int year);
	DynamicVector<Car> getRepo();
	DynamicVector<Car> allGiven(const string& name);
};

/*
Adds a car
Input:  name - car's manufacter's name
		model - car's model
		year - car's year of manufacture
		color - car's color
Return: 1, if car successfully added
		0, otherwise (car already exists)
*/
int Controller::addCtrl(const string& name, const string& model, int year, const string& color) {
	Car c{ name, model, year, color };
	if (this->repo.findCar(model, year) != -1)
		return 0; // already exists
	this->repo.addCar(c);
	return 1; // added
}

/*
Deletes a car
Input:  model - car's model
		year - car's year of manufacture
Output: 1, if car successfully removed
		0, otherwise (car does not exists in repo)
*/
int Controller::delCtrl(const string& model, int year) {
	if (this->repo.findCar(model, year) == -1)
		return 0; // not found
	this->repo.delCar(this->repo.findCar(model, year));
	return 1; // removed
}

DynamicVector<Car> Controller::getRepo() {
	return this->repo.getAll();
}

/*
Gets all cars by the given manufacturer
Input: name - manufacturer's name
Output: DynamicVector of cars
*/
DynamicVector<Car> Controller::allGiven(const string& name) {
	DynamicVector<Car> all = this->repo.getAll();
	DynamicVector<Car> res{};
	for (int i = 0; i < all.getSize(); i++)
		if (all[i].getName() == name)
			res.add(all[i]);
	return res;
}


void testCtrl() {
	Repository r{};
	Controller c(r);
	assert(c.getRepo().getSize() == 0);
	c.addCtrl("Fiat", "Bravo", 2007, "red");
	assert(c.getRepo().getSize() == 1);
	c.addCtrl("Fiat", "Bravo", 2007, "red"); // already exists
	assert(c.getRepo().getSize() == 1);
	c.delCtrl("Bravo", 2007);
	assert(c.getRepo().getSize() == 0);
}
