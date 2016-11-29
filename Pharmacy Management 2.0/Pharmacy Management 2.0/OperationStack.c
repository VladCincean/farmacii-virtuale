#include "OperationStack.h"
#include <string.h>
#include <stdlib.h>

Operation createOperation(Medicine med, char operationType[]) {
	Operation o;
	o.medicine = med;
	strcpy(o.operationType, operationType);
	return o;
}

char* getOperationType(Operation* o) {
	return o->operationType;
}

Medicine getMedicine(Operation* o){
	return o->medicine;
}

//--------------------------

OperationStack* createStack() {
	OperationStack* s = malloc(sizeof(OperationStack));
	s->length = 0;
	return s;
}

void destroyStack(OperationStack* s) {
	if (s == NULL)
		return;
	free(s);
	s = NULL;
}

int isEmpty(OperationStack* s) {
	return (s->length == 0);
}

int isFull(OperationStack* s) {
	return (s->length == 100);
}

void push(OperationStack* s, Operation o) {
	if (isFull(s))
		return;
	s->operations[s->length] = o;
	s->length++;
}

Operation pop(OperationStack* s) {
	Operation o = createOperation(createMedicine("", "", 0, -1), "");
	if (isEmpty(s))
		return o;
	s->length--;
	return s->operations[s->length];
}