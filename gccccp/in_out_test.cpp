
 // stringstreams
 #include <iostream>
 #include <string>
 #include <sstream>
 using namespace std;

 int main ()
 {
   string mystr;
   float price=0;                              //        Enter price: 22.25
   int quantity=0;                             //        Enter quantity: 7
                                                //       Total price: 155.75
   cout << "Enter price: ";
   getline (cin,mystr);
   stringstream(mystr) >> price;
   cout << "Enter quantity: ";
   getline (cin,mystr);
   stringstream(mystr) >> quantity;
   cout << "Total price: " << price*quantity << endl;
   return 0;
 }



