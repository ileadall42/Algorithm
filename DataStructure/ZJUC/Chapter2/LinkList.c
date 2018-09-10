//
// Created by Mr.Tangfeifan on 2018/9/10.
//

#include <stdio.h>

void getstart(int a);
int main(int argc, char const *argv[])
{
    int a;
    scanf("input a number %d", &a);

    printf("haha,hello,world.the number is : %d", a);

    for (size_t i = 0; i < a; i++)
    {
        printf("haha \n");
    }
    getstart(a);
    printf("add new change of this file");
    return 0;
}

void getstart(int a)
{

    printf("This is a function and get start of this :%d", a);
    return;
}