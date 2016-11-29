#pragma once

template <typename T>
class DynamicVector {
private:
	T* elems;
	int size;
	int capacity;

public:
	// Default constructor for DynamicVector
	//DynamicVector();

	// Default constructor for DynamicVector
	DynamicVector(int capacity = 10);

	// Copy constructor for DynamicVector
	DynamicVector(const DynamicVector& v);

	// Destructor for DynamicVector
	~DynamicVector();

	// Oveloading the assignment operator
	DynamicVector& operator=(const DynamicVector& v);

	/*
	Overloading the subscript operator
	Input: a valid position within the vector (0 <= pos < size(v))
	Output: a reference to the element on that position 
	*/
	T& operator[](int pos);

	// Add an element to the DynamicVector
	void add(T e);

	// Remove from the DynamicVector the element from a given position (does NOT check the validity of pos)
	T del(int pos);

	// Get the size of the DynamicVector
	int getSize() const;

	// Overload + operator to be able to perform 'v + e'
	DynamicVector operator+(T e);

	// Overload - operator to be able to perform 'v - e'
	DynamicVector operator-(T e);

	//DynamicVector operator+=(T e) { return this + e; }

	//DynamicVector operator-=(T e) { return this - e; }

	void setAtPos(int pos, T e);

private:
	// Resize the DynamicVector, multiplying its capacity by a given factor (2, by default)
	void resize(unsigned int factor = 2);
};

//template <typename T>
//DynamicVector<T>::DynamicVector() {
//	this->size = 0;
//	this->capacity = 10;
//	this->elems = new T[this->capacity];
//}

template <typename T>
DynamicVector<T>::DynamicVector(int capacity = 10) {
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[this->capacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector<T>& v) {
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}

template <typename T>
DynamicVector<T>::~DynamicVector() {
	delete[] this->elems;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& v) {
	if (this == &v)
		return *this;

	this->size = v.size;
	this->capacity = v.capacity;

	delete[] this->elems;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

template <typename T>
T& DynamicVector<T>::operator[](int pos) {
	return this->elems[pos];
}

template <typename T>
void DynamicVector<T>::resize(unsigned int factor) {
	this->capacity *= factor;
	T* elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		elements[i] = this->elems[i];

	delete[] this->elems;
	this->elems = elements;
}

template <typename T>
void DynamicVector<T>::add(T e) {
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size++] = e;
}

template <typename T>
T DynamicVector<T>::del(int pos) {
	T elem = elems[pos];
	for (int i = pos; i < this->size - 1; i++)
		this->elems[i] = this->elems[i + 1];
	this->size--;
	return elem;
}

template <typename T>
int DynamicVector<T>::getSize() const {
	int s = this->size;
	return s;
}

template <typename T>
DynamicVector<T> DynamicVector<T>::operator+(T e) {
	DynamicVector<T> res = *this;
	res.add(e);
	return res;
}

template <typename T>
DynamicVector<T> DynamicVector<T>::operator-(T e) {
	DynamicVector<T> res = *this;
	for (int i = 0; i < res.size; i++)
		if (res[i] == e)
			res.del(i);
	return res;
}

// non-member function
template <typename T>
DynamicVector<T> operator+(T e, const DynamicVector<T>& v) {
	DynamicVector<T> res = v;
	res.add(e);
	return res;
}

template <typename T>
void DynamicVector<T>::setAtPos(int pos, T e) {
	this->elems[pos] = e;
}
