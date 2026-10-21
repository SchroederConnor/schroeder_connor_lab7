#include "customer.h"

//constructors
Customer::Customer()
{
    name = "N/A";
    ID = "N/A";
    partySize = 0;
    next = NULL;
}
Customer::Customer(string n, string i, int p, Customer* point)
{
    name = n;
    ID = i;
    partySize = p;
    next = point;
}
Customer::Customer(const Customer& rh)
{
    name = rh.name;
    ID = rh.ID;
    partySize = rh.partySize;
    next = rh.next;
}

//destructor
Customer::~Customer(){}

//getters
string Customer::getName() {return name;}
string Customer::getID() {return ID;}
int Customer::getSize() {return partySize;}
Customer* Customer::getNext() {return next;}

//setters
void Customer::setName(string n) {name = n;}
void Customer::setID(string i) {ID = i;}
void Customer::setSize(int i) {partySize = i;}
void Customer::setNext(Customer* temp) {next = temp;}

//overloaded Operators
ostream& operator<<(ostream& os, const Customer& rh)
{
    cout << "Name: " << rh.name << "(" << "ID:" << ") - " << rh.partySize << " People." << endl;
    return os;
}
Customer& Customer::operator=(const Customer& rh)
{
    delete next;
    name = rh.name;
    ID = rh.ID;
    partySize = rh.partySize;
    next = rh.next;
    return *this;
}