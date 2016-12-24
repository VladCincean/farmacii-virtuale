package View;

import Controller.*;
import Model.*;
import java.util.Scanner;

/**
 * Created by vladc on 05.10.2016.
 */
public class View {
    private Controller ctrl;
    private Scanner cin;

    public View(Controller ctrl) {
        this.ctrl = ctrl;
        this.cin = new Scanner(System.in);
    }

    public void run() {
        int userInput;

        while (true) {
            printMenu();
            userInput = readUserMenuOption();
            switch(userInput) {
                case 1:     // add a new animal
                    IAnimal new_animal;
                    printMenu1();
                    userInput = readUserMenuOption();
                    if (userInput == 1)
                        new_animal = readPoultry();
                    else if (userInput == 2)
                        new_animal = readCow();
                    else if (userInput == 3)
                        new_animal = readPig();
                    else
                        break;
                    try {
                        ctrl.add(new_animal);
                    }
                    catch (Exception e) {
                        System.out.println(e);
                    }
                    break;
                case 2:     // remove an existing animal
                    int id;
                    printMenu2();
                    userInput = readUserMenuOption();
                    System.out.print("id = ");
                    while (!cin.hasNextInt()) {
                        cin.next();
                        System.out.println("Wrong input! Please enter an integer.");
                    }
                    id = cin.nextInt();
                    try {
                        if (userInput == 1)
                            ctrl.remove(new Poultry(id, "", 0));
                        else if (userInput == 2)
                            ctrl.remove(new Cow(id, "", 0));
                        else if (userInput == 3)
                            ctrl.remove(new Pig(id, "", 0));
                    }
                    catch (Exception e) {
                        System.out.println(e);
                    }
                    break;
                case 3:     // show all animals having weight > 3 kg
                    IAnimal[] solution = ctrl.solve();
                    for (int i = 0; i < solution.length; i++) {
                        System.out.print("Hello, I am a ");
                        if (solution[i] instanceof Poultry)
                            System.out.print("POULTRY");
                        else if (solution[i] instanceof Cow)
                            System.out.print("COW");
                        else if (solution[i] instanceof Pig)
                            System.out.print("PIG");
                        System.out.print(", my name is " + solution[i].getName());
                        System.out.print(" and I have ");
                        System.out.print(solution[i].getWeight());
                        System.out.println(" kg.");
                    }
                    break;
                case 0:
                    System.out.println("Bye!");
                    return;
                default:
                    break;
            }
        }
    }

    private int readUserMenuOption() {
        int userInput;

        while (true) {
            while (!cin.hasNextInt()) {
                cin.next();
                System.out.println("Wrong input! Please enter an integer.");
            }
            userInput = cin.nextInt();
            cin.nextLine();
            if (0 <= userInput && userInput <= 3)
                break;
            System.out.println("Wrong input! No such option.");
        }
        return userInput;
    }

    private void printMenu() {
        System.out.println("----Menu:----");
        System.out.println("1. Add a new animal");
        System.out.println("2. Remove an animal");
        System.out.println("3. Show all animals having weight > 3 kg");
        System.out.println("0. Exit");
    }

    private void printMenu1() {
        System.out.println("---Adding a new animal...");
        System.out.println("1. Add a new poultry");
        System.out.println("2. Add a new cow");
        System.out.println("3. Add a new pig");
        System.out.println("0. Go back to main menu");
    }

    private void printMenu2() {
        System.out.println("---Removing an existing animal...");
        System.out.println("1. Remove a poultry");
        System.out.println("2. Remove a cow");
        System.out.println("3. Remove a pig");
        System.out.println("0. Go back to main menu");
    }

    private Poultry readPoultry() {
        Poultry poultry;
        int id;
        String name;
        int weight;

        System.out.print("poultry id = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        id = cin.nextInt();
        cin.nextLine();

        System.out.print("poultry name = ");
        name = cin.nextLine();

        System.out.print("poultry weight = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        weight = cin.nextInt();
        cin.nextLine();

        poultry = new Poultry(id, name, weight);
        return poultry;
    }

    private Cow readCow() {
        Cow cow;
        int id;
        String name;
        int weight;

        System.out.print("cow id = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        id = cin.nextInt();
        cin.nextLine();

        System.out.print("cow name = ");
        name = cin.nextLine();

        System.out.print("cow weight = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        weight = cin.nextInt();
        cin.nextLine();

        cow = new Cow(id, name, weight);
        return cow;
    }

    private Pig readPig() {
        Pig pig;
        int id;
        String name;
        int weight;

        System.out.print("pig id = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        id = cin.nextInt();
        cin.nextLine();

        System.out.print("pig name = ");
        name = cin.nextLine();

        System.out.print("pig weight = ");
        while (!cin.hasNextInt()) {
            cin.next();
            System.out.println("Wrong input! Please enter an integer.");
        }
        weight = cin.nextInt();
        cin.nextLine();

        pig = new Pig(id, name, weight);
        return pig;
    }
}
