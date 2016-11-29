#pragma once
#include <string>

using namespace std;

class Car {
private:
	std::string name;
	std::string model;
	int year;
	std::string color;
public:
	Car() { "", "", 0, ""; }

	// default constructor
	Car(const string& name, const string& model, int year, const string& color) {
		this->name = name;
		this->model = model;
		this->year = year;
		this->color = color;
	}

	std::string& getName();
	std::string& getModel();
	int getYear();
	std::string& getColor();
};

std::string& Car::getName() {
	return this->name;
}

std::string& Car::getModel() {
	return this->model;
}

int Car::getYear() {
	return this->year;
}

std::string& Car::getColor() {
	return this->color;
}

