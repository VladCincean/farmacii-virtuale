#include "MedicineController.h"
#include <string.h>
#include <stdlib.h>

/*
Creates a controller for medications
Input: medRepo - a repository of medications
Output: controller - the medications' controller
*/
MedicineController createController(MedicineRepository *medRepo) {
	MedicineController controller;
	controller.repo = medRepo;
	return controller;
}

/*
Adds a medicine
Input:
		- medCtrl: the medicines' controller
		- name: medicine to be added's name
		- concentration: medicine to be added's concentration
		- quantity: medicine to be added's quantity
		- price: medicine to be added's price
Output: 1, if successfully added
		0, otherwise
*/
int addMedicine(MedicineController *medCtrl, const char *name, const char *concentration, int quantity, int price) {
	Medicine medicine = createMedicine(name, concentration, quantity, price);
	medCtrl->repo = add(medCtrl->repo, medicine);
	return 1;
}

/*
Removes a medicine
Input:
		- medCtrl: the medicines' controller
		- name: medicine to be removed's name
		- concentration: medicine to be removed's concentration
Output: 1, if successfully removed
		0, otherwise
*/
int removeMedicine(MedicineController *medCtrl, const char *name, const char *concentration) {
	MedicineRepository* newRep = remove2(medCtrl->repo, name, concentration);
	if (newRep == 0) { // NULL
		return 0;
	}
	else {
		medCtrl->repo = newRep;
		return 1;
	}
}

/*
Updates a medicine
Input:
		- medCtrl: the medicines' controller
		- name: medicine to be updated's name
		- concentration: medicine to be updated's concentration
		- quantity: the new quantity
		- price: the new price
Output: 1, if successfully updated
		0, otherwise
*/
int updateMedicine(MedicineController *medCtrl, const char *name, const char *concentration, int quantity, int price) {
	Medicine newMed = createMedicine(name, concentration, quantity, price);
	MedicineRepository* newRep = update(medCtrl->repo, newMed);
	if (newRep == 0) /* NULL */ { // if medicine not found
		return 0;
	}
	else {
		medCtrl->repo = newRep;
		return 1;
	}
}

int cmpPrice(const Medicine *med1, const Medicine *med2) {
	if (getPrice(med1) > getPrice(med2)) {
		return 1;
	}
	if (getPrice(med1) < getPrice(med2)) {
		return -1;
	}
	if (getPrice(med1) == getPrice(med2)) {
		return 0;
	}
}

int cmpName(const Medicine *med1, const Medicine *med2) {
	return strcmp(getName(med1), getName(med2));
}

MedicineRepository priceRange(MedicineRepository *repo, int min, int max) {
	MedicineRepository res = createRepo();
	for (int i = 0; i <= getLength(repo); ++i) {
		Medicine m = repo->data[i];
		if (getPrice(&m) > min && getPrice(&m) < max) {
			add(&res, m);
		}
	}
	return res;
}

MedicineRepository search(MedicineController *medCtrl, const char *searchKey) {
	MedicineRepository res = createRepo();
	//create
	if (searchKey == "") {
		res = *(medCtrl->repo);
	}
	else{
		for (int i = 0; i <= getLength(medCtrl->repo); ++i) {
			Medicine m = medCtrl->repo->data[i];
			if (strstr(getName(&m), searchKey) != 0) {
				add(&res, m);
			}
		}
	}

	//sort
	qsort(medCtrl->repo, getLength(medCtrl->repo), sizeof(Medicine), cmpPrice);
	qsort(medCtrl->repo, getLength(medCtrl->repo), sizeof(Medicine), cmpName);

	//return
	return res;
}