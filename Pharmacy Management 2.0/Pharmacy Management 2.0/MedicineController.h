#pragma once
#include "MedicineRepository.h"
#include "OperationStack.h"

typedef struct {
	MedicineRepository *repo;
	OperationStack *undoStack;
	OperationStack *redoStack;
} MedicineController;

/*
Creates a controller for medications
Input: pointer to a repository of medications
Output: pointer to the medications' controller
*/
MedicineController* createController(MedicineRepository *repo, OperationStack *undoStack, OperationStack *redoStack);

/*
Destroys a MedicineController
Input: pointer to the MedicineController
*/
void destroyController(MedicineController *ctrl);

MedicineRepository* getRepo(MedicineController *ctrl);

/*
Adds a medicine
Input:  - *ctrl: pointer to the medicines' controller
- *name: medicine to be added's name
- *concentration: medicine to be added's concentration
- quantity: medicine to be added's quantity
- price: medicine to be added's price
Output: 1, if Medicine successfully added
0, otherwise
*/
int addMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration, int quantity, int price);

/*
Removes a medicine
Input:  - *ctrl: pointer to the medicines' controller
- *name: medicine to be removed's name
- *concentration: medicine to be removed's concentration
Output: 1, if Medicine successfully removed
0, otherwise
*/
int removeMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration);

/*
Updates a medicine
Input:  - *ctrl: pointer to the medicines' controller
- *name: medicine to be updated's name
- *concentration: medicine to be updated's concentration
- quantity: the new quantity
- price: the new price
Output: 1, if Medicine successfully updated
0, otherwise
*/
int updateMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration, int quantity, int price);

/*
...
*/
MedicineRepository* searchByName(MedicineController *ctrl, const char *searchKey);

int undo(MedicineController* ctrl);

int redo(MedicineController* ctrl);