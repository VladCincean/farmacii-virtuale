package Repository;

import Model.*;
import java.lang.Exception;

/**
 * Created by vladc on 05.10.2016.
 */
public class InMemoryRepository implements IRepository {
    private IAnimal[] elements;
    private int capacity;
    private int length;

    public InMemoryRepository(int capacity) {
        this.elements = new IAnimal[capacity];
        this.capacity = capacity;
        this.length = 0;
    }

    public void add(IAnimal a) throws Exception {
        if (this.length == this.capacity) {
            throw new Exception("Error. Cannot add. Repository is already full.");
        }
        for (int i = 0; i < this.length; i++) {
            if (this.elements[i].equals(a)) {
                throw new Exception("Error. Cannot add. Animal already exists. Use a different id.");
            }
        }
        this.elements[this.length] = a;
        this.length++;
    }

//    public void remove(IAnimal a) throws Exception {
//        IAnimal[] new_elements;
//        int new_length;
//
//        new_elements = new IAnimal[capacity];
//        new_length = 0;
//        for (int i = 0; i < this.length; i++) {
//            if (!this.elements[i].equals(a)) {
//                new_elements[new_length] = this.elements[i];
//                new_length++;
//            }
//        }
//        if (new_length == this.length) {
//            throw new Exception("Error. Nothing was removed.");
//        }
//        this.elements = new_elements;
//        this.length = new_length;
//    }

    public void remove(IAnimal a) throws Exception {
        boolean removedAtLeastOne = false;

        for (int i = 0; i < this.length; i++) {
            if (this.elements[i].equals(a)) {
                for (int j = i; j < this.length - 1; j++)
                    this.elements[j] = this.elements[j + 1];
                this.length--;
                i--;
                removedAtLeastOne = true;
            }
        }
        if (!removedAtLeastOne) {
            throw new Exception("Error. Nothing was removed.");
        }
    }

    public IAnimal[] getAll() {
        IAnimal[] ret = new IAnimal[this.length];
        for (int i = 0; i < this.length; i++)
            ret[i] = this.elements[i];
        return ret;
    }
}
