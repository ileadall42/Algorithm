#include "Stack.h"
#include <stdio.h>
#include <stdlib.h>
#include "general.h"
typedef int SElemType; /* 定义栈元素类型为整型 */

status initStack(SqStack *S)
{
    (*S).base = (SElemType *)malloc(STACK_INIT_SIZE * sizeof(SElemType));
    if (!(*S).base)
        exit(OVERFLOW); /* 存储分配失败 */
    (*S).top = (*S).base;
    (*S).stacksize = STACK_INIT_SIZE;
    return OK;
}
status pushStack(SqStack *S, SElemType e)
{                                /* 插入元素e为新的栈顶元素 */
    if (isFullStack(*S) == TRUE) /* 栈满，追加存储空间 */
    {
        (*S).base = (SElemType *)realloc((*S).base, ((*S).stacksize + STACKINCREMENT) * sizeof(SElemType));
        if (!(*S).base)
            exit(OVERFLOW); /* 存储分配失败 */
        (*S).top = (*S).base + (*S).stacksize;
        (*S).stacksize += STACKINCREMENT;
    }
    *((*S).top) = e; //栈顶指针移动 并指向新的元素  相当于开辟了一个指针数组
    (*S).top += 1;
    return OK;
}
status isFullStack(SqStack S)
{
    if ((S).top - (S).base >= (S).stacksize)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}
status isEmptyStack(SqStack S)
{
    if (S.top == S.base)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

status destroyStack(SqStack *S){
    free((*S).base);  // free掉的永远是申请空间返回的对象
    (*S).base = NULL;
    (*S).top = NULL;
    (*S).stacksize = 0;
    return OK;
}

status clearStack(SqStack *S)
{ /* 把S置为空栈 */
    (*S).top = (*S).base;  //直接让top == base就清空了，但是仍然有可能越界访问
    return OK;
}

status StackTraverse(SqStack S, status (*visit)(SElemType))
{ /* 从栈底到栈顶依次对栈中每个元素调用函数visit()。 */
    /* 一旦visit()失败，则操作失败 */
    while (S.top > S.base){
        visit(*S.base++);
    }
        
    printf("\n");
    return OK;
}

status popStack(SqStack *S, SElemType *e)
{
    if (isEmptyStack(*S) == TRUE)
    {
        printf("\n栈为空没有元素出栈。\n");
        return ERROR;
    }
    (*S).top -= 1; // 栈顶没元素 栈底指针有元素
    *e = *((*S).top);
    return OK;
}

int main(int argc, char const *argv[])
{
    printf("\n准备开始书写一个栈了。\n");
    SqStack stack;
    initStack(&stack);
    status is_empty;
    pushStack(&stack, 3);
    is_empty = isEmptyStack(stack);

    if (is_empty == TRUE)
    {
        printf("这个是空栈。\n");
    }
    else
    {
        printf("这个不是个空栈\n");
    }

    for (int i = 0; i < 32; i++)
    {
        pushStack(&stack, i * 2);
    }
    printf("此时栈的分配空间大小为：%d  | 栈的长度为：%ld\n", (stack).stacksize, stack.top - stack.base - 1);

    printf("准备出栈了。\n");
    SElemType ep;
    for (int i = 0; i < 35; i++)
    {
        status is_succes = popStack(&stack, &ep);
        if (is_succes == TRUE)
        {
            printf("%d,", ep);
        }
    }

    return 0;
}
