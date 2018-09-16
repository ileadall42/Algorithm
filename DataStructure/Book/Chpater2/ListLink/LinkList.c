#include <stdlib.h>
#include "../general.h"
#include "LinkList.h"

status initLinkList(LinkList *L)
{
    *L = (LinkList)malloc(sizeof(struct LNode)); /* 产生头结点,并使L指向此头结点 */
    if (!*L)                                     /* 存储分配失败 */
        exit(OVERFLOW);
    (*L)->next = NULL; /* 指针域为空 */
    return OK;
}

status insertLinkList(LinkList L, int pos, ElemType value)
{
    int j = 0;
    LinkList p = L, s;
    while (p && j < pos - 1) /* 寻找第i-1个结点 */
    {
        p = p->next;
        j++;
    }
    if (!p || j > pos - 1) /* i小于1或者大于表长 */
        return ERROR;
    s = (LinkList)malloc(sizeof(struct LNode)); /* 生成新结点 */
    s->data = value;                            /* 插入L中 */
    s->next = p->next;
    p->next = s;
    L->data += 1;
    return OK;
}

status deleteElement(LinkList L, int pos, ElemType *e)
{
    int j = 0;
    LinkList p = L, s;
    while (p && j < pos - 1)
    { // 找到要删除的元素 例如pos=1 删除第一个元素 则j=0 删除第2个元素 则可以执行一次 j=1
        p = p->next;
        j++;
    }
    if (!p || j > pos - 1)
    {
        return ERROR;
    }
    *e = p->next->data;
    p->next = p->next->next; // p->next->data 就是要删除元素的值
    L->data -= 1;            // 长度减1
    return OK;
}

int length(LinkList L)
{
    // int j = 0;
    // while (L)
    // {
    //     printf("此时的数值为：%d \n", L->data);
    //     L = L->next;
    //     j++;
    // }

    return L->data; // 头结点是用来存储长度的
}
status isEmptyLinkList(LinkList L)
{
    if (L->data == 0)
    {
        return TRUE;
    }
    return FALSE;
}

status getElement(LinkList L, int pos, ElemType *e)
{
    int j = 0;
    LinkList p = L, s;
    while (p && j < pos) /* 寻找第i-1个结点 */
    {
        p = p->next;
        j++;
    }
    if (!p || j > pos) /* i小于1或者大于表长 */
        return ERROR;
    *e = p->data;
    return OK;
}
void visit(ElemType value)
{
    printf(",%d,", value);
}
status travelLinkList(LinkList L, void (*vi)(ElemType value))
{
    LinkList p = L;
    ElemType data;
    printf("开始调用函数: \n");
    while (p->next!=NULL)
    {
        p = p->next; // 第一个的时候 刚刚好跳过
        data = p->data;
        // printf(",%d ",data);
        vi(data);
    }
    return OK;
}

int main(int argc, char const *argv[])
{
    printf("\n开始写单向链表的程序了：\n");
    LinkList L;

    status isOK;
    isOK = initLinkList(&L);
    if (isOK == OK)
    {
        printf("\n 初始化单向链表成功。\n");
    }

    for (int i = 1; i < 10; i++)
    {
        /* code */
        insertLinkList(L, i, i);
    }
    printf("这个链表的长度此时为：%d \n", length(L)); // 第一个元素为0  是头结点
    printf("\n这个链表是否为空：%d (0 为否 1 为是)\n", isEmptyLinkList(L));
    ElemType e, ed;
    getElement(L, 3, &e);
    printf("这个链表的第 %d 个元素为：%d\n", 3, e);
    deleteElement(L, 5, &ed);
    deleteElement(L, 3, &ed);
    printf("这个链表删除了第%d个元素，其元素值为：%d \n", 3, ed);
    travelLinkList(L, visit);
    return 0;
}
