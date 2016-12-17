#include "UI.h"

int main() {
	// run tests
	testMedicine();
	testMedicineRepository();
	
	// init
	MedicineRepository repo = createRepo();
	MedicineController ctrl = createController(&repo);
	UI ui = createUI(&ctrl);

	// run
	startUI(&ui);

	return 0;
}