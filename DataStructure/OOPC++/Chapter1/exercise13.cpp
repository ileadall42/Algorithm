#include <iostream>
#include <vector>

using namespace std;
//http://www.runoob.com/w3cnote/cpp-vector-container-analysis.html 容器介绍
template <class T>
int getlength(T &array)
{
    return (sizeof(array) / sizeof(array[0]));
}

// template <typename T>
// T quickSort(T a){
//     return a;
// }
// 整形版本的数组

template <class T>
void quickSort(T &a) // 数组传入引用 相当于 传入可变变量了。
{
    for (int i = 0; i < getlength(a); i++)
    {

        for (int j = i; j < getlength(a); j++)
        {
            /* code */
            if (a[i] > a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}

template <class T>
void bubbleSort(T &a)
{
    for (int i = 0; i < a.size(); i++)
    {

        for (int j = i; j < a.size(); j++)
        {
            /* code */
            if (a[i] > a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    
}

template <class T>
void print_function(T a){
    for (int i = 0; i < a.size(); i++)
    {
        cout << a[i] << ",";
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    int a[] = {3, 2, 1, 2, 5, 3, 21};
    // cout << &a << endl;
    // vector<T> a;
    vector<int> va;

    for (int i = 0; i < getlength(a); i++)
    {
        /* code */
        va.push_back(a[i]);
    }
    cout << "未排序前的结果：" << endl;
    print_function(va);
    quickSort(va);
    cout << "排序后的结果：" << endl;
    print_function(va);
    // vector<T> obj; //创建一个向量存储容器 int

    /* code */
    return 0;
}
