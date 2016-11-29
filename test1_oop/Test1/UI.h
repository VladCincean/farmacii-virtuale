#pragma once
#include "Controller.h"
#include <iostream>
#include <string>

using namespace std;

class UI {
private:
	Controller ctrl{};
private:
	void printMenu();
	void addMenu();
	void delMenu();
	void showAllMenu();
	void allByM();
public:
	UI(const Controller& c) : ctrl(c) {}

	void run();
};

void UI::printMenu() {
	cout << "1 - ADD a new car" << endl;
	cout << "2 - REMOVE a car" << endl;
	cout << "3 - SHOW ALL cars" << endl;
	cout << "4 - Show all by manufacter" << endl;
	cout << "0 - EXIT" << endl;
}

void UI::addMenu() {
	string name, model, color;
	int year;
	cin.get();
	cout << "\tManufacter's name: ";
	getline(cin, name);
	cout << "\tModel: ";
	getline(cin, model);
	cout << "\tColor: ";
	getline(cin, color);
	cout << "\tYear: ";
	cin >> year;
	if (this->ctrl.addCtrl(name, model, year, color) == 1)
		cout << "Car successfully added." << endl;
	else
		cout << "Error. Car already exists. Not added." << endl;
}

void UI::delMenu() {
	string model;
	int year = 0;
	cin.get();
	cout << "Enter the model and year of car to be removed" << endl;
	cout << "\tModel: ";
	getline(cin, model);
	cout << "\tyear: ";
	cin >> year;
	if (this->ctrl.delCtrl(model, year) == 1)
		cout << "Car successfully removel." << endl;
	else
		cout << "Error. Car not found." << endl;
}

void UI::showAllMenu() {
	DynamicVector<Car> v = this->ctrl.getRepo();
	if (v.getSize() == 0)
		cout << "Nothing here..." << endl;
	else
		for (int i = 0; i < v.getSize(); i++) {
			Car c = v[i];
			cout << i + 1 << ". " << c.getName() << " | " << c.getModel() << " | " << c.getYear() << " | " << c.getColor() << endl;
		}
}

void UI::allByM() {
	string name;
	cin.get();
	cout << "\tManufacter's name: ";
	getline(cin, name);
	DynamicVector<Car> v = this->ctrl.allGiven(name);
	if (v.getSize() == 0)
		cout << "Nothing here..." << endl;
	else
		for (int i = 0; i < v.getSize(); i++) {
			Car c = v[i];
			cout << i + 1 << ". " << c.getName() << " | " << c.getModel() << " | " << c.getYear() << " | " << c.getColor() << endl;
		}
}

void UI::run() {
	while (1) {
		this->printMenu();
		int cmd;
		cout << "Enter command: ";
		cin >> cmd;
		if (cmd == 0)
			break;
		switch (cmd) {
		case 1:
			this->addMenu();
			break;
		case 2:
			this->delMenu();
			break;
		case 3:
			this->showAllMenu();
			break;
		case 4:
			this->allByM();
			break;
		default:
			cout << "Wrong command." << endl;
			break;
		}
	}
}
