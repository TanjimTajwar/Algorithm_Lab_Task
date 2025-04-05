#include <iostream>
#include <vector>
#include <utility>  // for pair and make_pair
using namespace std;

int main() {
    // Declare a vector of pair<int, string>
    vector<pair<int, string>> studentList;

    // Insert elements using make_pair and direct initialization
    studentList.push_back(make_pair(101, "Tanjim"));
    studentList.push_back({102, "Tajwar"});
    studentList.push_back({103, "Arnab"});
    studentList.push_back(make_pair(104, "Rayhan"));

    // Displaying all student ID-name pairs
    cout << "Student Roll and Name:\n";
    for (int i = 0; i < studentList.size(); i++) {
        cout << "Roll: " << studentList[i].first
             << ", Name: " << studentList[i].second << endl;
    }

    return 0;
}
