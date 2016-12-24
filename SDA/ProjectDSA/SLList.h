#pragma once

template <typename TE>
struct SLNode {
	SLNode* next;
	TE data;
};

template <typename TE>
class SLList {
public:

	class Iterator {
		friend class SLList<TE>;

	private:
		SLNode<TE>* current;

	public:
		inline Iterator(SLNode<TE>* c = nullptr) {
			current = c;
		}

		inline Iterator(const Iterator& it) {
			current = it.current;
		}

		inline Iterator& operator=(const Iterator& it) {
			current = it.current;
			return *this;
		}

		inline Iterator& operator++() { // ++ prefix
			current = current->next;
			return *this;
		}

		inline Iterator operator++(int) { // postfix ++
			Iterator itCopy(*this);
			current = current->next;
			return itCopy;
		}

		inline TE& operator*() const {
			return current->data;
		}

		inline TE* operator->() const {
			return current;
		}

		inline bool operator==(const Iterator& it) const {
			return current == it.current;
		}

		inline bool operator!=(const Iterator& it) const {
			return current != it.current;
		}
	};

private:
	SLNode<TE>* head;
	int size;

public:
	inline SLList() : head(nullptr), size(0) {}
	
	inline SLList(const SLList<TE>& l) : head(nullptr), size(0) {
		for (Iterator it = l.begin(); it != l.end(); ++it)
			insertBack(*it);
	}

	inline ~SLList() {
		while (head != nullptr) {
			SLNode<TE>* newHead = head->next;
			delete head;
			head = newHead;
		}
	}

	inline SLNode<TE>* getHead() {
		return head;
	}

	inline void insertFront(const TE& e) {
		SLNode<TE>* nod = new SLNode<TE>;
		nod->data = e;
		nod->next = head;
		head = nod;
		size++;
	}

	inline void insertBack(const TE& e) {
		SLNode<TE>* nod = head;
		while (nod != nullptr && nod->next != nullptr)
			nod = nod->next;
		if (nod == nullptr)
			insertFront(e);
		else {
			SLNode<TE>* last = new SLNode<TE>;
			last->data = e;
			last->next = nullptr;
			nod->next = last;
		}
		size++;
	}

	inline void insertAfter(Iterator& it, const TE& e) {
		SLNode<TE>* nod = new SLNode<TE>;
		nod->data = e;
		nod->next = it.current->next;
		it.current->next = nod;
		size++;
	}

	inline void eraseAfter(Iterator& it) {
		SLNode<TE>* nod = it.current->next;
		if (it.current->next != nullptr)
			it.current->next = it.current->next->next;
		delete nod;
	}

	inline void insertHere(Iterator& it, const TE& e) {
		/* "move" the VALUE of the value of the node pointed by the iterator
		 * to the newly inserted node (after *it) and assign it the value 'e'
		 */
		SLNode<TE>* nod = new SLNode<TE>;
		nod->data = it.current->data;
		it.current->data = e;
		nod->next = it.current->next;
		it.current->next = nod;
	}

	inline void eraseHere(Iterator& it) {
		/*SLNode* nod = *(it.current);
		*(it.current) = nod->next();
		delete nod;*/
		SLNode<TE>* nod = it.current;
		while (nod->next != nullptr) {
			nod->data = nod->next->data;
			if (nod->next->next == nullptr) {
				delete nod->next;
				nod->next = nullptr;
				break;
			}
			nod = nod->next;
		}
	}

	inline Iterator begin() {
		return Iterator(head);
	}

	inline Iterator end() {
		return Iterator();
	}
};
