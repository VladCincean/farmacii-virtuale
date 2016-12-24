#pragma once
#include "DynVectLWCE.h"
#include "SLListLWCE.h"
#include <iostream>
#include <assert.h>

class Tester {
private:
	ListWithCurrentADT<int>* repr;

public:
	Tester() {}
	~Tester() {}

	void testAll();

private:
	void setUpRepr1();
	void setUpRepr2();
	void tearDown();

	void testSet1();
	void testSet2();
};

void Tester::testAll() {
	std::cout << "Started unit testing...\n";

	try {
		std::cout << "Testing representation #1...\n";

		std::cout << "Set 1: started testing...\n";
		this->setUpRepr1();
		this->testSet1();
		this->tearDown();
		std::cout << "Set 1: all tests passed.\n";

		std::cout << "Set 2: started testing...\n";
		this->setUpRepr1();
		this->testSet2();
		this->tearDown();
		std::cout << "Set 2: all tests passed.\n";

		std::cout << "Testing representation #2...\n";

		std::cout << "Set 1: started testing...\n";
		this->setUpRepr2();
		this->testSet1();
		this->tearDown();
		std::cout << "Set 1: all tests passed.\n";

		std::cout << "Set 2: started testing...\n";
		this->setUpRepr2();
		this->testSet2();
		this->tearDown();
		std::cout << "Set 2: all tests passed.\n";

		std::cout << "Done.\n";
	}
	catch (std::exception& e) {
		std::cout << "Unit testing failed: " << e.what() << std::endl;
	}
}

void Tester::setUpRepr1() {
	this->repr = new DynVectLWCE<int>;
}

void Tester::setUpRepr2() {
	this->repr = new SLListLWCE<int>;
}

void Tester::tearDown() {
	delete this->repr;
}

void Tester::testSet1() {
	assert(this->repr->getSize() == 0);
	try {
		this->repr->getCurrent();
		assert(false);
	}
	catch (...) {
		assert(true);
	}
	assert(this->repr->isEmpty() == true);

	this->repr->addBack(4);
	assert(this->repr->getSize() == 1);
	assert(this->repr->getCurrent() == 4);
	assert(this->repr->isEmpty() == false);

	this->repr->addFront(1);
	assert(this->repr->getSize() == 2);
	assert(this->repr->getCurrent() == 1);
	assert(this->repr->isEmpty() == false);

	this->repr->addAfter(3);
	assert(this->repr->getSize() == 3);
	assert(this->repr->getCurrent() == 3);
	assert(this->repr->isEmpty() == false);

	this->repr->addBefore(2);
	assert(this->repr->getSize() == 4);
	assert(this->repr->getCurrent() == 2);
	assert(this->repr->isEmpty() == false);

	this->repr->first();
	assert(this->repr->getCurrent() == 1);
	this->repr->next();
	assert(this->repr->getCurrent() == 2);
	this->repr->next();
	assert(this->repr->getCurrent() == 3);
	this->repr->next();
	assert(this->repr->getCurrent() == 4);
	try {
		this->repr->next();
		assert(false);
	}
	catch (...) {
		assert(true);
	}
	assert(this->repr->getCurrent() == 4);
	this->repr->prev();
	assert(this->repr->getCurrent() == 3);
	this->repr->prev();
	assert(this->repr->getCurrent() == 2);
	this->repr->prev();
	assert(this->repr->getCurrent() == 1);
	try {
		this->repr->prev();
		assert(false);
	}
	catch (...) {
		assert(true);
	}

	this->repr->last();
	assert(this->repr->getCurrent() == 4);
	this->repr->delCurrent();
	this->repr->delCurrent();
	this->repr->delCurrent();
	this->repr->delCurrent();
	try {
		this->repr->delCurrent();
		assert(false);
	}
	catch (...) {
		assert(true);
	}
	assert(this->repr->getSize() == 0);
	assert(this->repr->isEmpty() == true);
}

void Tester::testSet2() {
	this->repr->addBack(1);
	this->repr->addBack(5);
	this->repr->addBack(2);
	this->repr->addBack(3);
	assert(this->repr->getSize() == 4);

	assert(this->repr->valid() == true);
	assert(this->repr->hasNext() == false);
	assert(this->repr->hasPrev() == true);

	this->repr->first();
	assert(this->repr->valid() == true);
	assert(this->repr->hasNext() == true);
	assert(this->repr->hasPrev() == false);

	assert(this->repr->exists(4) == false);
	assert(this->repr->exists(1) == true);

	this->repr->setCurrent(4);
	assert(this->repr->exists(4) == true);
	assert(this->repr->exists(1) == false);
}
