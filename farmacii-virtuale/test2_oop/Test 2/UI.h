#pragma once
#include "Controller.h"

using namespace std;

class UI {
private:
	Controller ctrl;

public:
	UI() {};
	UI(Controller c) {
		this->ctrl = c;
	}
	
	void run();

private:
	void printMenu();

	void _remove();
	void _move();
	void _showGallery();
	void _showSpecial();
};