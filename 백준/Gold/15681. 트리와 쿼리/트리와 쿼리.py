from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def main():
    N, R, Q = map(int, input().split())

    connect = defaultdict(list)
    for _ in range(N - 1):
        U, V = map(int, input().split())
        connect[U].append(V)
        connect[V].append(U)

    children_dict = defaultdict(list)
    parent_dict = dict()
    def make_tree(current, parent):
        for node in connect[current]:
            if node != parent:
                children_dict[current].append(node)
                parent_dict[node] = current
                make_tree(node, current)
    make_tree(R, -1)

    size = dict()
    def count_subtree_nodes(current):
        size[current] = 1
        for child in children_dict[current]:
            count_subtree_nodes(child)
            size[current] += size[child]
    count_subtree_nodes(R)

    for _ in range(Q):
        U = int(input())
        print(size[U])

if __name__ == '__main__':
    main()