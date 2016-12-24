#pragma once
#include "ListWithCurrentADT.h"
#include "DynamicVector.h"
#include <exception>

template <typename TE>
class DynVectLWCE : public ListWithCurrentADT<TE> {
private:
	DynamicVector<TE> elements;
	int current;
	int size;

public:
	DynVectLWCE() {
		this->size = 0;
		this->current = -1;
	}

	DynVectLWCE(const DynVectLWCE<TE>& l) {
		this->elements = l.elements;
		this->size = l.size;
		this->current = l.current;
	}

	~DynVectLWCE() {}

	TE getCurrent() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		return this->elements[this->current];
	}

	void setCurrent(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		this->elements[this->current] = e;
	}

	void delCurrent() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		this->elements.del(this->current);
		this->size--;
		if (this->current == this->size) // if we just deleted the last element
			this->current = 0;
	}

	void first() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		this->current = 0;
	}

	void last() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		this->current = this->elements.getSize() - 1;
	}

	void next() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->hasNext())
			throw std::exception("On last position. Can't go forward.");

		this->current++;
	}

	bool hasNext() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		return this->current != this->size - 1; // current is not the last
	}

	void prev() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->hasPrev())
			throw std::exception("On first position. Can't go backward.");

		this->current--;
	}

	bool hasPrev() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		return this->current != 0; // current is not the first
	}

	bool valid() override {
		return this->current < this->size && this->current >= 0;
	}

	bool exists(const TE e) override {
		for (int i = 0; i < this->elements.getSize(); i++)
			if (this->elements[i] == e)
				return true;
		return false;
	}

	bool isEmpty() override {
		return this->size == 0;
	}

	int getSize() override {
		return this->size;
	}

	void addFront(const TE e) override {
		this->elements.insert(0, e);
		this->size++;
		this->current = 0;
	}

	void addBack(const TE e) override {
		this->elements.push_back(e);
		this->size++;
		this->current = this->size - 1;
	}

	void addBefore(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		this->elements.insert(this->current, e);
		this->size++;
	}

	void addAfter(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		if (this->current == this->size - 1) {
			this->elements.push_back(e);
		}
		else
			this->elements.insert(this->current + 1, e);
		this->size++;
		this->current++;
	}
};
