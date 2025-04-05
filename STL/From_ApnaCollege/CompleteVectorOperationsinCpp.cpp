#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Initializing vectors
    vector<int> vec = {1, 2, 3, 4, 5};
    vector<int> vec2;  // empty vector

    // Insert operations
    vec2.push_back(10);                    // adds 10 at the end
    vec2.push_back(20);                    // adds 20 at the end
    vec2.insert(vec2.begin(), 5);          // insert 5 at the beginning
    vec2.insert(vec2.begin() + 1, 15);     // insert 15 at index 1

    // Print vec2
    cout << "vec2 after insertions: ";
    for (int x : vec2) cout << x << " ";
    cout << endl;

    // Erase operations
    vec2.erase(vec2.begin());              // erase first element
    vec2.erase(vec2.begin() + 1);          // erase second element (after previous deletion)

    cout << "vec2 after erasing elements: ";
    for (int x : vec2) cout << x << " ";
    cout << endl;

    // Check empty
    cout << "Is vec2 empty? " << (vec2.empty() ? "Yes" : "No") << endl;

    // Clear all elements
    vec2.clear();
    cout << "vec2 cleared. Size = " << vec2.size() << endl;

    // Resize vector
    vec.resize(7);  // increases size to 7, new elements are default-initialized (0)
    cout << "vec after resize(7): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // Resize to smaller size
    vec.resize(3);
    cout << "vec after resize(3): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // Front and back
    cout << "Front element: " << vec.front() << endl;
    cout << "Back element: " << vec.back() << endl;

    // Assign values
    vector<int> vec3;
    vec3.assign(4, 99);  // assigns 4 elements with value 99
    cout << "vec3 after assign(4, 99): ";
    for (int x : vec3) cout << x << " ";
    cout << endl;

    // Swap content
    cout << "Before swap, vec: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    cout << "Before swap, vec3: ";
    for (int x : vec3) cout << x << " ";
    cout << endl;

    vec.swap(vec3); // swap vec and vec3

    cout << "After swap, vec: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    cout << "After swap, vec3: ";
    for (int x : vec3) cout << x << " ";
    cout << endl;

    // Capacity and shrink_to_fit
    vector<int> capVec;
    capVec.reserve(100); // reserve capacity
    cout << "Initial capacity (reserved): " << capVec.capacity() << endl;

    capVec.push_back(1);
    capVec.push_back(2);
    capVec.push_back(3);

    cout << "Size: " << capVec.size() << ", Capacity: " << capVec.capacity() << endl;

    capVec.shrink_to_fit(); // optional: requests to shrink capacity to fit size
    cout << "Capacity after shrink_to_fit(): " << capVec.capacity() << endl;

    return 0;
}
