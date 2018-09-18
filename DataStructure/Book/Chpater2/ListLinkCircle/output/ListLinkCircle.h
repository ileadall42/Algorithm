#include <stdio.h>

typedef int status;
typedef int ElemType;

/* c2-2.h 线性表的循环链表存储结构 在初始化的时候要把尾指针 指向自己 插入的时候要 如果插入在中间 位置 则原来操作即可，如果插入在末端，则需要
将末端的对位指针指向 该节点就可以了 删除也是同理*/
struct LNode
{
    ElemType data;
    struct LNode *next;
};
typedef struct LNode *LinkList; /* 另一种定义LinkList的方法 LinkList 本来就是指针类型的了*/

status initLinkList(LinkList *Lkl);
status insertLinkList(LinkList Lkl, int pos, ElemType value);
status isEmptyLinkList(LinkList Lkl);
status getElement(LinkList Lkl, int pos, ElemType *value);
status deleteElement(LinkList Lkl, int pos, ElemType *e);
status travelLinkList(LinkList Lkl, void (*vi)(ElemType value));
int length(LinkList Lkl);