#include <stdio.h>
#include <stdlib.h>
#include "ListLinkDouble.h"
#include "../general.h"

status initLinkListDouble(LinkList *L)
{
    // 凡是要修改全局变量 改变指针 或者 某个变量值得 都要 指针作为形参 传入取址作为实参来处理 这样才可以保证修改 不做修改的直接传入结构体指针就好
    //要做修改 即使指针的指针
    *L = (LinkList)malloc(sizeof(struct LNode));
    if (!*L) /* 存储分配失败 */
        exit(OVERFLOW);
    (*L)->next = NULL; /* 指针域为空 */
    (*L)->prior = NULL;
    (*L)->data = 0; //  用头节点的数值存储长度
    return OK;
}

status insertLinkListDouble(LinkList *L, int pos, ElemType e)
{
    LinkList p = *L, s;
    int j = 0;
    while (p && j < pos - 1)
    {
        /* code */
        p = p->next; // 移动到前一个位置就好了，插入pos 则移动 pos - 1次
        j++;
    }
    printf("移动成功了，此时J为%d\n", j);
    if (!p || j > pos - 1)
    { // 所在位置大于pos - 1 就是小于0 以及超过链表长度了 p已经指向NULL 了。

        printf("现在已经超过了指针了或者没有移动j");
        return ERROR;
    }
    s = (LinkList)malloc(sizeof(struct LNode));
    s->data = e;
    printf("赋值成功。");
    s->prior = p;      //新节点前驱指向
    s->next = p->next; //新节点后继指向
    p->next = s;       //断链
    (*L)->data += 1;   //长度加1
    return OK;
}

status isEmptyLinkListDouble(LinkList L)
{
    if (L->data == 0)
    {
        return TRUE;
    }
    return FALSE;
}

int get_length(LinkList L)
{
    return L->data; // 返回第一个节点的数值 也就是长度
}

status deleteElement(LinkList *L, int pos, ElemType *e)
{
    LinkList p = *L, q;
    int j = 0;
    while (p && j < pos - 1)
    {
        p = p->next;
        j++;
    }
    if (!p || j > pos - 1)
    {
        return ERROR;
    }

    q = p->next; //取出删除的节点
    *e = q->data;
    p->next = q->next; // 接链
    q->next->prior = p;
    free(q);
    (*L)->data -= 1;
    return OK;
}

status destroyListDouble(LinkList *L) // 此时（*L的整体是代表着指向LNode结构体 指针 L为指针的指针） // 最保险的可变类型传播还是指针+取址
{
    LinkList p = (*L)->next, q; // 从头开始释放了就不需要释放头结点了 双向 非循环链表 循环链表要稍微注意一下
    while (p != NULL)
    {
        q = p->next;
        free(p);
        p = q;
    }
    free(*L); //L相当于 (*L).next L->next 指针结构体封装了 头结点再释放
    *L = NULL;

    // printf("%d\n", L->data);
    // printf("\n此时内存大小为：%d\n", sizeof(L));
    return OK;
}

status clearList(LinkList *L) // 传入参数时  取地址相当于 指针一层 封一次指针
{
    LinkList p = (*L)->next, q;

    while (p != NULL)
    {
        q = p->next;
        free(p);
        p = q;
    }
    (*L)->data = 0;
    (*L)->next = NULL;
    return OK;
}

status getElement(LinkList L, int pos, ElemType *e)
{
    LinkList p = L;
    int j = 0;
    while ((p && j < pos - 1))
    {
        /* code */
        p = p->next;
        j++;
    }
    if (!p || j > pos - 1)
    {
        return ERROR;
    }
    *e = p->next->data;
    return OK;
}
status getNext(LinkList L, ElemType ele, ElemType *ret)
{
    LinkList p = L;
    ElemType tmp;
    while (p->next != NULL && tmp != ele)
    {
        p = p->next; // 跳过头结点的参数
        tmp = p->data;
    }
    if (p->next == NULL)
    {
        printf("获取后继到空了。\n");
        return ERROR;
    }

    else
    {
        *ret = p->next->data; //获得后继
        return OK;
    }
}

status getPriority(LinkList L, ElemType ele, ElemType *ret)
{
    LinkList p = L;
    ElemType tmp = NULL;
    int j=0;
    while (p->next != NULL && tmp != ele)
    {
        p = p->next; // 跳过头结点的参数
        tmp = p->data;
        j++;
    }
    if (p->next == NULL || j==1)
    {
        printf("\n获取前驱到空了。或者头结点\n");
        return ERROR;
    }

    *ret = p->prior->data; //获得前驱

    return OK;
}
int main(int argc, char const *argv[])
{
    /* code */
    LinkList L;
    status is_init = initLinkListDouble(&L);
    if (is_init == OK)
    {
        printf("\n初始化双向链表成功了。\n");
    }
    int pos = 1;
    insertLinkListDouble(&L, pos, 5);

    for (int idx = 1; idx < 6; idx++)
    {
        insertLinkListDouble(&L, idx, idx * 2);
    }
    LinkList pn = L;
    insertLinkListDouble(&L, 3, 12);

    // clearList(&L);
    printf("此时双向链表的长度为：%d\n", L->data);
    for (int i = 0; i < L->data; i++)
    {
        printf(",%d", pn->next->data);
        pn = pn->next;
    }
    // clearList(&L);

    ElemType e;

    // clearList(&L);

    // printf("此时L还存在内存中吗?%d", sizeof(*L)); // 在函数里面操作的是指针的值也就是要传入一个指针地址了
    // destroyListDouble(L);
    // printf("此时L还存在内存中吗?%d",sizeof(*L));

    // printf("\n%d\n", L->next);
    getElement(L, 3, &e); //* 可以理解为访问地址 & 可以理解为获得地址

    printf("\n获取后的数值为：%d\n", e);

    // destroyListDouble(&L); //执行此步之后就没有Null了
    if ((L) == NULL)
    {
        printf("此时L已经是NULL了");
    }
    // if ((*L).next == NULL)
    // {
    //     printf("L.next 是NULL");
    // }
    // printf("\n此时内存大小为：%d\n", sizeof((*L)));
    ElemType ed;
    LinkList p2 = L;
    deleteElement(&L, 4, &ed); //* 可以理解为访问地址 & 可以理解为获得地址
    printf("此时删除的元素为：%d\n", ed);
    printf("此时双向链表的长度为：%d\n", L->data);
    for (int i = 0; i < L->data; i++)
    {
        printf(",%d", p2->next->data);
        p2 = p2->next;
    }
    ElemType ret1, ret2;
    ElemType dvalue = 2;
    getPriority(L, dvalue, &ret1);
    printf("\n%d的前驱是：%d\n", dvalue, ret1);
    getNext(L, dvalue, &ret2);
    printf("%d的后继是：%d\n", dvalue, ret2);
    return 0;
}
