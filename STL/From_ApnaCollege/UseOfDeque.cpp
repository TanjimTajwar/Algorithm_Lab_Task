#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
    deque<string> mydeque;  // Use lowercase 'string'

    // Adding elements
    mydeque.push_back("Tajwar");
    mydeque.push_front("Tanjim");
    mydeque.push_back("Arnab");
    mydeque.push_back("Taj");

    // Printing the deque using range-based for loop
    cout << "Current deque: ";
    for (const string& name : mydeque) {
        cout << name << " ";
    }
    cout << endl;

    // Remove last element
    mydeque.pop_back();

    // Accessing specific elements
    cout << "2nd Element (index 2) using operator[]: " << mydeque[2] << endl;
    cout << "2nd Element (index 2) using at(): " << mydeque.at(2) << endl;
    cout << "First element using front(): " << mydeque.front() << endl;
    cout << "Last element using back(): " << mydeque.back() << endl;

    // Size of deque
    cout << "Size of deque: " << mydeque.size() << endl;

    // Check if deque is empty
    cout << "Is deque empty? " << (mydeque.empty() ? "Yes" : "No") << endl;

    // Clear all elements
    mydeque.clear();
    cout << "Deque cleared. Size now: " << mydeque.size() << endl;

    return 0;
}
