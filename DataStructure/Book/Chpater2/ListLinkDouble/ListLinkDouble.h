#include <stdio.h>

typedef int status;
typedef int ElemType;

/* 双向链表 有前继和后驱 头节点无前驱 尾节点无后继 */
struct LNode
{
    ElemType data;
    struct LNode *prior;
    struct LNode *next;
};
typedef struct LNode *LinkList; /* 另一种定义LinkList的方法 LinkList 本来就是指针类型的了* 结构体指针 是多了一层引用 如果再LinkList *L 则为 */
// Linklist L 相当于 LNode *L 定义了一个结构体指针类型

status initLinkListDouble(LinkList *Lkl);  //初始化一个双向链表
status insertLinkListDouble(LinkList *Lkl, int pos, ElemType value);  // 在第pos个位置前插入一个元素
status isEmptyLinkListDouble(LinkList Lkl);  // 判断链表是否为空
int get_length(LinkList L);  // 获取链表长度
status getElement(LinkList L,int pos,ElemType *e);  //获得第pos个位置的元素并 用e返回
// status destroyListDouble(LinkList L);  // 销毁链表 内存也释放掉 一个节点一个节点的释放
status destroyListDouble(LinkList *L);  // 销毁链表 内存也释放掉 一个节点一个节点的释放
status clearList(LinkList *L);  //清空重置链表  变成空的双向链表
status deleteElement(LinkList *L, int pos, ElemType *e); // 删除第pos个元素 并用e返回该元素
status getPriority(LinkList L,ElemType ele,ElemType *ret);
status getNext(LinkList L,ElemType ele,ElemType *ret);
