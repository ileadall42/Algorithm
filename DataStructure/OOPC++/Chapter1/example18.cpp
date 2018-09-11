#include <iostream>

using namespace std;

int rMax(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    return b;
}
inline int rMax(int a, int b, int c)
{
    if (b > a)
    {
        a = b;
    }
    if (c > a)
    {
        a = c;
    }
    return a;
}
int main(int argc, char const *argv[])
{
    /* code */
    int a = 8, b = 10, c = 1;
    std::cout << rMax(a, b, c) << '\n';
    // std::cout << rMax(c, a) << '\n';
    return 0;
}