#include <stdio.h>
#include "List.h"
#include "general.h"
#include <stdlib.h>

typedef int Status;
typedef int ElemType;

#define LIST_INIT_SIZE 100
#define LISTINCREMENT 10

/* bo2-1.c 顺序表示的线性表(存储结构由c2-1.h定义)的基本操作(12个) */
Status initList(SqList *L) /* 算法2.3 */
{                          /* 操作结果：构造一个空的顺序线性表 */
    (*L).elem = (ElemType *)malloc(LIST_INIT_SIZE * sizeof(ElemType));
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
    q = (*L).elem + i - 1;                             /* q为插入位置 */
    for (p = (*L).elem + (*L).length - 1; p >= q; --p) /* 插入位置及之后的元素右移 */
        *(p + 1) = *p;
    *q = e;        /* 插入e */
    ++(*L).length; /* 表长增1 */
    return OK;
}

int main(int argc, char const *argv[])
{
    /* code */
    SqList La;
    
    SqList L;
    ElemType e, e0;
    Status i;
    int j, k;
    i = initList(&L);
    printf("初始化L后：L.elem=%u L.length=%d L.listsize=%d\n", *(L.elem), L.length, L.listsize);
    for (j = 1; j <= 5; j++)
        i = listInsert(&L, 1, j);
    printf("在L的表头依次插入1～5后：*L.elem=");

    printf("初始化数组成功了。\n");
    for (j = 1; j <= 5; j++)
        printf("%d ", *(L.elem + j - 1));
    printf("\n");

    return 0;
}
