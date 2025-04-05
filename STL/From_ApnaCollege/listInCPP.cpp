#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> mylist; // Create a list of integers

    // Add elements to the list
    mylist.push_back(10);
    mylist.push_front(9);
    mylist.emplace_back(11);
    mylist.push_back(12);
    mylist.push_front(6);

    // Print the elements of the list
    for (const int& a : mylist) { // Use reference to avoid unnecessary copying
        cout << a << " ";
    }
    cout << endl<< "After Poping: " << mylist.size() << endl; // Print the size of the list

    mylist.pop_back(); // Remove the last element
    for (const int& a : mylist) { // Use reference to avoid unnecessary copying
        cout << a << " ";
    }
    cout << endl;
    return 0;
}