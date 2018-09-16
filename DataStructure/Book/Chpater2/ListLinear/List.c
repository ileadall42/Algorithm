#include <stdio.h>
#include "List.h"
#include "../general.h"
#include <stdlib.h>

typedef int Status;
typedef int ElemType;

#define LIST_INIT_SIZE 100
#define LISTINCREMENT 10

/* bo2-1.c 顺序表示的线性表(存储结构由c2-1.h定义)的基本操作(12个) */
// 在C语言里面，要想传引用 也就是传真正的值 也就是传可变对象  就相当于在形参定义上为 指针  传参数的时候传指针
// 如果变量不是指针类型  只要取值&  取地址传进去就可以了。  要时刻了解每个地方的值到底是什么
Status initList(SqList *L)                                             /* 算法2.3 */
{                                                                      /* 操作结果：构造一个空的顺序线性表 */
    (*L).elem = (ElemType *)malloc(LIST_INIT_SIZE * sizeof(ElemType)); // 强制转换成 element type 的指针类型 让其指向第一个地址
    if (!(*L).elem)
        exit(OVERFLOW);             /* 存储分配失败 */
    (*L).length = 0;                /* 空表长度为0 */
    (*L).listsize = LIST_INIT_SIZE; /* 初始存储容量 */
    return OK;
}
Status listInsert(SqList *L, int i, ElemType e) /* 算法2.4 */
{                                               /* 初始条件：顺序线性表L已存在，1≤i≤ListLength(L)+1 */
    /* 操作结果：在L中第i个位置之前插入新的数据元素e，L的长度加1 */
    ElemType *newbase, *q, *p;
    if (i < 1 || i > (*L).length + 1) /* i值不合法 */
        return ERROR;
    if ((*L).length >= (*L).listsize) /* 当前存储空间已满,增加分配 */
    {
        newbase = (ElemType *)realloc((*L).elem, ((*L).listsize + LISTINCREMENT) * sizeof(ElemType));
        if (!newbase)
            exit(OVERFLOW);             /* 存储分配失败 */
        (*L).elem = newbase;            /* 新基址 */
        (*L).listsize += LISTINCREMENT; /* 增加存储容量 */
    }
    q = (*L).elem + i - 1;                             /* q为插入位置 q后的元素都后移了 */
    for (p = (*L).elem + (*L).length - 1; p >= q; --p) /* 插入位置及之后的元素右移 */
        *(p + 1) = *p;
    *q = e; /* 插入e */
    // ++(*L).length; /* 表长增1 */
    (*L).length += 1;
    return OK;
}

Status isEmpty(SqList L)
{
    if ((L).length == 0)
    {
        return TRUE; // 为空
    }
    return FALSE; // 不为空
}

Status getElem(SqList l, int pos, ElemType *e) // pos 从1开始计算的 也可以不从1开始 第一个元素就是0
{
    if (pos < 0 || pos > l.length)
    {
        return ERROR;
    }
    *e = *(l.elem + pos - 1);
    return OK;
}

Status destroyList(SqList *L)
{
    free((*L).elem);
    (*L).elem = NULL;
    (*L).length = 0;
    (*L).listsize = 0;
    return OK;
}
Status clearList(SqList *L)
{
    (*L).length = 0;
    return OK;
}

Status deleteElem(SqList *L, int i, ElemType *e)
{
    if (i < 1 || i > (*L).length)
    {
        return ERROR;
    }
    ElemType *p;
    // p = (*L).elem + i - 1;
    p = (*L).elem + i - 1; /* p为被删除元素的位置 */
    *e = *p;               /* 被删除元素的值赋给e */

    for (int idx = 0; idx < (*L).length - i; idx++)
    {
        /* code */
        p = (*L).elem + i - 1 + idx; // 顺序后移
        *(p) = *(p + 1);
    }
    (*L).length -= 1;

    // *e = *p;
    return OK;
}

Status travelList(SqList L, void (*vi)(ElemType *element))
{
    ElemType *p; //则p为指针的地址  值得地址  vi为函数的地址直接调用就可以不取值
    for (int i = 0; i < (L).length; i++)
    {
        p = (L).elem + i;
        vi(p);
        /* code */
    }
    return OK;
}
void visit(ElemType *value)
{
    printf("此时的值为：%d\n", *value);
}

int main(int argc, char const *argv[])
{
    /* code */

    SqList L;
    ElemType e, e0;
    Status is_init_ok, is_insert_ok;
    int j, k;
    is_init_ok = initList(&L);
    printf("\n 此时数组是否为空：%d", isEmpty(L));
    printf("\n\n");
    if (is_init_ok)
        printf("初始化成功了.\n");
    printf("初始化L后：L.elem=%u L.length=%d L.listsize=%d\n", *(L.elem), L.length, L.listsize);
    for (j = 1; j <= 5; j++)
        is_insert_ok = listInsert(&L, 1, j);
    printf("在L的表头依次插入1～5后：*L.elem=  \n");

    printf("初始化数组成功了。\n");
    for (j = 1; j <= 5; j++)
        printf("%d ", *(L.elem + j - 1));
    printf("\n");
    printf("开始插入数组了。 \n");
    listInsert(&L, 2, 3);
    listInsert(&L, 2, 3);
    listInsert(&L, 2, 4); // 第二个位置 下标从1开始

    printf("数组插入后的结果为。");
    printf("\n 此时数组的长度为：%d \n", L.length);
    for (int idx = 1; idx < L.length + 1; idx++)
    {
        /* code */
        printf("%d ", *(L.elem + idx - 1));
    }
    int idx = 2;
    printf("\n 准备获取第 %d 个元素了。\n", 5);
    Status isOk = getElem(L, idx, &e);
    if (isOk == 1)
    {
        printf("\n 获取第 %d 个元素成功，其值为 %d \n", idx, e);
    }
    else
    {
        printf("获取第5个元素失败了，超出长度或者索引错误。");
    }
    // ElemType e;
    Status is_delete = deleteElem(&L, 3, &e);
    if (is_delete == 1)
    {
        printf("删除元素成功，并成功返回删除的元素为：%d", e);
    }
    else
    {
        printf("删除失败！。");
    }
    printf("\n 此时数组的长度为：%d \n", L.length);
    for (int idx = 1; idx < L.length + 1; idx++)
    {
        /* code */
        printf("%d ", *(L.elem + idx - 1));
    }
    Status is_visit;
    is_visit = travelList(L, visit);
    return 0;
}
