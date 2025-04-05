#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50};

    // -----------------------------
    // 1. begin() and end() (forward)
    // -----------------------------
    cout << "Using begin() to end(): ";
    for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " "; // Dereference iterator to get value
    }
    cout << endl;

    // --------------------------------
    // 2. rbegin() and rend() (reverse)
    // --------------------------------
    cout << "Using rbegin() to rend(): ";
    for (vector<int>::reverse_iterator rit = vec.rbegin(); rit != vec.rend(); ++rit) {
        cout << *rit << " "; // Reverse traversal
    }
    cout << endl;

    // -----------------------------------
    // 3. cbegin() and cend() (const-safe)
    // -----------------------------------
    cout << "Using cbegin() to cend(): ";
    for (vector<int>::const_iterator it = vec.cbegin(); it != vec.cend(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // --------------------------------------
    // 4. crbegin() and crend() (const-reverse)
    // --------------------------------------
    cout << "Using crbegin() to crend(): ";
    for (vector<int>::const_reverse_iterator it = vec.crbegin(); it != vec.crend(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // --------------------------------------
    // 5. Using auto (C++11 and above)
    // --------------------------------------
    cout << "Using auto with begin() to end(): ";
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // --------------------------------------
    // 6. Using range-based for loop (best way)
    // --------------------------------------
    cout << "Using range-based for loop: ";
    for (int value : vec) {
        cout << value << " ";
    }
    cout << endl;

    return 0;
}
