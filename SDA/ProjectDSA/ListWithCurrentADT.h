#pragma once

template <typename TE>
class ListWithCurrentADT {
public:
	
	// default constructor
	ListWithCurrentADT() {}

	// copy constructor
	ListWithCurrentADT(ListWithCurrentADT<TE>& l) {}

	// virtual destructor
	virtual ~ListWithCurrentADT() {}
	

	/*
	Get the current element from the list
	@pre: the current element is valid
		  the list is not empty
	@post: e:TE is the element pointed by current
	@return: the current element
	*/
	virtual TE getCurrent() = 0;

	/*
	Modify the current element from the list
	@pre: the current element is valid
		  the list is not empty
	@post: the current element is modified to e:TE
	*/
	virtual void setCurrent(const TE e) = 0;

	/*
	Remove the current element from the list
	@pre: the current element is valid
		  the list is not empty
	@post: the current element is removed from the list
	*/
	virtual void delCurrent() = 0;

	/*
	Change the current to the first element from the list
	@pre: the list is not empty
	@post: current points to the first element in the list
	*/
	virtual void first() = 0;

	/*
	Change the current to the last element from the list
	@pre: the list is not empty
	@post: current points to the last element in the list
	*/
	virtual void last() = 0;

	/*
	Change the current to the next element from the list
	@pre: the list is not empty
		  current is not the last element in the list
	@post: current points to the next element in the list
	*/
	virtual void next() = 0;

	/*
	Checks if the current element has a next element or not
	@pre: the list is not empty
	@post: -
	@return: true, if current is not on the last position
			false, otherwise
	*/
	virtual bool hasNext() = 0;

	/*
	Change the current to the previous element from the list
	@pre: the list is not empty
		  current is not the first element in the list
	@post: current points to the previous element in the list
	*/
	virtual void prev() = 0;

	/*
	Checks if the current element has a previous element or not
	@pre: the list is not empty
	@post: -
	@return: true, if current is not on the first position
			false, otherwise
	*/
	virtual bool hasPrev() = 0;

	/*
	Check if the current element from the list is valid or not
	@pre: -
	@post:
	@return: true, if current is valid (i.e. it can be retrieved by getCurrent())
			false, otherwise
	*/
	virtual bool valid() = 0;

	/*
	Check if a certain element is contained in the list or not
	@pre: e:TE
	@post: -
	@return: true, if e:TE is in the list
			false, otherwise
	*/
	virtual bool exists(const TE e) = 0;

	/*
	Check if the list is empty or not
	@pre: -
	@post: -
	@return: true, if the list is empty (i.e. it does not contain any element)
		    false, otherwise
	*/
	virtual bool isEmpty() = 0;

	/*
	Get the number of elements contained in the list
	@pre: -
	@post: -
	@return: returns the size of the list (i.e. the number of elements)
	*/
	virtual int getSize() = 0;

	/*
	Add a new element in the front of the list
	@pre: e:TE
	@post: e:TE is added on the first position in the list
		   current is changed to the element just added
	*/
	virtual void addFront(const TE e) = 0;

	/*
	Add a new element in the back of the list
	@pre: e:TE
	@post: e:TE is added on the last position in the list
		   current is changed to the element just added
	*/
	virtual void addBack(const TE e) = 0;

	/*
	Add a new element before the current element in the list
	@pre: e:TE
	@post: e:TE is added in the list just before the current element
		   current is changed to the element just added
	*/
	virtual void addBefore(const TE e) = 0;

	/*
	Add a new element after the current element in the list
	@pre: e:TE
	@post: e:TE is added in the list just after the current element
		   current is changed to the element just added
	*/
	virtual void addAfter(const TE e) = 0;
};
