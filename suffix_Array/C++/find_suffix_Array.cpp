#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

string text;

void find_suffix_array() {
    int n = text.length();
    vector<pair<int, string>> myList;

    for (int a = 0; a < n; a++) {
        myList.push_back({a, text.substr(a)});
    }

    // Sort the list based on suffixes
    sort(myList.begin(), myList.end(), 
         [](const auto& a, const auto& b) { return a.second < b.second; });

    // Print the sorted suffix array map
    cout << "Suffix Array:" << endl;
    for (const auto& answer : myList) {
        cout << answer.first << " ";
    }
    cout << endl;
}

int main() {
    cin >> text;
    find_suffix_array();
    return 0;
} 