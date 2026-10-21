#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <iostream>
using namespace std;

class Customer
{
    string name, ID;
    int partySize;
    Customer* next;

    public:
        //constructors
        Customer();
        Customer(string, string, int, Customer*);
        Customer(const Customer&);

        //destructor
        ~Customer();

        //getters
        string getName();
        string getID();
        int getSize();
        Customer* getNext();

        //setters
        void setName(string);
        void setID(string);
        void setSize(int);
        void setNext(Customer*);

        //operator overloads
        friend ostream& operator<<(ostream&, const Customer&);
        Customer& operator=(const Customer&);
};
#endif