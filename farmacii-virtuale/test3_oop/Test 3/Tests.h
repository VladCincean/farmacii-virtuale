#pragma once
#include "Repository.h"
#include <assert.h>

using namespace std;

void testAll() {
	Repository r("players.txt");
	assert(r.playersByNationality("ROU") == 1);
	assert(r.playersByNationality("FRA") == 1);
	assert(r.playersByNationality("WWW") == 0);
}
