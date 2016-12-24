import Model.*;
import Repository.*;
import Controller.*;
import View.*;

/**
 * Created by vladc on 08.10.2016.
 */
public class Main {
    private static int repository_capacity = 100;

    public static void main(String[] args) {
        IRepository repo = new InMemoryRepository(repository_capacity);
        Controller  ctrl = new Controller(repo);
        View        ui   = new View(ctrl);

        try {
            populate(ctrl);
            ui.run();
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }

    private static void populate(Controller ctrl) throws Exception {
        ctrl.add(new Poultry(1, "Joe", 2));
        ctrl.add(new Pig(1, "John", 110));
        ctrl.add(new Pig(2, "Zob", 102));
        ctrl.add(new Cow(1, "Johan", 450));
        ctrl.add(new Poultry(2, "Lisa", 3));
        ctrl.add(new Poultry(3, "Bob", 4));
    }
}
