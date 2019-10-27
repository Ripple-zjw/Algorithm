class TreeNode:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def search(self, val):
        tail = self.root
        while tail and tail.val != val:
            if val < tail.val:
                tail = tail.left
            else:
                tail = tail.right
        return tail

    def inorder_tree(self):
        ans = []
        stack = []
        tail = self.root
        while tail or len(stack) > 0:
            if tail:
                stack.append(tail)
                tail = tail.left
            else:
                tail = stack.pop()
                ans.append(tail.val)
                tail = tail.right
        return ans

    def minimum(self):
        tail = self.root
        while tail.left:
            tail = tail.left
        return tail.val

    def maximum(self):
        tail = self.root
        while tail.right:
            tail = tail.right
        return tail.val

    def successor(self, val):
        tail = self.search(val)
        if tail.right:
            tail = tail.right
            while tail.left:
                tail = tail.left
            return tail
        pa = tail.parent
        while pa and pa.right == tail:
            tail = pa
            pa = pa.parent
        return pa

    def predecessor(self, val):
        tail = self.search(val)
        if tail is None:
            return tail
        if tail.left:
            tail = tail.left
            while tail.right:
                tail = tail.right
            return tail
        pa = tail.parent
        while pa and pa.left == tail:
            tail = pa
            pa = pa.parent
        return pa

    def insert(self, val):
        tail = self.root
        tp = None
        newNode = TreeNode(val)
        while tail:
            tp = tail
            if tail.val < val:
                tail = tail.right
            else:
                tail = tail.left
        newNode.parent = tp
        if tp is None:
            self.root = newNode
        elif val < tp.val:
            tp.left = newNode
        else:
            tp.right = newNode
        return True

    def transplant(self, old, new):
        if old.parent is None:
            self.root = new
        elif old.parent.left == old:
            old.parent.left = new
        else:
            old.parent.right = new
        if new:
            new.parent = old.parent

    def delete(self, val):
        tail = self.search(val)
        if tail is None:
            return False
        if tail.left is None:
            self.transplant(tail, tail.right)
        elif tail.right is None:
            self.transplant(tail, tail.left)
        else:
            rpnode = tail.right
            while rpnode.left:
                rpnode = rpnode.left
            if rpnode.parent != tail:
                self.transplant(rpnode, rpnode.right)
                rpnode.right = tail.right
                rpnode.right.parent = rpnode
            self.transplant(tail, rpnode)
            rpnode.left = tail.left
            rpnode.left.parent = rpnode
        return tail


if __name__ == '__main__':
    bst = BinarySearchTree(1)
    # from random import randint
    # for i in range(30):
    #     bst.insert(randint(1, 100))
    # bstList = bst.inorder_tree()
    # # print(bst.minimum())
    # # print(bst.maximum())
    # print(bstList)
    # bst.delete(bstList[3])
    # bst.delete(bstList[4])
    # bst.delete(bstList[5])
    # bstList = bst.inorder_tree()
    # print(bstList)
    # print(bst.successor(bstList[3]).val)
    # print(bst.predecessor(bstList[23]).val)
    # print(bstList[23])
    from time import perf_counter
    st = perf_counter()
    for i in range(30001):
        bst.insert(i)
    bst.search(30000)
    print(perf_counter() - st)
