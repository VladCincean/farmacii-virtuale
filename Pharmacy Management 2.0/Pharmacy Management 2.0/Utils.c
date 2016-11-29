#include "Utils.h"
#include <stdio.h>

/*
Reads an integer number from the keyboard. Asks for number while read errors encoutered.
Input: the message to be displayed when asking the user for input.
Returns the number.
*/
int readIntegerNumber(const char* message)
{
	char s[16];
	int res = 0;
	int flag = 0;
	int r = 0;

	while (flag == 0)
	{
		printf(message);
		scanf("%s", s);

		r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
		flag = (r == 1);
		if (flag == 0)
			printf("Error reading number!\n");
	}
	return res;
}

int cmpPrice(const Medicine *med1, const Medicine *med2) {
	if (getPrice(med1) > getPrice(med2)) {
		return 1;
	}
	if (getPrice(med1) < getPrice(med2)) {
		return -1;
	}
	if (getPrice(med1) == getPrice(med2)) {
		return 0;
	}
}

int cmpQuantity(const Medicine *med1, const Medicine *med2) {
	if (getQuantity(med1) > getQuantity(med2)) {
		return 1;
	}
	if (getQuantity(med1) < getQuantity(med2)) {
		return -1;
	}
	if (getQuantity(med1) == getQuantity(med2)) {
		return 0;
	}
}

int cmpName(const Medicine *med1, const Medicine *med2) {
	return strcmp(getName(med1), getName(med2));
}

