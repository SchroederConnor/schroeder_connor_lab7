#include "waitingLine.h"

//constructos
WaitingLine::WaitingLine()
{
    numCustomer = 0;
    first = NULL;
    last = NULL;
}
WaitingLine::WaitingLine(int n, Customer* f, Customer* l)
{
    if(f == NULL)
    {
        numCustomer = 0;
        first = NULL;
        last = NULL;
        return;
    }
    numCustomer = n;
    Customer* temp = f;
    first = new Customer();
    last = first;

    first->setName(temp->getName());
    first->setID(temp->getID());
    first->setSize(temp->getSize());

    temp = temp->getNext();
    while(temp != NULL)
    {
        last->setNext(new Customer);
        last = last->getNext();
        last->setName(temp->getName());
        last->setID(temp->getID());
        last->setSize(temp->getSize());
        last->setNext(NULL);
        temp = temp->getNext();
    }
}
WaitingLine::WaitingLine(const WaitingLine& rhs)
{
    if(rhs.first == NULL)
    {
        first =last= NULL;
        return;
    }
    Customer* temp = rhs.first;
    first =last= new Customer;
    first->setName(temp->getName());
    first->setNext(NULL);
    temp = temp->getNext();
    while(temp!= NULL){
        last->setNext(new Customer);
        last = last->getNext();
        last->setName(temp->getName());
        last->setNext(NULL);
        temp = temp->getNext();
    }
}

//destructor
WaitingLine::~WaitingLine()
{
    Customer* temp = first;
    while(temp != NULL){
        Customer* toDelete = temp;
        temp = temp->getNext();
        delete toDelete;
    }
    first = NULL;
    last = NULL;
}

//getters
int WaitingLine::getNumCustomers() {return numCustomer;}
Customer* WaitingLine::getFirst() {return first;}
Customer* WaitingLine::getLast() {return last;}

//settors
void WaitingLine::setNumCustomers(int n) {numCustomer = n;}
void WaitingLine::setFirst(Customer* f) {first = f;}
void WaitingLine::setLast(Customer* l) {last = l;}

//check customer


//add customer
void WaitingLine::addCustomer(Customer& rh)
{
    if(checkCustomer(rh))
    {
        cout << "Customer: " << rh.getName() << "(ID:" << rh.getID() << ") Already Exists!" << endl;
        return;
    }
    Customer* cust = new Customer;
    
    cust->setName(rh.getName());
    cust->setID(rh.getID());
    cust->setSize(rh.getSize());
    cust->setNext(NULL);

    if(first == NULL)
    {
        first = cust;
        last = first;
    }
    else
    {
        last->setNext(cust);
        last = cust;
        numCustomer++;
        cout << "Customer: " << rh.getName() << "(ID:" << rh.getID() << ") Added Successfully!" << endl;
    }
}

//remove customer
void WaitingLine::removeCustomer()
{
    if(numCustomer == 0 || first == NULL)
    {
        cout << "The waiting line is empty." << endl;
        return;
    }
    cout << "Calling Customer: " << first->getName() << "(ID:" << first->getID() << ")" << endl;
    Customer* temp = first;
    first = first->getNext();
    delete temp;
    numCustomer--;
    if(numCustomer == 0 || first == NULL)
    {
        last = NULL;
    }
}

//check customer
bool WaitingLine::checkCustomer(Customer& rh)
{
    Customer* temp = first;
    while(temp != NULL)
    {
        if(temp->getID() == rh.getID())
        {
            return true;
        }
        temp = temp->getNext();
    }
    return false;
}

//overloaded operators
ostream& operator<<(ostream& os, const WaitingLine& rh)
{
    Customer* temp = rh.first;
    int count = 1;
    if(temp != NULL)
    {
        cout << "===================" << endl << "Waiting Line" << endl;
        cout << rh.numCustomer << " in Line" << endl << "===================" << endl;
    }
    while(temp != NULL)
    {
        cout << count << ". " << *temp;
        count++;
        temp = temp->getNext();
    }
    return os;
}
WaitingLine& WaitingLine::operator=(const WaitingLine& wl)
{
    Customer* temp = wl.first;
    first =last= new Customer;
    first->setName(temp->getName());
    first->setNext(NULL);
    temp = temp->getNext();
    while(temp!= NULL){
        last->setNext(new Customer);
        last = last->getNext();
        last->setName(temp->getName());
        last->setNext(NULL);
        temp = temp->getNext();
    }
    return *this;
}