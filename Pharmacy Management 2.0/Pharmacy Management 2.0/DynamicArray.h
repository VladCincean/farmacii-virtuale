#pragma once
#include "Medicine.h"

typedef Medicine TElem;

typedef struct {
	TElem *elements;
	int length;
	int capacity;
} DynamicArray ;

/*
Creates a dynamic array of TElems = medicines with given capacity
Input: capacity (positive integer) - maximum capacity of the array
Output: a pointer to the dynamic array just created
*/
DynamicArray* createArray(int capacity);

/*
Doubles a DynamicArray's capacity, allocating more space
Input: pointer to the DynamicArray
*/
void resizeArray(DynamicArray* da);

/*
Destroys a DynamicArray
Input: pointer to the DynamicArray
*/
void destroyArray(DynamicArray* da);

void addToArray(DynamicArray* da, TElem elem);

void removeFromArray(DynamicArray* da, int pos);

int getArrayLength(DynamicArray* da);

TElem getElem(DynamicArray* da, int pos);

void setElem(DynamicArray*da, int pos, TElem elem);

void swapElems(DynamicArray* da, int pos1, int pos2);

void testDynamicArray();