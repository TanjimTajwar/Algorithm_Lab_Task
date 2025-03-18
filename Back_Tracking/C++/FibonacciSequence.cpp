#include <iostream>
using namespace std;

// Function to print Fibonacci sequence recursively
void findFibonacci(int n, int a, int b) {
    // Store current value of b
    int temp = b;
    // Calculate next Fibonacci number
    b = a + b;
    // Update a to previous b value
    a = temp;
    
    // Base case: stop if we exceed the limit
    if (n < a || n < b) {
        return;
    }
    
    // Print current Fibonacci number
    cout << "+" << b;
    // Recursive call for next number
    findFibonacci(n, a, b);
}

int main() {
    int n;
    // Prompt user for input
    cout << "Enter the Limit of fibonacci sequence: ";
    cin >> n;
    
    // Print initial sequence
    cout << "1+1";
    // Start Fibonacci sequence
    findFibonacci(n, 1, 1);
    cout << endl;
    
    return 0;
} 