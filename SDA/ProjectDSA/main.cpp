#include "Tests.h"
#include "Tests.h"
#include "BalloonsGame.h"
#include <iostream>
#include <Windows.h>

using namespace std;

int main() {
	Tester tester;
	tester.testAll();
	system("pause");
	system("cls");

	//BalloonsGame game("ball1.txt");
	//BalloonsGame game("ball2.txt");
	//BalloonsGame game("test10.txt");
	BalloonsGame game("test100.txt");
	//BalloonsGame game("test1000.txt");
	//BalloonsGame game("test10000.txt");
	//BalloonsGame game("test100000.txt");

	game.runUsingRepr1();
	system("pause");

	game.runUsingRepr2();

	return 0;
}
