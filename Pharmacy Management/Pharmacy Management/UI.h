#pragma once
#include "MedicineController.h"

typedef struct {
	MedicineController *controller;
} UI;

UI createUI(MedicineController *medCtrl);

void printMenu();

/*
Verifies if a command is valid
Input: cmd - integer
Output: 1, if command is valid
0, otherwise
*/
int validCommand(int cmd);

/*
Reads an integer number from the keyboard. Asks for number while read errors encoutered.
Input: the message to be displayed when asking the user for input.
Returns the number.
*/
int readIntegerNumber(const char* message);

int addMedicineUI(UI *ui);
int updateMedicineUI(UI *ui);
int removeMedicineUI(UI *ui);

void printRepo(MedicineRepository *repo);
void searchUI(UI *ui);
void printAll(UI *ui);

void startUI(UI *ui);