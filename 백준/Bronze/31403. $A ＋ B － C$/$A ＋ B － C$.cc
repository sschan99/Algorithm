#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    cout << a + b - c << endl;
    
    int x = 10;
    while (x <= b)
    {
        x *= 10;
    }
    cout << a * x + b - c;
}