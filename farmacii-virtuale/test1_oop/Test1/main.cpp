#include "UI.h"
#include "Repository.h"
#include "Controller.h"

using namespace std;

int main() {
	
	testRepo();
	testCtrl();

	Repository repo;
	Controller ctrl(repo);

	ctrl.addCtrl("Fiat", "Bravo", 2007, "red");
	ctrl.addCtrl("Fiat", "Idea", 2003, "black");
	ctrl.addCtrl("Audi", "A5", 2007, "blue");
	ctrl.addCtrl("BMW", "Coupe", 2013, "pink");
	ctrl.addCtrl("Ford", "Fiesta", 1976, "yellow");

	UI ui(ctrl);

	ui.run();

	return 0;
}
