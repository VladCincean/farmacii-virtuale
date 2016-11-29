#include "UI.h"
#include <crtdbg.h>
#include <stdio.h>

int main() {
	// tests
	testMedicine();
	testMedicineRepository();


	// init
	MedicineRepository* repo = createRepo();
	if (repo == NULL) {
		printf("Memory error! Can't create MedicineRepository.\n");
		return 1;
	}
	OperationStack* undoStack = createStack();
	printf("1");
	OperationStack* redoStack = createStack();
	MedicineController* ctrl = createController(repo, undoStack, redoStack);
	if (ctrl == NULL) {
		printf("Memory error! Can't create MedicineController.\n");
		return 1;
	}

	addMedicineCtrl(ctrl, "Nurofen", "200mg", 20, 15);
	addMedicineCtrl(ctrl, "Nurofen", "300mg", 10, 20);
	addMedicineCtrl(ctrl, "Nurofen Forte", "300mg", 20, 25);
	addMedicineCtrl(ctrl, "Ceai musetel 50g", "-", 25, 10);
	addMedicineCtrl(ctrl, "Ceai merisor 30g", "-", 5, 12);
	addMedicineCtrl(ctrl, "Ceai de afin 50g", "-", 10, 18);
	addMedicineCtrl(ctrl, "Ceai sunatoare 50g", "-", 8, 15);
	addMedicineCtrl(ctrl, "Lecitina", "1000mg", 20, 20);
	addMedicineCtrl(ctrl, "Magnesium + B6", "250mg/1.4mg", 20, 50);

	UI* ui = createUI(ctrl);
	if (ui == NULL) {
		printf("Memory Error! Can't create UI.\n");
		return 1;
	}

	// run
	startUI(ui);

	// dealocate memory
	destroyUI(ui);
	destroyController(ctrl);
	destroyStack(undoStack);
	destroyStack(redoStack);
	destroyRepo(repo);

	// verify memory
	_CrtDumpMemoryLeaks();

	// return
	return 0;
}