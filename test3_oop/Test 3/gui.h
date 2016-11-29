#ifndef GUI_H
#define GUI_H

#include <QtWidgets/QMainWindow>
#include "ui_gui.h"
#include "Controller.h"

class GUI : public QMainWindow
{
	Q_OBJECT

public:
	GUI(Controller& c, QWidget *parent = 0);
	~GUI();

private:
	Ui::GUIClass ui;
	Controller ctrl;

	std::vector<Player> playersVector;

	void connectSignalsAndSlots();

	void populatePlayersList();

public slots:
	void updateLineEdits();
	void sortPlayers();
	void showGivenNationality();
};

#endif // GUI_H
