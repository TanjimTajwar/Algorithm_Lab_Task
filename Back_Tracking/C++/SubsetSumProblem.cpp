#include <iostream>
#include <vector>
using namespace std;

// Global variables
int target;
vector<vector<int>> mylist;
int n;

// Function to find all subsets that sum up to target
void findSubSetSum(int index, vector<int>& temp, vector<int>& arr, int remaining) {
    // Base case: if we found a subset that sums to target
    if (remaining == 0) {
        mylist.push_back(temp);
        return;
    }
    
    // Base case: if we've reached end of array or remaining sum is negative
    if (index == n || remaining < 0) {
        return;
    }
    
    // Include current element
    temp.push_back(arr[index]);
    findSubSetSum(index + 1, temp, arr, remaining - arr[index]);
    
    // Exclude current element
    temp.pop_back();
    findSubSetSum(index + 1, temp, arr, remaining);
}

int main() {
    cout << "Enter the number of elements in the set: ";
    cin >> n;
    
    cout << "Enter the Set: ";
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    cout << "Enter the Target Sum: ";
    cin >> target;
    
    vector<int> temp;
    findSubSetSum(0, temp, arr, target);
    
    cout << "So the sum set is:" << endl;
    cout << "[";
    for (size_t i = 0; i < mylist.size(); i++) {
        cout << "[";
        for (size_t j = 0; j < mylist[i].size(); j++) {
            cout << mylist[i][j];
            if (j < mylist[i].size() - 1) cout << ", ";
        }
        cout << "]";
        if (i < mylist.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
    
    return 0;
} 