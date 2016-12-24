package Repository;

import Model.*;
import java.lang.Exception;

/**
 * Created by vladc on 05.10.2016.
 */
public interface IRepository {
    void add(IAnimal a) throws Exception;
    void remove(IAnimal a) throws Exception;
    IAnimal[] getAll();
}
