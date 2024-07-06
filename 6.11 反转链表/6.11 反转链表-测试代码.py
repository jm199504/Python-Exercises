from solution import ListNode
from solution import reverse_list


def test_reverse_list():
    # 构建链表 [1,2,3,4,5]
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    # 测试逆转链表
    reversed_head = reverse_list(node1)

    # 遍历打印逆转后的链表
    current_node = reversed_head
    example_1_result = []
    while current_node:
        example_1_result.append(current_node.val)
        current_node = current_node.next

    # 判断输出的值是否符合预期
    example_1_expect = [5, 4, 3, 2, 1]
    for i, j in zip(example_1_result, example_1_expect):
        assert i == j


# 运行测试
if __name__ == "__main__":
    test_reverse_list()
    print("All tests passed!")
