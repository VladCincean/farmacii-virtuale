#pragma once
#include "Medicine.h"
#include <string.h>

typedef struct {
	Medicine medicine;
	char operationType[30];
} Operation;

Operation createOperation(Medicine med, char operationType[]);
char* getOperationType(Operation* o);
Medicine getMedicine(Operation* o);

//----------------------------------------

typedef struct {
	Operation operations[100];
	int length;
} OperationStack;


OperationStack* createStack();

void destroyStack(OperationStack* s);

int isEmpty(OperationStack* s);

int isFull(OperationStack* s);

void push(OperationStack* s, Operation o);

Operation pop(OperationStack* s);