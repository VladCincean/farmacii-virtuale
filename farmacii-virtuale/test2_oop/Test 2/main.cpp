#include "UI.h"

using namespace std;

int main() {
	Painting p1{ "William Turner", "Bridgewater Sea Piece", 1797 };
	Painting p2{ "Vincent van Gogh", "The Starry Night", 1889 };
	Painting p3{ "Francesco Hayez", "The Kiss", 1859 };
	Painting p4{ "A", "A", 1 };
	Painting p5{ "B", "B", 2 };

	Repository repoAll;

	repoAll.addPainting(p1);
	repoAll.addPainting(p2);
	repoAll.addPainting(p3);
	repoAll.addPainting(p4);
	repoAll.addPainting(p5);

	Repository repoSpecial;
	Controller ctrl{ repoAll, repoSpecial };
	UI ui{ ctrl };
	ui.run();

	return 0;
}
