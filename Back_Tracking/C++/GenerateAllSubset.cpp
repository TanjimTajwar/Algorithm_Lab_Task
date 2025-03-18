#include <iostream>
#include <vector>
using namespace std;

// Function to generate all subsets recursively
void generateSubset(vector<int>& arr, int index, vector<int>& temp, vector<vector<int>>& result) {
    // Base case: when we've processed all elements
    if (index == arr.size()) {
        result.push_back(temp);
        return;
    }
    
    // Exclude current element
    generateSubset(arr, index + 1, temp, result);
    
    // Include current element
    temp.push_back(arr[index]);
    generateSubset(arr, index + 1, temp, result);
    temp.pop_back();  // Backtrack
}

int main() {
    int n;
    // Prompt user for input size
    cout << "Enter the number of element in the set: ";
    cin >> n;
    
    // Input array
    vector<int> arr(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Vector to store all subsets
    vector<vector<int>> result;
    vector<int> temp;
    
    // Generate all subsets
    generateSubset(arr, 0, temp, result);
    
    // Print all subsets
    cout << "So the SubSet are: " << endl;
    cout << "[";
    for (size_t i = 0; i < result.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < result[i].size(); j++) {
            cout << result[i][j];
            if (j < result[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < result.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    
    return 0;
} 