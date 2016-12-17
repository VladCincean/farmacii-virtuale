#pragma once
#include <string>

using namespace std;


class Painting {
private:
	string title;
	string artist;
	int year;
public:
	Painting() {
		title = ""; artist = ""; year = 0;
	}
	Painting(string artist, string title, int year) {
		this->title = title;
		this->artist = artist;
		this->year = year;
	}
	inline string getTitle() { return title; }
	inline string getArtist() { return artist; }
	inline int getYear() { return year; }
};