#pragma once

typedef struct {
	char name[20];
	char concentration[10];
	int quantity;
	float price;
} Medicine;

/*
Creates a Medicine
Input:
- name: the medicine's name
- concentration: the medicine's concentration
- quantity: the medicine's quantity (in units)
- price: the medicine's price (in RON)
Output:
- a Medicine with the given attributes
*/
Medicine createMedicine(const char *name, const char *concentration, int quantity, int price);

/*
Gets a Medicine's name
Input: a pointer to a Medicine
Output: a pointer to the Medicine's name
*/
char *getName(Medicine *med);

/*
Gets the Medicine's concentration
Input: a pointer to a Medicine
Output: a pointer to the Medicine's concentration
*/
char *getConcentration(Medicine *med);

/*
Gets the Medicine's quantity
Input: a pointer to a Medicine
Output: Medicine's quantity (in units)
*/
int getQuantity(Medicine *med);

/*
Gets the Medicine's price
Input: a pointer to a Medicine
Output: Medicine's price (in RON)
*/
int getPrice(Medicine *med);

void toString(Medicine *medicine, char output[256]);

void testMedicine();