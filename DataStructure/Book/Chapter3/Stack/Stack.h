
#include "general.h"
typedef int status;
/* algo3-1.c 调用算法3.1的程序 */
typedef int SElemType; /* 定义栈元素类型为整型 */

/* c3-1.h 栈的顺序存储表示 */
#define STACK_INIT_SIZE 10 /* 存储空间初始分配量 */
#define STACKINCREMENT 5   /* 存储空间分配增量 */

typedef struct SqStack
{
    SElemType *base; /* 在栈构造之前和销毁之后，base的值为NULL */
    SElemType *top;  /* 栈顶指针 */
    int stacksize;   /* 当前已分配的存储空间max空间，以元素为单位 */
} SqStack;           /* 顺序栈 在同一端插入和删除 判断栈空 则栈顶=栈尾 栈满就是元素等于存储空间的时候 出栈判断是否为空*/


status initStack(SqStack *stack);
status pushStack(SqStack *stack,SElemType e);
status popStack(SqStack *stack,SElemType *e);
status isEmptyStack(SqStack stack);
status isFullStack(SqStack stack);
status clearStack(SqStack *stack);
status destroyStack(SqStack *stack);

status StackTraverse(SqStack S, status (*visit)(SElemType));