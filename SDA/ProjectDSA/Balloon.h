#pragma once

class Balloon{
private:
	double _xCoord;
	double _radius;

public:
	Balloon() : _xCoord(0), _radius(0) {};
	Balloon(double xCoord, double radius, bool hasArrow = false) :
		_xCoord(xCoord), _radius(radius) {};
	~Balloon() {};

	Balloon& operator=(const Balloon& b) {
		this->_xCoord = b._xCoord;
		this->_radius = b._radius;
		return *this;
	}

	bool operator==(const Balloon& b) const {
		return this->_xCoord == b._xCoord && this->_radius == b._radius;
	}

	void setXCoord(const double& xCoord) { _xCoord = xCoord; }
	void setRadius(const double& radius) { _radius = radius; }

	double getXCoord() const { return _xCoord; }
	double getRadius() const { return _radius; }
	double getRightBound() const { return _xCoord + _radius; }
	double getLeftBound() const{ return _xCoord - _radius; }
};
