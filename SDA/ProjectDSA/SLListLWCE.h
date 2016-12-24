#pragma once
#include "ListWithCurrentADT.h"
#include "SLList.h"
#include <exception>

template <typename TE>
class SLListLWCE : public ListWithCurrentADT<TE> {
private:
	SLList<TE> elements;
	SLNode<TE>* current;
	int size;

public:
	SLListLWCE() {
		this->size = 0;
		this->current = nullptr;
	}

	SLListLWCE(const DynVectLWCE<TE>& l) {
		this->elements = l.elements;
		this->size = l.size;
		this->current = l.current;
	}

	~SLListLWCE() {}

	TE getCurrent() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		return this->current->data;
	}

	void setCurrent(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		this->current->data = e;
	}

	void delCurrent() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		this->elements.eraseHere(SLList<TE>::Iterator(this->current));

		this->size--;
		if (this->current == nullptr) // if we just deleted the last element
			this->current = this->elements.getHead();
	}

	void first() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		this->current = this->elements.getHead();
	}

	void last() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");
		if (this->current == nullptr)
			this->current = this->elements.getHead();
		while (this->current->next != nullptr)
			this->current = this->current->next;
	}

	void next() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->hasNext())
			throw std::exception("On last position. Can't go forward.");

		this->current = this->current->next;
	}

	bool hasNext() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		return this->current->next != nullptr; // current is not the last
	}

	void prev() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->hasPrev())
			throw std::exception("On first position. Can't go backward.");

		SLNode<TE>* nod = this->elements.getHead();
		while (nod->next != this->current)
			nod = nod->next;
		this->current = nod;
	}

	bool hasPrev() override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		return this->current != this->elements.getHead(); // current is not the first
	}

	bool valid() override {
		return this->current != nullptr;
	}

	bool exists(const TE e) override {
		for (SLList<TE>::Iterator it = this->elements.begin(); it != this->elements.end(); ++it)
			if (*it == e)
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
		this->elements.insertFront(e);
		this->size++;
		this->current = this->elements.getHead();
	}

	void addBack(const TE e) override {
		this->elements.insertBack(e);
		this->size++;
		this->last();
	}

	void addBefore(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		SLList<TE>::Iterator it(this->current);
		this->elements.insertHere(it, e);
		this->size++;
	}

	void addAfter(const TE e) override {
		if (this->isEmpty())
			throw std::exception("List is empty.");

		if (!this->valid())
			throw std::exception("The current is not valid.");

		SLList<TE>::Iterator it(this->current);
		this->elements.insertAfter(it, e);
		this->size++;
		this->current = this->current->next;
	}
};
