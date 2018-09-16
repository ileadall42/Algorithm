#include <stdio.h>

typedef int Status;
typedef int ElemType;

#define LIST_INIT_SIZE 100
#define LISTINCEREMENT 10

typedef struct
{
    ElemType *elem;
    int length;
    int listsize;
} SqList;

Status initList(SqList *L);                        //初始化一个线性表，利用指针来存储数据，不是用数组。
Status listInsert(SqList *L, int pos, ElemType e); //往L 线性表的位置pos处插入 类型为ElemType的元素e
Status isEmpty(SqList L);                          // 判断是否为空
Status getElem(SqList L, int i, ElemType *e);
Status destroyList(SqList *L);
Status clearList(SqList *L);
Status deleteElem(SqList *L, int i, ElemType *e);
Status travelList(SqList L, void (*vi)(ElemType *));
