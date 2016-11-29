#pragma once
#include "Medicine.h"

/*
Reads an integer number from the keyboard. Asks for number while read errors encoutered.
Input: the message to be displayed when asking the user for input.
Returns the number.
*/
int readIntegerNumber(const char* message);

int cmpPrice(const Medicine *med1, const Medicine *med2);

int cmpQuantity(const Medicine *med1, const Medicine *med2);

int cmpName(const Medicine *med1, const Medicine *med2);