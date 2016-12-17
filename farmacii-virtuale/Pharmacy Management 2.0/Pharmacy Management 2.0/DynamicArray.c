#include "DynamicArray.h"
#include <stdlib.h>
#include <assert.h>

/*
Creates a dynamic array of TElems = medicines with given capacity
Input: capacity (positive integer) - maximum capacity of the array
Output: a pointer to the dynamic array just created
		NULL, if memory error
*/
DynamicArray* createArray(int capacity) {
	DynamicArray* da = (DynamicArray*)malloc(sizeof(DynamicArray));
	// if the space was NOT allocated, the function will return NULL
	if (da == NULL) {
		return NULL;
	}
	da->capacity = capacity;
	da->length = 0;

	// allocate space for its elements
	da->elements = (TElem*)malloc(capacity*sizeof(TElem));
	// if the space was NOT allocated, the function will return NULL
	if (da->elements == NULL) {
		return NULL;
	}
	return da;
}

/*
Doubles a DynamicArray's capacity, allocating more space
Input: pointer to the DynamicArray
*/
void resizeArray(DynamicArray* da) {
	if (da == NULL)
		return;
	da->capacity *= 2;
	da->elements = (TElem*)realloc(da->elements, da->capacity * sizeof(TElem));
}

/*
Destroys a DynamicArray
Input: pointer to the DynamicArray
*/
void destroyArray(DynamicArray* da) {
	if (da == NULL)
		return;
	free(da->elements);
	da->elements = NULL;
	free(da);
	da = NULL;
}

void addToArray(DynamicArray* da, TElem elem) {
	if (da == NULL)
		return;
	if (da->elements == NULL)
		return;
	if (da->length == da->capacity) {
		resizeArray(da);
	}
	da->elements[da->length++] = elem;
}

void removeFromArray(DynamicArray* da, int pos) {
	if (pos < 0 || pos >= da->length)
		return;
	for (int i = pos; i < da->length - 1; ++i)
		da->elements[i] = da->elements[i + 1];
	da->length--;
}

int getArrayLength(DynamicArray* da) {
	if (da == NULL)
		return -1;
	return da->length;
}

TElem getElem(DynamicArray* da, int pos) {
	return da->elements[pos];
}

void setElem(DynamicArray*da, int pos, TElem elem) {
	if (pos >= 0 && pos < da->length)
		da->elements[pos] = elem;
}

void swapElems(DynamicArray* da, int pos1, int pos2) {
	if (da == NULL)
		return;
	if (da->elements == NULL)
		return;
	TElem aux = da->elements[pos1];
	da->elements[pos1] = da->elements[pos2];
	da->elements[pos2] = aux;
}

void testDynamicArray() {
	DynamicArray* da = createArray(2);
	if (da == NULL) assert(0);
	assert(da->capacity == 2);
	assert(da->length == 0);
	Medicine m1 = createMedicine("nurofen", "200 mg", 20, 25);
	addToArray(da, m1);
	assert(da->length == 1);
	Medicine m2 = createMedicine("nurofen", "300 mg", 20, 30);
	addToArray(da, m2);
	assert(da->length == 2);
	Medicine m3 = createMedicine("nurofen", "400 mg", 20, 35);
	addToArray(da, m3);
	assert(da->length == 3);
	assert(da->capacity == 4);
	destroyArray(da);
	//assert(da == NULL);
}