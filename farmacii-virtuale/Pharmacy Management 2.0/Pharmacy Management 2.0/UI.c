#include "UI.h"
#include "Utils.h"
#include <stdio.h>

UI* createUI(MedicineController *ctrl) {
	UI* ui = malloc(sizeof(UI));
	if (ui == NULL)
		return;
	ui->ctrl = ctrl;
	return ui;
}

void destroyUI(UI *ui) {
	if (ui == NULL)
		return;
	free(ui);
	ui = NULL;
}

void printMenu() {
	printf("\n1 - ADD a medication\n");
	printf("2 - UPDATE a medication\n");
	printf("3 - REMOVE a medication\n\n");

	printf("4 - SEARCH for a medication\n");
	printf("5 - SHOW ALL\n");
	printf("6 - [new] Show medications is SHORT SUPPLY\n\n");

	printf("7 - [new] UNDO\n");
	printf("8 - [new] REDO\n\n");

	printf("0 - EXIT\n");
}

//int validCommand(int cmd) {
//	if (cmd >= 0 && cmd <= 5)
//		return 1;
//	return 0;
//}

int addMedicineUI(UI *ui) {
	char name[40], concentration[10];
	int quantity, price;
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	quantity = readIntegerNumber("    quantity: ");
	price = readIntegerNumber("    price: ");
	return addMedicineCtrl(ui->ctrl, name, concentration, quantity, price); //return 1;
}

int removeMedicineUI(UI *ui) {
	char name[40], concentration[10];
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	return removeMedicineCtrl(ui->ctrl, name, concentration);
}

int updateMedicineUI(UI *ui) {
	char name[40], concentration[10];
	int quantity, price;
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	quantity = readIntegerNumber("    new quantity: ");
	price = readIntegerNumber("    new price: ");
	return updateMedicineCtrl(ui->ctrl, name, concentration, quantity, price);
}

void printRepo(MedicineRepository *repo) {
	if (getRepoLength(repo) == 0) {
		printf("Nothing here...\n");
		return;
	}
	for (int i = 0; i < getRepoLength(repo); ++i) {
		char s[256];
		Medicine m = getMedAtPos(repo, i);
		toString(&m, &s);
		printf("%2d. %s\n", i + 1, s);
	}
}

void searchUI(UI *ui) {
	char name[20];
	printf("    search for: ");
	scanf("%20s", &name);
	MedicineRepository* toPrint = searchByName(ui->ctrl, name);
	printRepo(toPrint);
	free(toPrint);
}

void printAll(UI *ui) {
	printRepo(getRepo(ui->ctrl));
}

void shortSupply(UI *ui) {
	int X = readIntegerNumber("    quantity less than: ");
	MedicineRepository* toPrint = searchByQuantity(ui->ctrl, X);
	printRepo(toPrint);
	free(toPrint);
}

void startUI(UI *ui) {
	printf("John's \"Smiles\" Pharmacy 2.0\n");
	while (1) {
		printMenu();
		int cmd = readIntegerNumber("Enter command: ");
		if (cmd == 0) {
			break;
		}
		switch (cmd) {
		case 1: {
			if (addMedicineUI(ui)) {
				printf("Medicine successfully added.\n");
			}
			else {
				printf("Error! Medicine not added.\n");
			}
			break;
		}
		case 2: {
			if (updateMedicineUI(ui)) {
				printf("Medicine successfully updated.\n");
			}
			else {
				printf("Error! Medicine not updated.\n");
			}
			break;
		}
		case 3: {
			if (removeMedicineUI(ui)) {
				printf("Medicine successfully removed.\n");
			}
			else {
				printf("Error! Medicine not found.\n");
			}
			break;
		}
		case 4: {
			searchUI(ui);
			break;
		}
		case 5: {
			printAll(ui);
			break;
		}
		case 6: {
			shortSupply(ui);
			break;
		}
		case 7: {
			int u = undo(ui->ctrl);
			if (u == 1)
				printf("Undo successfull.\n");
			else
				printf("Can't undo.\n");
			break;
		}
		case 8: {
			int r = redo(ui->ctrl);
			if (r == 1)
				printf("Redo successfull.\n");
			else
				printf("Can't redo.\n");
			break;
		}
		default:
			printf("Wrong command!\n");
			break;
		}
	}
	printf("Bye!\n");
}
