#include <iostream>
#include <vector>
#include <algorithm> // for sort, reverse

using namespace std;

int main() {
    // Initialization
    vector<int> vec = {1, 2, 3};      // using initializer list
    vector<int> vec2(vec);           // copy constructor
    vector<int> vec3;                // empty vector using constructor

    // Insert elements
    vec3.push_back(10);             // add 10 at end
    vec3.push_back(20);
    vec3.insert(vec3.begin(), 5);   // insert 5 at beginning

    // Access elements
    cout << "vec3[0] = " << vec3[0] << endl;        // direct access
    cout << "vec3.at(1) = " << vec3.at(1) << endl;  // safe access

    // Size and Capacity
    cout << "Size of vec3: " << vec3.size() << endl;
    cout << "Is vec3 empty? " << (vec3.empty() ? "Yes" : "No") << endl;

    // Iterate using index
    cout << "vec3: ";
    for (int i = 0; i < vec3.size(); i++) {
        cout << vec3[i] << " ";
    }
    cout << endl;

    // Iterate using range-based for loop
    cout << "vec: ";
    for (int value : vec) {
        cout << value << " ";
    }
    cout << endl;

    // Iterate using iterators
    cout << "vec2: ";
    for (auto it = vec2.begin(); it != vec2.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // Delete elements
    vec3.pop_back();                     // remove last element
    vec3.erase(vec3.begin());           // remove first element

    cout << "vec3 after deletions: ";
    for (int x : vec3) cout << x << " ";
    cout << endl;

    // Sort and reverse
    vector<int> sortVec = {4, 1, 3, 2};
    sort(sortVec.begin(), sortVec.end());    // ascending sort
    cout << "Sorted: ";
    for (int x : sortVec) cout << x << " ";
    cout << endl;

    reverse(sortVec.begin(), sortVec.end()); // reverse
    cout << "Reversed: ";
    for (int x : sortVec) cout << x << " ";
    cout << endl;

    // Clear all elements
    sortVec.clear();
    cout << "sortVec size after clear: " << sortVec.size() << endl;

    return 0;
}
