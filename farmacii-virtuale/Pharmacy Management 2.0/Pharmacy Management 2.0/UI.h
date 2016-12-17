#pragma once
#include "MedicineController.h"

typedef struct {
	MedicineController* ctrl;
} UI;

UI* createUI(MedicineController *ctrl);
void destroyUI(UI *ui);
void startUI(UI *ui);