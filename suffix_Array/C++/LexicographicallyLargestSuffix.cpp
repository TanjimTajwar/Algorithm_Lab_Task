#include <iostream>
#include <set>
#include <string>

using namespace std;

string findLSS(string mystr, int length) {
    set<string> myTree;
    for(int a = 0; a < length; a++) {
        myTree.insert(mystr.substr(a));
    }
    return *myTree.rbegin();
}

int main() {
    cout << "Lets Code it." << endl;
    string mystr;
    cout << "Enter the String: ";
    cin >> mystr;
    int length = mystr.length();
    cout << "The Lexicographically Largest Suffix is : " << findLSS(mystr, length) << endl;
    return 0;
} 