
#include "general.h"
typedef int status;

typedef int QElemType; /* 定义队元素类型为整型 */

/* c3-2.h 单链队列－－队列的链式存储结构 */
typedef struct QNode
{
    QElemType data;
    struct QNode *next;
} QNode, *QueuePtr;

typedef struct
{
    QueuePtr front, rear; /* 队头、队尾指针 */
} LinkQueue;