#include "menuItem.h"

MenuItem ::MenuItem(){
    name = "N/A";
    price = 0.0;
}
MenuItem ::MenuItem  (string n,double p){
    name = n;
    price = p;
}
MenuItem::MenuItem  (const MenuItem& rhs){
    name = rhs.name;
    price = rhs.price;
}   

void MenuItem::setName(string n){
    name = n;
}
void MenuItem::setPrice(double p){
    price = p;
}

string MenuItem::getName(){
    return name;
}
double MenuItem::getPrice(){
    return price;
}



MenuItem MenuItem:: operator+(const MenuItem& rhs){
    double sum = price + rhs.price;
    MenuItem m("N/A", sum);
    return m;
}

ostream& operator<<(ostream& out,  const MenuItem& rhs) {
    cout << rhs.name << ": $" << rhs.price << endl;
    return out;
}