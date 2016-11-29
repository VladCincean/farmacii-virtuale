#include "MedicineController.h"
#include "OperationStack.h"
#include "Utils.h"
#include <string.h>
#include <stdlib.h>

/*
Creates a controller for medications
Input: pointer to a repository of medications
Output: pointer to the medications' controller
*/
MedicineController* createController(MedicineRepository *repo, OperationStack *undoStack, OperationStack *redoStack) {
	MedicineController* ctrl = malloc(sizeof(MedicineController));
	if (ctrl == NULL)
		return NULL;
	ctrl->repo = repo;
	ctrl->undoStack = undoStack;
	ctrl->redoStack = redoStack;
	return ctrl;
}

/*
Destroys a MedicineController
Input: pointer to the MedicineController
*/
void destroyController(MedicineController *ctrl) {
	if (ctrl == NULL)
		return;
	free(ctrl);
	ctrl = NULL;
}

MedicineRepository* getRepo(MedicineController *ctrl) {
	return ctrl->repo;
}

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
int addMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration, int quantity, int price) {
	Medicine medicine = createMedicine(name, concentration, quantity, price);
	int E = add(ctrl->repo, medicine);
	if (E == 1) {
		Operation o = createOperation(medicine, "add");
		push(ctrl->undoStack, o);
	}
	return E;
}

/*
Removes a medicine
Input:  - *ctrl: pointer to the medicines' controller
		- *name: medicine to be removed's name
		- *concentration: medicine to be removed's concentration
Output: 1, if Medicine successfully removed
		0, otherwise
*/
int removeMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration) {
	Medicine med = getMedAtPos(ctrl->repo, find(ctrl->repo, name, concentration));
	int E = remove2(ctrl->repo, name, concentration);
	if (E == 1) {
		Operation o = createOperation(med, "remove");
		push(ctrl->undoStack, o);
	}
	return E;
}

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
int updateMedicineCtrl(MedicineController *ctrl, const char *name, const char *concentration, int quantity, int price) {
	Medicine oldMed = getMedAtPos(ctrl->repo, find(ctrl->repo, name, concentration));
	Medicine newMed = createMedicine(name, concentration, quantity, price);
	int E = update(ctrl->repo, newMed);
	if (E == 1) {
		Operation o = createOperation(oldMed, "update");
		push(ctrl->undoStack, o);
	}
	return E;
}

/*
...
*/
MedicineRepository* searchByName(MedicineController *ctrl, const char *searchKey) {
	MedicineRepository* res = createRepo();
	// create
	if (searchKey == "") {
		res = ctrl->repo;
	}
	else {
		for (int i = 0; i < getRepoLength(ctrl->repo); ++i) {
			Medicine m = getMedAtPos(ctrl->repo, i);
			if (strstr(getName(&m), searchKey) != 0) {
				add(res, m);
			}
		}
	}

	// sort (bubble sort)
	sortRepo(res, cmpPrice);
	sortRepo(res, cmpName);
	
	// return
	return res;
}

MedicineRepository* searchByQuantity(MedicineController* ctrl, int X) {
	MedicineRepository* res = createRepo();
	for (int i = 0; i < getRepoLength(ctrl->repo); ++i) {
		Medicine m = getMedAtPos(ctrl->repo, i);
		if (getQuantity(&m) < X)
			add(res, m);
	}
	sortRepo(res, cmpQuantity);
	return res;
}

int undo(MedicineController* ctrl) {
	if (isEmpty(ctrl->undoStack))
		return 0;
	Operation o = pop(ctrl->undoStack);
	if (strcmp(getOperationType(&o), "add") == 0) {
		Medicine med = getMedicine(&o);
		/*char name[20] = getName(&med);
		char concentration[10] = getConcentration(&med);*/
		remove2(ctrl->repo, getName(&med), getConcentration(&med));
		push(ctrl->redoStack, o);
		return 1;
	}
	if (strcmp(getOperationType(&o), "remove") == 0) {
		Medicine med = getMedicine(&o);
		add(ctrl->repo, med);
		push(ctrl->redoStack, o);
		return 1;
	}
	if (strcmp(getOperationType(&o), "update") == 0) {
		Medicine med = getMedicine(&o);
		Medicine oldMed = getMedAtPos(ctrl->repo, find(ctrl->repo, getName(&med), getConcentration(&med)));
		Operation o = createOperation(oldMed, "update");
		update(ctrl->repo, oldMed);
		return 1;
	}
	if (strcmp(getOperationType(&o), "") == 0)
		return 0;
}

int redo(MedicineController* ctrl) {
	if (isEmpty(ctrl->redoStack))
		return 0;
	Operation o = pop(ctrl->redoStack);
	if (strcmp(getOperationType(&o), "add") == 0) {
		Medicine med = getMedicine(&o);
		add(ctrl->repo, med);
		push(ctrl->undoStack, o);
		return 1;
	}
	if (strcmp(getOperationType(&o), "remove") == 0) {
		Medicine med = getMedicine(&o);
		//char name[20] = getName(&med);
		//char concentration[10] = getConcentration(&med);
		remove2(ctrl->repo, getName(&med), getConcentration(&med));
		push(ctrl->undoStack, o);
		return 1;
	}
	if (strcmp(getOperationType(&o), "update") == 0) {
		Medicine med = getMedicine(&o);
		Medicine oldMed = getMedAtPos(ctrl->repo, find(ctrl->repo, getName(&med), getConcentration(&med)));
		Operation o = createOperation(oldMed, "update");
		update(ctrl->repo, oldMed);
		return 1;
	}
	if (strcmp(getOperationType(&o), "") == 0)
		return 0;
}