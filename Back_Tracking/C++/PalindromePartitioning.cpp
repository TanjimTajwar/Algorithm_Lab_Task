#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Global variables
vector<vector<string>> mylist;
string str;

// Function to check if a substring is palindrome
bool isSafe(int start, int end) {
    while (start < end) {
        if (str[start++] != str[end--]) {
            return false;
        }
    }
    return true;
}

// Function to find all palindrome partitioning
void findPalindromePartitioning(int index, vector<string>& temp) {
    // Base case: if we've reached the end of string
    if (index == str.length()) {
        mylist.push_back(temp);
        return;
    }
    
    // Try all possible partitions
    for (int i = index; i < str.length(); i++) {
        if (isSafe(index, i)) {
            // Add current palindrome substring
            temp.push_back(str.substr(index, i - index + 1));
            // Recur for remaining string
            findPalindromePartitioning(i + 1, temp);
            // Backtrack
            temp.pop_back();
        }
    }
}

int main() {
    cout << "Enter the String: ";
    cin >> str;
    
    vector<string> temp;
    findPalindromePartitioning(0, temp);
    
    cout << "So the Palindrome Partitioning Set is:" << endl;
    cout << "[";
    for (size_t i = 0; i < mylist.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < mylist[i].size(); j++) {
            cout << "\"" << mylist[i][j] << "\"";
            if (j < mylist[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < mylist.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    
    return 0;
} 