from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = ListNode()
        dummy = ret
        curr = ret

        while len(lists) != 0:
            print(lists, len(lists))
            tmp = []

            for ls in lists:
                tmp.append(ls.val)

            m = min(tmp)
            curr.val = m
            curr.next = ListNode()
            curr = curr.next

            i = tmp.index(m)
            lists[i] = lists[i].next
            if lists[i] is None:
                lists.remove(lists[i])

        return ret

    def print_list_node(self, nodes):
        while nodes is not None:
            print(f"{nodes.val}", end="-")
            nodes = nodes.next

        print("")


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    ins = Solution()

    ret = ins.mergeKLists(lists)
    ins.print_list_node(ret)
    #ins.print_list_node(list1)