
#include <iostream>
using namespace std;
#define MAX_SIZE = 31
int max(int a, int b, int c = 3)
{
    if (c > a)
    {
        a = c;
    }
    if (b > a)
    {
        a = b;
    }
    return a;
}

int main(int argc, char const *argv[])
{
    /* code */
    int x = 10, y = 12;
    cout << max(x, y) << endl;
    cout << "English is supported" << endl;
    cout << "请输入你的名字：" << endl;
    int a;
    // cin >> a;
    
    return 0;
}
