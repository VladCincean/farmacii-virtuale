#pragma once
#include "Balloon.h"
#include "DynVectLWCE.h"
#include "SLListLWCE.h"
#include <string>
#include <exception>
#include <iostream>
#include <fstream>
#include <limits>
#include <ctime>

using std::string;
using std::exception;
using std::ifstream;
using std::ofstream;
using std::numeric_limits;
using std::cout;
using std::endl;

class BalloonsGame {
private:
	ListWithCurrentADT<Balloon>* _balloons;
	string _filename;

public:
	BalloonsGame(string filename) : _filename(filename) {};
	void runUsingRepr1();
	void runUsingRepr2();

private:
	void _readFromFile();
	void _bubbleSort();
	void _solve();
	void _run();
};

void BalloonsGame::_readFromFile() {
	ifstream f(this->_filename);
	if (!f.is_open())
		throw exception("Cannot open the input file.");

	double xCoord, radius;
	while (f >> xCoord >> radius) {
		Balloon b{ xCoord, radius, false };

		// !! use only one of the following two posibilities
		this->_balloons->addBack(b);
		//this->_balloons->addFront(b);
	}

	f.close();
}

void BalloonsGame::_bubbleSort() {
	int n = this->_balloons->getSize();
	bool swaps = true;
	while (swaps) {
		swaps = false;
		this->_balloons->first();
		while (this->_balloons->hasNext()) {
			Balloon b1 = this->_balloons->getCurrent();
			this->_balloons->next();
			Balloon b2 = this->_balloons->getCurrent();
			if (b1.getRightBound() > b2.getRightBound()) {
				// here, swap them
				Balloon temp = b2;
				this->_balloons->setCurrent(b1);
				this->_balloons->prev();
				this->_balloons->setCurrent(temp);
				this->_balloons->next();
				swaps = true;
			}
		}
	}
}

void BalloonsGame::_solve() {
	string fName = "SOL_" + this->_filename;
	ofstream g(fName);

	int nrArrows = 0;
	double lastArrow = - numeric_limits<double>::infinity();

	this->_balloons->first();
	Balloon b = this->_balloons->getCurrent();
	if (lastArrow < b.getLeftBound()) {
		lastArrow = b.getRightBound(); // shoot the arrow on the right bound of the balloon
		++nrArrows;
		g << "Arrow no. " << nrArrows << " found at coord. " << lastArrow << endl;
	}
	do {
		this->_balloons->next();
		Balloon b = this->_balloons->getCurrent();
		if (lastArrow < b.getLeftBound()) {
			lastArrow = b.getRightBound(); // shoot the arrow on the right bound of the balloon
			++nrArrows;
			g << "Arrow no. " << nrArrows << " found at coord. " << lastArrow << endl;
		}
	} while (this->_balloons->hasNext());

	g.close();
}

void BalloonsGame::_run() {
	clock_t start, end;
	double duration;

	start = clock();
	this->_readFromFile();
	end = clock();
	duration = (double)(end - start) / (CLOCKS_PER_SEC);
	cout << "Reading from file executed in " << duration << " s.." << endl;

	start = clock();
	this->_bubbleSort();
	end = clock();
	duration = (double)(end - start) / (CLOCKS_PER_SEC);
	cout << "Sorting executed in " << duration << " s.." << endl;

	start = clock();
	this->_solve();
	end = clock();
	duration = (double)(end - start) / (CLOCKS_PER_SEC);
	cout << "Solving the problem executed in " << duration << " s.." << endl;

	cout << "Done." << endl;
}

void BalloonsGame::runUsingRepr1() {
	this->_balloons = new DynVectLWCE<Balloon>;
	this->_run();
	delete this->_balloons;
}

void BalloonsGame::runUsingRepr2() {
	this->_balloons = new SLListLWCE<Balloon>;
	this->_run();
	delete this->_balloons;
}
