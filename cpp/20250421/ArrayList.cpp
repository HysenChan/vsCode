#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// 定义结点结构体
typedef struct student
{
    // 数据域
    int num;       // 学号
    int score;     // 分数
    char name[20]; // 姓名
    // 指针域
    struct student *next;
} STU;

void link_creat_head(STU **p_head, STU *p_new)
{
    STU *p_mov = *p_head;
    if (*p_head == NULL) // 当第一次加入链表为空时，head执行p_new
    {
        *p_head = p_new;
        p_new->next = NULL;
    }
    else // 第二次及以后加入链表
    {
        while (p_mov->next != NULL)
        {
            p_mov = p_mov->next; // 找到原有链表的最后一个结点
        }
        p_mov->next = p_new; // 将新申请的节点加入链表
        p_new->next = NULL;
    }
}

// 链表的遍历
void link_print(STU *head)
{
    STU *p_mov;
    // 定义新的指针保存链表的首地址，防止使用head改变原本链表
    p_mov = head;
    // 当指针保存最后一个结点的指针域为NULL时，循环结束
    while (p_mov != NULL)
    {
        // 先打印当前指针保存结点的数据域
        printf("学号:%d, 分数:%d, 姓名:%s\n", p_mov->num, p_mov->score, p_mov->name);

        // 指针后移，保存下一个结点的地址
        p_mov = p_mov->next;
    }
}

// 链表的释放
void link_free(STU **p_head)
{
    // 定义一个指针变量保存头结点的地址
    STU *pb = *p_head;

    while (*p_head != NULL)
    {
        // 先保存p_head指向的结点的地址
        pb = *p_head;
        // p_head保存下一个结点地址
        *p_head = (*p_head)->next;
        // 释放结点并防止野指针
        free(pb);
        pb = NULL;
    }
}

// 链表的查找
// 按照学号查找
STU *link_search_num(STU *head, int num)
{
    STU *p_mov = head;
    while (p_mov != NULL)
    {
        if (p_mov->num == num)
        {
            return p_mov;
        }
        p_mov = p_mov->next;
    }
    return NULL;
}

// 按照姓名查找
STU *link_search_name(STU *head, char *name)
{
    STU *p_mov = head;
    while (p_mov != NULL)
    {
        if (strcmp(p_mov->name, name) == 0)
        {
            return p_mov;
        }
        p_mov = p_mov->next;
    }
    return NULL;
}

// 链表结点的删除
void link_delete_num(STU **p_head, int num)
{
    STU *pb, *pf;
    pb = pf = *p_head;
    if (*p_head == NULL) // 链表为空，不用删
    {
        printf("链表为空，不用删\n");
        return;
    }
    while (pb->num != num && pb->next != NULL) // 循环找，要删除的节点
    {
        pf = pb;
        pb = pb->next;
    }
    if (pb->num == num) // 找到要删除的节点
    {
        if (pb == *p_head) // 删除头结点
        {
            *p_head = pb->next;
        }
        else
        {
            pf->next = pb->next;
        }
        // 释放空间
        free(pb);
        pb = NULL;
    }
    else // 没有找到
    {
        printf("没有找到要删除的节点\n");
    }
}

int main()
{
    STU *head = NULL, *p_new = NULL;
    int num, i;
    printf("请输入链表初始个数:\n");
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        p_new = (STU *)malloc(sizeof(STU));  // 申请一个新节点
        printf("请输入学号、分数、名字:\n"); // 给新节点赋值
        scanf("%d%d%s", &p_new->num, &p_new->score, p_new->name);

        link_creat_head(&head, p_new);
    }
    link_print(head);
    link_free(&head);
    system("pause");
    return 0;
}