#include <stdio.h>

typedef int status;
typedef int ElemType;

/* c2-2.h 线性表的单链表存储结构 */
struct LNode
{
    ElemType data;
    struct LNode *next;
};
typedef struct LNode *LinkList; /* 另一种定义LinkList的方法 LinkList 本来就是指针类型的了*/

status initLinkList(LinkList *Lkl);
status insertLinkList(LinkList Lkl,int pos,ElemType value);
status isEmptyLinkList(LinkList Lkl);
status getElement(LinkList Lkl,int pos,ElemType *value);
status deleteElement(LinkList Lkl, int pos,ElemType *e);
status travelLinkList(LinkList Lkl, void (*vi)(ElemType value));
int length(LinkList Lkl);