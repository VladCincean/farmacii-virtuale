#include "gui.h"
#include <QtWidgets/QApplication>
#include <QtWidgets\qmessagebox.h>
#include "Tests.h"

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	testAll();
	//try {
		Repository r("players.txt");
		Controller c(r);
		GUI w(c);
		w.show();
	//}
	//catch (std::exception& e) {
	//	QMessageBox::critical(NULL, "Error", QString::fromStdString(e.what()));
	//	a.quit();
	//}
	return a.exec();
}
