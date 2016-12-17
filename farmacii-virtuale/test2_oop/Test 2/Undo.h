#pragma once
#include "Painting.h"
#include "Repository.h"

using namespace std;

class UndoOperation {
public:
	virtual void executeUndo() = 0;
};

class UndoRemoveOperation : public UndoOperation {
private:
	Repository& paintingRepo;
	Painting p;
public:
	UndoRemoveOperation(Repository& repo, Painting p): paintingRepo(repo) {
		//this->paintingRepo = repo;
		this->p = p;
	}
	void executeUndo() override;
};

class UndoMoveOperation : public UndoOperation {
private:
	Repository& paintingRepo;
	Repository& specialPaintingsRepo;
public:
	UndoMoveOperation(Repository& ar, Repository& sr): paintingRepo(ar), specialPaintingsRepo(sr){
	/*	this->paintingRepo = ar;
		this->specialPaintingsRepo = sr;*/
	};
	void executeUndo() override;
};
