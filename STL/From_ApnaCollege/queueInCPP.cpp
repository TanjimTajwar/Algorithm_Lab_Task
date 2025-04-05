#include <iostream>
#include <queue>
using namespace std;

int main() {

    // -------------------------------
    // 1️⃣ Basic Queue of Integers
    // -------------------------------
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);

    cout << "Queue<int> Example:" << endl;
    cout << "Front: " << q.front() << endl;
    cout << "Back: " << q.back() << endl;
    cout << "Size: " << q.size() << endl;

    cout << "Elements: ";
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << "\n\n";


    // -------------------------------
    // 2️⃣ Queue of Strings
    // -------------------------------
    queue<string> names;
    names.push("Tanjim");
    names.push("Tajwar");
    names.push("Arnab");

    cout << "Queue<string> Example:" << endl;
    cout << "Front: " << names.front() << endl;
    cout << "Back: " << names.back() << endl;
    cout << "Size: " << names.size() << endl;

    cout << "Names: ";
    while (!names.empty()) {
        cout << names.front() << " ";
        names.pop();
    }
    cout << "\n\n";


    // --------------------------------------
    // 3️⃣ Queue of Pair<int, string>
    // --------------------------------------
    queue<pair<int, string>> students;
    students.push({101, "Tanjim"});
    students.push({102, "Tajwar"});
    students.push({103, "Arnab"});

    cout << "Queue<pair<int, string>> Example:" << endl;
    cout << "Size: " << students.size() << endl;

    cout << "Students:\n";
    while (!students.empty()) {
        cout << "Roll: " << students.front().first
             << ", Name: " << students.front().second << endl;
        students.pop();
    }

    return 0;
}
