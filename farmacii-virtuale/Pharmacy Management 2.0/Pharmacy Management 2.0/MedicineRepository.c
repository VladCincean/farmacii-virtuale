#include "MedicineRepository.h"
#include <stdlib.h>
#include <assert.h>

/*
Constructor of a MedicineRepository
Output: pointer to the new MedicineRepository
*/
MedicineRepository* createRepo() {
	MedicineRepository* repo = malloc(sizeof(MedicineRepository));
	if (repo == NULL) {
		return NULL;
	}
	repo->medDynArr = createArray(5);
	return repo;
}

/*
Destructor of a MedicineRepository
Input: pointer to a MedicineRepository
*/
void destroyRepo(MedicineRepository* repo) {
	if (repo == NULL)
		return;
	destroyArray(repo->medDynArr);
	free(repo);
	repo = NULL;
}

/*
Gets the length of a MedicineRepository
Input: pointer to a MedicineRepository
Output: length of the medicine repository
*/
int getRepoLength(MedicineRepository* repo) {
	if (repo == NULL)
		return 0;
	return getArrayLength(repo->medDynArr);
}

/*
Gets the Medicine found on a certain position in a MedicineRepository
Input:  - *repo: pointer to a MedicineReposiory
		- pos: position
Output: - Medicine, if the position is valid
		- "void" Medicine, otherwise
*/
Medicine getMedAtPos(MedicineRepository *repo, int pos) {
	if ((repo == NULL) || pos < 0 || pos > getArrayLength(repo->medDynArr)) {
		return createMedicine("", "", -1, 0);
	}
	return getElem(repo->medDynArr, pos);
}

/*
Checks if a Medicine exists in a MedicineRepository
Input:  - *repo: pointer to a medicine repository
		- *name: the Medicine's name
		- *concentration: the Medicine's concentration
Output: - the position in the repository data's structure of the Medicine uniquely identified by its name and its concentration, if found
		- -1, otherwise
*/
int find(MedicineRepository *repo, const char *name, const char *concentration) {
	if (repo == NULL)
		return -1;
	for (int i = 0; i < getRepoLength(repo); ++i) {
		if ((strcmp(getMedAtPos(repo, i).name, name) == 0) && (strcmp(getMedAtPos(repo, i).concentration, concentration) == 0)) {
			return i;
		}
	}
	return -1;
}

/*
Adds a medicine to the repository
If a product that already exists is added, its quantity will be modified (the new quantity is added to the existing one)
Input:  - *repo: pointer to a medicine repository
		- medicine: the medicine
Output: - 1, if Medicine successfully added
		- 0, otherwise
*/
int add(MedicineRepository *repo, Medicine medicine) {
	if (repo == NULL)
		return 0;
	if (find(repo, medicine.name, medicine.concentration) != -1) {
		/*int i = find(repo, medicine.name, medicine.concentration);
		repo->data[i].quantity += medicine.quantity;
		repo->data[i].price = medicine.price;*/
		int pos = find(repo, medicine.name, medicine.concentration);
		// we update the quantity
		medicine.quantity += getElem(repo->medDynArr, pos).quantity;
		setElem(repo->medDynArr, pos, medicine);
		return 1;
	}
	addToArray(repo->medDynArr, medicine);
	return 1;
}

/*
Removes a Medicine from a MedicineRepository
Input:  - *repo: pointer to a medicines' repository
		- *name: medicine to be removed's name
		- *concentration: medicine to be removed's concentration
Output: - 1, if Medicine successfully removed
		- 0, otherwise (i.e. Medicine not found)
*/
int remove2(MedicineRepository *repo, const char *name, const char *concentration) {
	int pos = find(repo, name, concentration);
	if (pos == -1) {
		return 0;
	}
	removeFromArray(repo->medDynArr, pos);
	return 1;
}

/*
Updates a medicine
Input:  - *repo: pointer a medicines' repository
		- newMed: Medicine to be updated
Output: - 1, if Medicine successfully updated
		- 0, otherwise (i.e. Medicine not found)
*/
int update(MedicineRepository *repo, Medicine newMed) {
	int pos = find(repo, newMed.name, newMed.concentration);
	if (pos == -1) {
		return 0;
	}
	setElem(repo->medDynArr, pos, newMed);
	return 1;
}

/*
...
*/
void sortRepo(MedicineRepository *repo, cmpF F) {
	int swaps = 1;
	while (swaps) {
		swaps = 0;
		for (int i = 0; i < getRepoLength(repo) - 1; ++i) {
			Medicine m1 = getElem(repo->medDynArr, i);
			Medicine m2 = getElem(repo->medDynArr, i + 1);
			if (F(&m1, &m2) > 0) {
				swapElems(repo->medDynArr, i, i + 1);
				swaps = 1;
			}
		}
	}
}

void testMedicineRepository() {
	Medicine ibuprofen = createMedicine("Ibuprofen", "600 mg", 20, 12);
	Medicine nurofen = createMedicine("Nurofen Forte", "400 mg", 20, 20);

	// init
	MedicineRepository* repo = createRepo();
	assert(getRepoLength(repo) == 0);

	// add
	assert(add(repo, ibuprofen) != 0);
	assert(getRepoLength(repo) == 1);
	assert(add(repo, nurofen) != 0);
	assert(getRepoLength(repo) == 2);
	assert(add(repo, nurofen) != 0);
	assert(getRepoLength(repo) == 2);
	//assert(getQuantity(repo->medDynArr->elements[find(repo, "Nurofen Forte", "400 mg")]) == 2 * getQuantity(&nurofen));
	//assert(getQuantity(&(getElem(repo->medDynArr, find(repo, "Nurofen Forte", "400 mg")))) == 2 * getQuantity(&nurofen));
	assert(repo->medDynArr->elements[find(repo, "Nurofen Forte", "400 mg")].quantity == 2 * getQuantity(&nurofen));
	
	// remove
	assert(remove2(repo, "Nurofen Forte", "400 mg") != 0);
	assert(remove2(repo, "Ibuprofen", "300 mg") == 0);
	assert(getRepoLength(repo) == 1);
	assert(remove2(repo, "Ibuprofen", "600 mg") != 0);
	assert(getRepoLength(repo) == 0);

	// destroy
	destroyRepo(repo);
}