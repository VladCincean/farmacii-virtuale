#include "Medicine.h"
#include <string.h>
#include <assert.h>
#include <stdio.h>

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
Medicine createMedicine(const char *name, const char *concentration, int quantity, int price) {
	Medicine med;
	strcpy(med.name, name);
	strcpy(med.concentration, concentration);
	med.quantity = quantity;
	med.price = price;
	return med;
}

char *getName(Medicine *med) {
	return med->name;
}

char *getConcentration(Medicine *med) {
	return med->concentration;
}

int getQuantity(Medicine *med) {
	return med->quantity;
}

int getPrice(Medicine *med) {
	return med->price;
}

/*
void setName(Medicine *med, const char *name) {
	*med->name = name;
}
void setConcentration(Medicine *med, const char *concentration) {
	*med->concentration = concentration;
}
void setQuantity(Medicine *med, int quantity) {
	med->quantity = quantity;
}
void setPrice(Medicine *med, int price) {
	med->price = price;
}
*/

void toString(Medicine *medicine, char output[256])
{
	sprintf(output, "%s, %s\n    |availability: %d bucs.\n    |price: %d RON\n",
		getName(medicine),
		getConcentration(medicine),
		getQuantity(medicine),
		getPrice(medicine));
}

void testMedicine() {
	char *name = "Ibuprofen";
	char *concentration = "600 mg";
	int quantity = 20;
	int price = 12;
	Medicine ibuprofen = createMedicine(name, concentration, quantity, price);
	assert(strcmp(getName(&ibuprofen), name) == 0);
	assert(strcmp(getConcentration(&ibuprofen), concentration) == 0);
	assert(getQuantity(&ibuprofen) == quantity);
	assert(getPrice(&ibuprofen) == price);
}