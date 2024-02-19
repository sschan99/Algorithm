import sys
sys.setrecursionlimit(100000)

def postorder(tree, x):
    if tree[x][0]:
        postorder(tree, tree[x][0])
    if tree[x][1]:
        postorder(tree, tree[x][1])
    print(x)

def main():
    data = list(map(int, sys.stdin.readlines()))
    
    root = data[0]
    tree = {root: [None, None]}
    for node in data[1:]:
        now = root
        while True:
            i = 0 if now > node else 1
            if tree[now][i] is None:
                tree[now][i] = node
                tree[node] = [None, None]
                break
            now = tree[now][i]
    
    postorder(tree, root)

if __name__ == '__main__':
    main()