#include <iostream>
#include <string>
using namespace std;

class Time
{
  private:
    int age;
    string name;

  public:
    int hour = -1, sec = -1, min = -1;
    int check_hour(int hour)
    {
        if (hour <= 24 and hour >= 0)
        {
            return 1;
        }
        cout << "Please enter the correct time!" << endl;
        return 0;
    }
    int check_min_sec(int value)
    {
        if (value <= 60 and value >= 0)
        {
            return 1;
        }
        cout << "Please enter the correct min or sec!" << endl;
        return 0;
    }

    void set_time()
    {

        while (!check_hour(this->hour))
        {
            std::cout << " Please enter the hour : " << '\n';
            cin >> this->hour;
        }
        while (!check_min_sec(this->min))
        {
            std::cout << " Please enter the min : " << '\n';
            cin >> this->min;
        }
        while (!check_min_sec(this->sec))
        {
            std::cout << " Please enter the sec : " << '\n';
            cin >> this->sec;
        }
    }
    void display()
    {
        cout << "The time is now :" << this->hour << ":" << this->min << ":" << this->sec << "\n";
    }
};

int main(int argc, char const *argv[])
{
    Time t1; // 实例化一个t1
    t1.set_time();
    t1.display();
    return 0;
}
