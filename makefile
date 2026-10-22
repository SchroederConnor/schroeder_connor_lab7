restaurant: menuItem.o main.o restaurant.o waitingLine.o customer.o
	g++ -o restaurant menuItem.o main.o restaurant.o waitingLine.o customer.o
customer.o: customer.cpp customer.h
	g++ -c customer.cpp 
waitingLine.o: waitingLine.h waitingLine.cpp
	g++ -c waitingLine.cpp 
restaurant.o: restaurant.h restaurant.cpp
	g++ -c restaurant.cpp
main.o: main.cpp restaurant.h waitingLine.h
	g++ -c main.cpp 
menuItem.o: menuItem.cpp menuItem.h
	g++ -c menuItem.cpp 
clean:
	rm *.o restaurant