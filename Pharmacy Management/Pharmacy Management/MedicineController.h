#pragma once
#include "MedicineRepository.h"

typedef struct {
	MedicineRepository *repo;
}MedicineController;

/*
Creates a controller for medications
Input: medRepo - a repository of medications
Output: controller - the medications' controller
*/
MedicineController createController(MedicineRepository *medRepo);

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
int addMedicine(MedicineController *medCtrl, const char *name, const char *concentration, int quantity, int price);

/*
Removes a medicine
Input:
		- medCtrl: the medicines' controller
		- name: medicine to be removed's name
		- concentration: medicine to be removed's concentration
Output: 1, if successfully removed
		0, otherwise
*/
int removeMedicine(MedicineController *medCtrl, const char *name, const char *concentration);

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
int updateMedicine(MedicineController *medCtrl, const char *name, const char *concentration, int quantity, int price);

//MedicineRepository *getMedicineRepository(MedicineController *medCtrl);

int cmpPrice(const Medicine *med1, const Medicine *med2);
int cmpName(const Medicine *med1, const Medicine *med2);

MedicineRepository priceRange(MedicineRepository *repo, int min, int max);

MedicineRepository search(MedicineController *medCtrl, const char *search_key);