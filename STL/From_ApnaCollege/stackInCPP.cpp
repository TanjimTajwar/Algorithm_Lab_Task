#include <iostream>
#include <stack>
using namespace std;

int main() {
    // 1. Declare a stack of integers
    stack<int> s;

    // 2. Push elements onto the stack
    s.push(10);   // Stack: 10
    s.push(20);   // Stack: 10, 20
    s.push(30);   // Stack: 10, 20, 30

    // 3. Access the top element
    cout << "Top element: " << s.top() << endl;  // Output: 30

    // 4. Pop an element from the stack
    s.pop();  // Removes 30 → Now top is 20
    cout << "Top after pop: " << s.top() << endl;

    // 5. Size of the stack
    cout << "Stack size: " << s.size() << endl;

    // 6. Check if stack is empty
    if (s.empty()) {
        cout << "Stack is empty" << endl;
    } else {
        cout << "Stack is not empty" << endl;
    }

    // 7. Print all elements (pop till empty)
    cout << "Stack elements (from top to bottom): ";
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;

    return 0;
}
