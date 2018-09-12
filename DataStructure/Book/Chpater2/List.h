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

Status initList(SqList *L);
Status destroyList(SqList *L);
Status clearList(SqList *L);
Status isEmpty(SqList L);
Status length(SqList L);
Status listInsert(SqList *L,int pos,ElemType e);
Status getElem(SqList L, ElemType *e, int i);
