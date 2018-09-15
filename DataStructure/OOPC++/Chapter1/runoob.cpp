#include <iostream>
#include <string>

using namespace std;

int max(int a, int b)
{
    if (a >= b)
        return a;
    else
        return b;
}
int main()
{
    string s;
    cin >> s;
    s += s;
    int ans = 1;
    for (int i = 0; i < s.size(); i++)
    {
        int j = 1;
        while (i != s.size() - 1 && s[i] != s[i + 1])
        {
            i++;
            j++;
        }
        ans = max(ans, j);
    }
    if (s.size() / 2 < ans)
    {
        ans = s.size() / 2;
    }
    printf("%d\n", ans);
    return 0;
}