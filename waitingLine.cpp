#include "waitingLine.h"

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
        Customer* cust = new Customer();
        
    }
}
WaitingLine::WaitingLine(const WaitingLine& rh)
{

}