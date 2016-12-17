#include "UI.h"
#include <iostream>

using namespace std;

void UI::printMenu() {
	cout << "1 - Remove a painting" << endl;
	cout << "2 - Move to special storage" << endl;
	cout << "3 - Show GALLERY" << endl;
	cout << "4 - Show SPECIAL CONDITIONS STORAGE" << endl;
	cout << "5 - Undo" << endl;
	cout << "0 - EXIT" << endl;
}

void UI::run() {
	while (1) {
		this->printMenu();
		int cmd;
		cout << "Command: ";
		cin >> cmd;
		if (cmd == 0)
			break;
		switch (cmd) {
		case 1:
			this->_remove();
			break;
		case 2:
			this->_move();
			break;
		case 3:
			this->_showGallery();
			break;
		case 4:
			this->_showSpecial();
			break;
		case 5:
			try {
				this->ctrl.undo();
			}
			catch (...) {
				cout << "Cannot undo" << endl;
			}
			break;
		default:
			cout << "Wrong command" << endl;
			break;
		}
	}
}

void UI::_remove() {
	string artist, title;
	int year;
	cin.get();
	cout << "artist: ";
	getline(cin, artist);
	cout << "title: ";
	getline(cin, title);
	cout << "year: ";
	cin >> year;
	try {
		this->ctrl.removePainting(artist, title, year);
	}
	catch(...) {
		cout << "Error. The painting does not exists." << endl;
		cin.get();
	}
}

void UI::_move() {
	string artist, title;
	int year;
	cin.get();
	cout << "artist: ";
	getline(cin, artist);
	cout << "title: ";
	getline(cin, title);
	cout << "year: ";
	cin >> year;
	try {
		this->ctrl.movePainting(artist, title, year);
	}
	catch (...) {
		cout << "Error. The painting does not exists." << endl;
		cin.get();
	}
}

void UI::_showGallery() {
	vector<Painting> v = this->ctrl.getAll();
	for (Painting p : v) {
		cout << p.getArtist() << ", " << p.getTitle() << ", " << p.getYear() << endl;
	}
}

void UI::_showSpecial() {
	vector<Painting> v = this->ctrl.getAllSpecialStorage();
	for (Painting p : v) {
		cout << p.getArtist() << ", " << p.getTitle() << ", " << p.getYear() << endl;
	}
}

