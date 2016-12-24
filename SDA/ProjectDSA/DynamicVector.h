#pragma once

template <typename TE>
class DynamicVector {
private:
	TE* elements;
	int size;
	int capacity;

public:
	DynamicVector();
	DynamicVector(const DynamicVector& v);
	~DynamicVector();

	DynamicVector& operator=(const DynamicVector& v);
	TE& operator[](int index) const;

	void push_back(const TE e);
	void insert(int poisiton, const TE e);
	TE del(int poisition);

	int getSize();

private:
	void resize(int factor = 2);
};

template <typename TE>
DynamicVector<TE>::DynamicVector() {
	this->capacity = 1;
	this->size = 0;
	this->elements = new TE[this->capacity];
}

template <typename TE>
DynamicVector<TE>::DynamicVector(const DynamicVector<TE>& v) {
	delete[] this->elements;
	this->capacity = v.capacity;
	this->size = v.size;
	this->elements = new TE[this->capacity];
	for (int i = 0; i < this->size; i++) {
		this->elements[i] = v.elements[i];
	}
}

template <typename TE>
DynamicVector<TE>::~DynamicVector() {
	delete[] this->elements;
}

template <typename TE>
DynamicVector<TE>& DynamicVector<TE>::operator=(const DynamicVector<TE>& v) {
	if (this == &v)
		return *this;

	this->size = v.size;
	this->capacity = v.capacity;
	delete[] this->elements;
	this->elements = new TE[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = v.elements[i];

	return *this;
}

template <typename TE>
TE& DynamicVector<TE>::operator[](int index) const {
	return this->elements[index];
}

template <typename TE>
void DynamicVector<TE>::push_back(const TE e) {
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size++] = e;
}

template <typename TE>
void DynamicVector<TE>::insert(int position, const TE e) {
	if (position < 0 || position > this->size - 1)
		return;

	if (this->size == this->capacity)
		this->resize();

	for (int i = this->size - 1; i >= position; i--)
		this->elements[i + 1] = this->elements[i];
	this->size++;
	this->elements[position] = e;
}

template <typename TE>
TE DynamicVector<TE>::del(int position) {
	TE elem = this->elements[position];
	for (int i = position; i < this->size; i++)
		this->elements[i] = this->elements[i + 1];
	this->size--;
	return elem;
}

template <typename TE>
int DynamicVector<TE>::getSize() {
	return this->size;
}

template <typename TE>
void DynamicVector<TE>::resize(int factor = 2) {
	this->capacity *= factor;
	this->capacity++; // c' := f*c + 1
	TE* newElems = new TE[this->capacity];
	for (int i = 0; i < this->size; i++)
		newElems[i] = this->elements[i];
	delete[] this->elements;
	this->elements = newElems;
}
