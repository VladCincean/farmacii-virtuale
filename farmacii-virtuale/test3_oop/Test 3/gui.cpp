#include "gui.h"

using namespace std;

GUI::GUI(Controller& c, QWidget *parent)
	: ctrl(c), QMainWindow(parent)
{
	ui.setupUi(this);
	this->playersVector = this->ctrl.getAll();
	this->populatePlayersList();
	this->connectSignalsAndSlots();
}

GUI::~GUI()
{

}

void GUI::connectSignalsAndSlots() {
	QObject::connect(ui.playersListWidget, SIGNAL(itemSelectionChanged()), this, SLOT(updateLineEdits()));
	QObject::connect(ui.sortButton, SIGNAL(clicked()), this, SLOT(sortPlayers()));
	QObject::connect(ui.showPlayersButton, SIGNAL(clicked()), this, SLOT(showGivenNationality()));
}

void GUI::populatePlayersList() {
	ui.playersListWidget->clear();
	for (Player p : this->playersVector) {
		ui.playersListWidget->addItem(QString::fromStdString(p.getName() + " | " + p.getTeam()));
	}
}

void GUI::updateLineEdits() {
	int index = ui.playersListWidget->currentIndex().row();
	Player p = this->playersVector[index];
	ui.nameLineEdit->setText(QString::fromStdString(p.getName()));
	ui.nationalityLineEdit->setText(QString::fromStdString(p.getNationality()));
	ui.teamLineEdit->setText(QString::fromStdString(p.getTeam()));
	ui.goalsLineEdit->setText(QString::number(p.getGoals()));
}

void GUI::sortPlayers() {
	this->playersVector = this->ctrl.getAllSorted();
	this->populatePlayersList();
}

void GUI::showGivenNationality() {
	string nationality = ui.showByNationalityLineEdit->text().toStdString();
	int n = this->ctrl.playersByNationality(nationality);
	ui.numberOfPlayersLineEdit->setText(QString::number(n));
}
