#include <iostream>
#include <set>
#include <string>

using namespace std;

int findDistinctSub(string str) {
    set<string> tree;
    for(int a = 0; a < str.length(); a++) {
        tree.insert(str.substr(a));
    }

    int count = 1;
    string text2 = *tree.begin();

    for(const string& text : tree) {
        if(text != text2) {
            count++;
        }
        text2 = text;
    }
    return count;
}

int main() {
    cout << "Aloha Bro: " << endl;
    string str;
    cout << "Enter the String: ";
    cin >> str;
    cout << "Distinct Substrings Count: " << findDistinctSub(str) << endl;
    return 0;
} 