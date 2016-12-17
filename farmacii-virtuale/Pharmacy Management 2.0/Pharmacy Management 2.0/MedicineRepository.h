#pragma once
#include "Medicine.h"
#include "DynamicArray.h"

typedef struct {
	DynamicArray* medDynArr;
} MedicineRepository;

typedef int(*cmpF)(Medicine* m1, Medicine* m2);

/*
Constructor of a MedicineRepository
Output: pointer to the new MedicineRepository
*/
MedicineRepository* createRepo();

/*
Destructor of a MedicineRepository
Input: pointer to a MedicineRepository
*/
void destroyRepo(MedicineRepository* repo);

/*
Gets the length of a MedicineRepository
Input: pointer to a MedicineRepository
Output: length of the medicine repository
*/
int getRepoLength(MedicineRepository* repo);

/*
Gets the Medicine found on a certain position in a MedicineRepository
Input:  - *repo: pointer to a MedicineReposiory
- pos: position
Output: - Medicine, if the position is valid
- "void" Medicine, otherwise
*/
Medicine getMedAtPos(MedicineRepository *repo, int pos);

/*
Checks if a Medicine exists in a MedicineRepository
Input:  - *repo: pointer to a medicine repository
- *name: the Medicine's name
- *concentration: the Medicine's concentration
Output: - the position in the repository data's structure of the Medicine uniquely identified by its name and its concentration, if found
- -1, otherwise
*/
int find(MedicineRepository *repo, const char *name, const char *concentration);

/*
Adds a medicine to the repository
If a product that already exists is added, its quantity will be modified (the new quantity is added to the existing one)
Input:  - *repo: pointer to a medicine repository
- medicine: the medicine
Output: - 1, if Medicine successfully added
- 0, otherwise
*/
int add(MedicineRepository *repo, Medicine medicine);

/*
Removes a Medicine from a MedicineRepository
Input:  - *repo: pointer to a medicines' repository
- *name: medicine to be removed's name
- *concentration: medicine to be removed's concentration
Output: - 1, if Medicine successfully removed
- 0, otherwise (i.e. Medicine not found)
*/
int remove2(MedicineRepository *repo, const char *name, const char *concentration);

/*
Updates a medicine
Input:  - *repo: pointer a medicines' repository
- newMed: Medicine to be updated
Output: - 1, if Medicine successfully updated
- 0, otherwise (i.e. Medicine not found)
*/
int update(MedicineRepository *repo, Medicine newMed);

/*
...
*/
void sortRepo(MedicineRepository *repo, cmpF F);

void testMedicineRepository();