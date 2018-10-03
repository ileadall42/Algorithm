#include <iostream>
#include <string>
using namespace std;

class TriangleV
{
  private:
    int length, height, width;

  public:
    void set_value(int l, int h, int w)
    {
        this->length = l;
        this->height = h;
        this->width = w;
    }
    int getArea()
    {
        std::cout << " 这个柱体面积为：" << this->height * this->width * this->length << '\n';
        return this->height * this->width * this->length;
    }
};

int main(int argc, char const *argv[])
{
    std::cout << "请输入长宽高：" << '\n';  
    TriangleV t1; // 实例化一个t1
    int l,w,h;
    std::cin>>l;
    std::cin >> w;
    std::cin >> h;
    std::cout << l << w << h << '\n';
    t1.set_value(l,h,w);
    t1.getArea();
    return 0;
}
