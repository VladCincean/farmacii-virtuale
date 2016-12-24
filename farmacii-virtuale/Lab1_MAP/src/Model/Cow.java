package Model;

/**
 * Created by vladc on 05.10.2016.
 */
public class Cow implements IAnimal {
    private int id;
    private String name;
    private int weight;

    public Cow(int id, String name, int weight) {
        this.id = id;
        this.name = name;
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    @Override
    public boolean equals(Object other) {
        if (other == null)
            return false;
        if (other == this)
            return true;
        if (!(other instanceof Cow))
            return false;

        Cow otherCow = (Cow)other;
        return (otherCow.getId() == this.getId());
    }
}
