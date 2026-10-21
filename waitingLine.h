#ifndef WAITINGLINE_H
#define WAITINGLINE_H

#include "customer.h"

class WaitingLine
{
    int numCustomer;
    Customer* first;
    Customer* last;
    
    public:
        WaitingLine();
        WaitingLine(int, Customer*, Customer*);
        WaitingLine(const WaitingLine&);

        ~WaitingLine();

        int getNumCustomers();
        Customer* getFirst();
        Customer* getLast();

        void setNumCustomers(int);
        void setFirst(Customer*);
        void setLast(Customer*);

        bool checkCustomer(Customer&);

        void addCustomer(Customer&);
        void removeCustomer(Customer&);

        friend ostream& operator<<(ostream&, const WaitingLine&);
        WaitingLine& operator=(const WaitingLine&);
};
#endif