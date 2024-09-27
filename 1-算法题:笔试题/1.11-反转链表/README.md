## 1.11-反转链表

### 问题描述
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

### 实验示例 1

```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

### 实验示例 2

```
输入：head = [1,2]
输出：[2,1]
```

### 示例代码（迭代法）

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    反转单链表

    参数：
    head: ListNode - 链表的头节点

    返回：
    ListNode - 反转后的链表头节点
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # 保存当前节点的下一个节点
        curr.next = prev  # 反转当前节点的指向
        prev = curr  # 移动 prev 到当前节点
        curr = next_node  # 移动 curr 到下一个节点

    return prev  # 返回反转后的头节点

# 示例测试
# 创建链表 [1, 2, 3, 4, 5]
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

reversed_head1 = reverseList(head1)
# 打印反转后的链表
while reversed_head1:
    print(reversed_head1.val, end=" ")
    reversed_head1 = reversed_head1.next
print()

# 创建链表 [1, 2]
head2 = ListNode(1)
head2.next = ListNode(2)

reversed_head2 = reverseList(head2)
# 打印反转后的链表
while reversed_head2:
    print(reversed_head2.val, end=" ")
    reversed_head2 = reversed_head2.next
print()
```

### 示例代码（递归法）

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    反转单链表

    参数：
    head: ListNode - 链表的头节点

    返回：
    ListNode - 反转后的链表头节点
    """
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)  # 递归反转剩余部分
    head.next.next = head  # 将当前节点的下一个节点的 next 指向当前节点
    head.next = None  # 断开当前节点的 next 指向

    return new_head  # 返回新的头节点

# 示例测试
# 创建链表 [1, 2, 3, 4, 5]
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

reversed_head1 = reverseList(head1)
# 打印反转后的链表
while reversed_head1:
    print(reversed_head1.val, end=" ")
    reversed_head1 = reversed_head1.next
print()

# 创建链表 [1, 2]
head2 = ListNode(1)
head2.next = ListNode(2)

reversed_head2 = reverseList(head2)
# 打印反转后的链表
while reversed_head2:
    print(reversed_head2.val, end=" ")
    reversed_head2 = reversed_head2.next
print()
```

