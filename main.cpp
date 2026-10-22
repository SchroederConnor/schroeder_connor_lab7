#include "restaurant.h"
#include "waitingLine.h"



int main(){

    // Creating a MenuItem object named burger using the parameterized constructor.
    // Passing "Burger" as the name and 8.5 as the price.
    MenuItem burger("Burger", 8.5);

    // Creating a MenuItem object named pizza using the parameterized constructor.
    // Passing "Pizza" as the name and 18.55 as the price.
    MenuItem pizza("Pizza", 18.55);

    // Creating a MenuItem object named sandwich using the parameterized constructor.
    // Passing "Sandwich" as the name and 10.5 as the price.
    MenuItem sandwich("Sandwich", 10.5);

    // Creating a MenuItem object named softDrink using the parameterized constructor.
    // Passing "Soft Drink" as the name and 2.5 as the price.
    MenuItem softDrink("Soft Drink", 2.5);

    // Creating a Restaurant object named restaurant using the default constructor.
    Restaurant restaurant;

    // Setting the restaurant name to "Hello World".
    restaurant.setName("Hello World");

    // Adding burger to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + burger;

    // Adding pizza to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + pizza;

    // Adding sandwich to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + sandwich;

    // Adding softDrink to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + softDrink;

    // Creating a MenuItem object named combo by adding burger and
    // softDrink using the overloaded + operator of the MenuItem class.
    MenuItem combo = softDrink + burger;

    // Setting the combo item's name to "Combo (Burger & Drinks)".
    combo.setName("Combo (Burger & Drinks)");

    // Adding combo to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + combo;

    // Creating a MenuItem object named salad using the parameterized constructor.
    // Passing "Salad" as the name and 10.75 as the price.
    MenuItem salad("Salad", 10.75);

    // Adding salad to the restaurant using the overloaded + operator of the Restaurant class.
    restaurant + salad;
    cout << restaurant;



    //TODO step 1:Dynaically create a Customer object named Annie using the parameterized constructor.
    // Passing "Annie" as the name, "An4" as ID, 4 as partySize and NULL as next pointer.
    Customer* Annie = new Customer("Annie", "An4", 4, NULL);

    //TODO step 2:Dynaically create a Customer object named Harry using the parameterized constructor.
    // Passing "Harry" as the name, "Ha4" as ID, 3 as partySize and NULL as next pointer.
    Customer* Harry = new Customer("Harry", "Ha4", 3, NULL);

    //TODO step 3:Dynaically create a Customer object named Jane using the parameterized constructor.
    // Passing "Jane" as the name, "Ja1" as ID, 1 as partySize and NULL as next pointer.
    Customer* Jane = new Customer("Jane", "Ja1", 1, NULL);

    //TODO step 4:Set Annie's next pointer to Harry using the setNext method
    Annie->setNext(Harry);
    
    //TODO step 5:Set Harry's next pointer to Jane using the setNext method
    Harry->setNext(Jane);

    //TODO step 6: Create a WaitingLine object named line using the parameterized constructor
    //Pass 3 as number of customer, Annie as first and Jane as last
    WaitingLine line(3, Annie, Jane);

    //TODO step 7: display the waiting line information using the insertion operator overload method for the WaitingLine class
    cout << line;

    //TODO step 8: add customer Annie using the addCustomer() method 
    //pass *Annie as parameter for this method
    line.addCustomer(*Annie);

    //TODO step 9: Dynaically create a Customer object named John using the parameterized constructor.
    // Passing "John" as the name, "Jo5" as ID, 5 as partySize and NULL as next pointer.
    Customer* John = new Customer("John", "Jo5", 5, NULL);

    //TODO step 10: add customer John using the addCustomer() method 
    //pass *John as parameter for this method
    line.addCustomer(*John);

    //TODO step 11: removing the first person from the waiting list
    line.removeCustomer();

    //TODO step 12: display the waiting line information using the insertion operator overload method for the WaitingLine class
    cout << line;
    
     // Your output must match Output.txt exactly.
    // Pay close attention to spelling, capitalization, spaces, and newlines.
    

    return 0;
}