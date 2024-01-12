import sys
input = sys.stdin.readline

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

root = cursor = ListNode('root')
for char in input().strip():
    new_node = ListNode(char)
    new_node.prev, new_node.next = cursor, cursor.next
    cursor.next = new_node
    cursor = cursor.next

for _ in range(int(input())):
    command = input().strip()
    if command[0] == 'P':
        new_node = ListNode(command[-1])
        new_node.prev, new_node.next = cursor, cursor.next
        cursor.next = new_node
        cursor = cursor.next
        if cursor.next:
            cursor.next.prev = cursor
    elif command == 'L' and cursor.prev:
        cursor = cursor.prev
    elif command == 'D' and cursor.next:
        cursor = cursor.next
    elif command == 'B' and cursor.prev:
        cursor.prev.next = cursor.next
        if cursor.next:
            cursor.next.prev = cursor.prev
        cursor, temp = cursor.prev, cursor
        del temp

output = []
cursor = root.next
while cursor:
    output.append(cursor.val)
    cursor = cursor.next
print(*output, sep='')