#include <iostream>
using namespace std;

// Function to calculate factorial recursively
long long findFactorial(int n) {
    // Base case: factorial of 0 or 1 is 1
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case: n! = n * (n-1)!
    return n * findFactorial(n - 1);
}

int main() {
    int n;
    // Prompt user for input
    cout << "Enter the number: ";
    cin >> n;
    
    // Calculate and display factorial
    cout << "So the Factorial of " << n << " is " << findFactorial(n) << endl;
    
    return 0;
} 