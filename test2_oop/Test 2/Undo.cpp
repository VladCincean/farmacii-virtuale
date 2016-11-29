#include "Undo.h"

using namespace std;

void UndoMoveOperation::executeUndo() {
	Painting p = this->specialPaintingsRepo.getAll().back();
	this->specialPaintingsRepo.removePainting(p);
	this->paintingRepo.addPainting(p);
}

void UndoRemoveOperation::executeUndo() {
	this->paintingRepo.addPainting(this->p);
}
