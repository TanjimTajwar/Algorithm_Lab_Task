#include <iostream>
#include <utility>     // For pair, make_pair
#include <vector>      // For vector of pairs
using namespace std;

int main() {
    // 1. Simple pair
    pair<int, string> student1 = make_pair(1, "Tanjim");

    // 2. Another pair with {} initialization
    pair<int, string> student2 = {2, "Tajwar"};

    // 3. Nested pair
    pair<int, pair<string, float>> student3 = {3, {"Arnab", 3.91}};

    // 4. Pair of pairs
    pair<pair<int, int>, pair<string, string>> combo = {{10, 20}, {"Hello", "World"}};

    // 5. Vector of pairs
    vector<pair<int, string>> studentList;
    studentList.push_back({4, "Rifat"});
    studentList.push_back({5, "Sakib"});
    studentList.push_back({6, "Rayhan"});

    // Output section
    cout << "1. Simple Pair:\n";
    cout << "Student1 ID: " << student1.first << ", Name: " << student1.second << endl;

    cout << "\n2. Another Pair:\n";
    cout << "Student2 ID: " << student2.first << ", Name: " << student2.second << endl;

    cout << "\n3. Nested Pair:\n";
    cout << "Student3 ID: " << student3.first
         << ", Name: " << student3.second.first
         << ", GPA: " << student3.second.second << endl;

    cout << "\n4. Pair of Pairs:\n";
    cout << "First Pair: " << combo.first.first << ", " << combo.first.second << endl;
    cout << "Second Pair: " << combo.second.first << ", " << combo.second.second << endl;

    cout << "\n5. Vector of Pairs:\n";
    for (auto &student : studentList) {
        cout << "ID: " << student.first << ", Name: " << student.second << endl;
    }

    // 6. Swapping
    cout << "\n6. Swapping Student1 and Student2:\n";
    swap(student1, student2);
    cout << "After swap, Student1 ID: " << student1.first << ", Name: " << student1.second << endl;
    cout << "After swap, Student2 ID: " << student2.first << ", Name: " << student2.second << endl;

    // 7. Comparison
    pair<int, int> A = {1, 50};
    pair<int, int> B = {1, 70};

    cout << "\n7. Comparison:\n";
    if (A < B)
        cout << "Pair A is less than Pair B" << endl;
    else
        cout << "Pair B is less than or equal to Pair A" << endl;

    return 0;
}
