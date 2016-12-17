#pragma once
#include "Medicine.h"

typedef struct {
	Medicine data[300];
	int length;
} MedicineRepository;

/*
Constructor of a MedicineRepository
Output: a new MedicineRepository
*/
MedicineRepository createRepo();

/*
Gets the length of a MedicineRepository
Input: medRepo: a MedicineRepository
Output: the length of the medicine repository
*/
int getLength(MedicineRepository *medRepo);

/*
Gets the Medicine found on a certain position in a MedicineRepository
Input:
- medRepo: a MedicineReposiory
- pos: position
Output: - Medicine, if the position is valid
- "void" Medicine, otherwise
*/
Medicine getMedAtPos(MedicineRepository *medRepo, int pos);

/*
Checks if a Medicine exists in a MedicineRepository
Input:
- medRepo: a MedicineRepository
- name: the Medicine's name
- concentration: the Medicine's concentration
Output: - the position in the repository data's structure of the Medicine uniquely identified by its name and its concentration, if found
- -1, otherwise
*/
int find(MedicineRepository *medRepo, const char *name, const char *concentration);

/*
Adds a medicine to the repository
Input:
- medRepo: the medicines' repository
- medicine: the medicine
Output: a pointer to the new MedicineRepository
*/
MedicineRepository *add(MedicineRepository *medRepo, Medicine medicine);

/*
Removes a Medicine from a MedicineRepository
Input:
- medRepo: a medicines' repository
- name: medicine to be removed's name
- concentration: medicine to be removed's concentration
Output: a pointer to the new MedicineRepository
- NULL, if it was not changed (i.e. medicine not found)
*/
MedicineRepository *remove2(MedicineRepository *medRepo, const char *name, const char *concentration);

/*
Updates a medicine
Input:
- medRepo: a medicines' repository
- newMed: medicine to be updated
Output: a pointer to the new MedicineRepository
- NULL, if nothing was changed (i.e. medicine not found)
*/
MedicineRepository *update(MedicineRepository *medRepo, Medicine newMed);

void testMedicineRepository();