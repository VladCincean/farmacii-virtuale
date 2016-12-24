package Controller;

import Model.*;
import Repository.*;

/**
 * Created by vladc on 05.10.2016.
 */
public class Controller {
    private IRepository repo;

    public Controller(IRepository repo) {
        this.repo = repo;
    }

    public void add(IAnimal a) throws Exception {
        repo.add(a);
    }

    public void remove(IAnimal a) throws Exception {
        repo.remove(a);
    }

    // returns all animals that have weight > 3 kg
    public IAnimal[] solve() {
        IAnimal[] all = repo.getAll();
        IAnimal[] result = null;
        int count = 0;
        int current = 0;

        // step 1. count the length of the result
        for (int i = 0; i < all.length; i++) {
            if (all[i].getWeight() > 3)
                count++;
        }

        // step 2. create the result array
        if (count > 0) {
            result = new IAnimal[count];
            for (int i = 0; i < all.length; i++) {
                if (all[i].getWeight() > 3) {
                    result[current] = all[i];
                    current++;
                }
            }
        }

        // step 3. return the result
        return result;
    }
}
