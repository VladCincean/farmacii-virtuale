package Model;

/**
 * Created by vladc on 05.10.2016.
 */
public interface IAnimal {
    int getWeight();
    String getName();
    int getId();
    @Override
    boolean equals(Object other);
}