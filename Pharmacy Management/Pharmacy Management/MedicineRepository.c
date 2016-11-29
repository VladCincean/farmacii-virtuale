#include "MedicineRepository.h"
#include <string.h>
#include <assert.h>

/*
Constructor of a MedicineRepository
Output: a new MedicineRepository
*/
MedicineRepository createRepo() {
	MedicineRepository repo;
	repo.length = 0;
	return repo;
}

/*
Gets the length of a MedicineRepository
Input: medRepo: a MedicineRepository
Output: the length of the medicine repository
*/
int getLength(MedicineRepository *medRepo) {
	return medRepo->length;
}

/*
Gets the Medicine found on a certain position in a MedicineRepository
Input:
		- medRepo: a MedicineReposiory
		- pos: position
Output: - Medicine, if the position is valid
		- "void" Medicine, otherwise
*/
Medicine getMedAtPos(MedicineRepository *medRepo, int pos) {
	if (pos < 0 || pos > getLength(medRepo)) {
		return createMedicine("", "", -1, 0);
	}
	return medRepo->data[pos];
}

/*
Checks if a Medicine exists in a MedicineRepository
Input:
		- medRepo: a MedicineRepository
		- name: the Medicine's name
		- concentration: the Medicine's concentration
Output: - the position in the repository data's structure of the Medicine uniquely identified by its name and its concentration, if found
		- -1, otherwise
*/
int find(MedicineRepository *medRepo, const char *name, const char *concentration) {
	for (int i = 0; i < getLength(medRepo); ++i) {
		if (strcmp(getMedAtPos(medRepo, i).name, name) == 0 && strcmp(getMedAtPos(medRepo, i).concentration, concentration) == 0) {
			return i;
		}
	}
	return -1;
}

/*
Adds a medicine to the repository
If a product that already exists is added, its quantity will be modified (the new quantity is added to the existing one)
Input:
		- medRepo: the medicines' repository
		- medicine: the medicine
Output: a pointer to the new MedicineRepository
*/
MedicineRepository *add(MedicineRepository *medRepo, Medicine medicine) {
	if (find(medRepo, medicine.name, medicine.concentration) != -1) {
		int i = find(medRepo, medicine.name, medicine.concentration);
		medRepo->data[i].quantity += medicine.quantity;
		medRepo->data[i].price = medicine.price;
	}
	else {
		medRepo->data[medRepo->length++] = medicine;
	}
	return medRepo;
}

/*
Removes a Medicine from a MedicineRepository
Input:
		- medRepo: a medicines' repository
		- name: medicine to be removed's name
		- concentration: medicine to be removed's concentration
Output: a pointer to the new MedicineRepository
		- NULL, if it was not changed (i.e. medicine not found)
*/
MedicineRepository *remove2(MedicineRepository *medRepo, const char *name, const char *concentration) {
	int pos = find(medRepo, name, concentration);
	if (pos == -1) {
		return NULL;
	}
	for (int i = pos; i < getLength(medRepo) - 1; ++i) {
		medRepo->data[i] = medRepo->data[i + 1];
	}
	--medRepo->length;
	return medRepo;
}

/*
Updates a medicine
Input:
		- medRepo: a medicines' repository
		- newMed: medicine to be updated
Output: a pointer to the new MedicineRepository
		- NULL, if nothing was changed (i.e. medicine not found)
*/
MedicineRepository *update(MedicineRepository *medRepo, Medicine newMed) {
	int pos = find(medRepo, newMed.name, newMed.concentration);
	if (pos == -1) {
		return NULL;
	}
	else {
		medRepo->data[pos].quantity = newMed.quantity;
		medRepo->data[pos].price = newMed.price;
	}
	return medRepo;
}

void testMedicineRepository() {
	Medicine ibuprofen = createMedicine("Ibuprofen", "600 mg", 20, 12);
	Medicine nurofen = createMedicine("Nurofen Forte", "400 mg", 20, 20);

	//init
	MedicineRepository repo = createRepo();
	assert(getLength(&repo) == 0);
	
	//add
	assert(add(&repo, ibuprofen) != NULL);
	assert(getLength(&repo) == 1);
	assert(add(&repo, nurofen) != NULL);
	assert(getLength(&repo) == 2);
	assert(add(&repo, nurofen) != NULL);
	assert(getLength(&repo) == 2);
	assert(getQuantity(&repo.data[find(&repo, "Nurofen Forte", "400 mg")]) == 2 * getQuantity(&nurofen));

	//remove
	assert(remove2(&repo, "Nurofen Forte", "400 mg") != NULL);
	assert(remove2(&repo, "Ibuprofen", "300 mg") == NULL);
	assert(getLength(&repo) == 1);
	assert(remove2(&repo, "Ibuprofen", "600 mg") != NULL);
	assert(getLength(&repo) == 0);
}