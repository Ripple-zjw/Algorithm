class TreeNode:
    def __init__(self, val, point=None):
        self.val = val
        self.left = point
        self.right = point
        self.parent = point
        self.color = False  # False为红 True为黑


class RedBlackTree:
    def __init__(self, val):
        self.nil = TreeNode(None)
        self.nil.color = True
        self.root = TreeNode(val, point=self.nil)
        self.root.color = True

    def left_rotate(self, x: TreeNode):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: TreeNode):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, val: int):
        z = TreeNode(val, point=self.nil)
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if x.val <= z.val:
                x = x.right
            else:
                x = x.left
        z.parent = y
        if y is self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        self.insert_fixup(z)

    def insert_fixup(self, z: TreeNode):
        while z.parent.color is False:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color is False:  # y的叔节点为红
                    y.color = True
                    z.parent.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                    continue
                elif z.parent.right == z:  # y的叔节点为黑且z是右孩子
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = True  # y的叔节点为黑且z是左孩子
                z.parent.parent.color = False
                self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color is False:
                    y.color = True
                    z.parent.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                    continue
                elif z.parent.left == z:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = True
                z.parent.parent.color = False
                self.left_rotate(z.parent.parent)
        self.root.color = True

    def transplant(self, u: TreeNode, v: TreeNode):
        if u.parent is self.nil:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self) -> int:
        z = self.root
        while z.left is not self.nil:
            z = z.left
        return z.val

    def maximum(self) -> int:
        z = self.root
        while z.right is not self.nil:
            z = z.right
        return z.val

    def delete(self, val: int):
        z = self.search(val)
        y = z
        y_origin = y.color
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = z.right
            while z.left is not self.nil:
                z = z.left
            y_origin = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_origin is True:
            self.delete_fixup(x)

    def delete_fixup(self, x: TreeNode):
        while x is not self.root and x.color is True:
            if x.parent.left == x:
                w = x.parent.right
                if w.color is False:  # 情况1 x的兄弟节点时红色
                    w.color = True
                    x.parent.color = False
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color is True and w.right.color is True:  # 情况2 x兄弟节点为黑，且它的两个子节点为黑。
                    w.color = False
                    x = x.parent
                elif w.right.color is True:  # 情况3 x兄弟节点为黑且它的左孩子为红，右孩子为黑
                    w.color = False
                    w.left.color = True
                    self.right_rotate(w)
                    w = x.parent.right
                if w.right.color is False:  # 情况4 兄弟节点为黑，且右孩子为红
                    w.color = x.parent.color
                    x.parent.color = True
                    w.right.color = True
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color is False:
                    w.color = True
                    x.parent.color = False
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color is True and w.right.color is True:
                    w.color = False
                    x = x.parent
                elif w.left.color is True:
                    w.right.color = True
                    w.color = False
                    self.left_rotate(w)
                    w = x.parent.left
                if w.left.color is False:
                    w.color = x.parent.color
                    x.parent.color = True
                    w.left.color = True
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = True

    def search(self, val: int) -> TreeNode:
        z = self.root
        while z.val != val and z is not self.nil:
            if z.val <= val:
                z = z.right
            else:
                z = z.left
        return z

    def successor(self, val: int) -> int:
        z = self.search(val)
        if z.right is not self.nil:
            z = z.right
            while z.left is not self.nil:
                z = z.left
            return z.val
        y = z.parent
        while y is not self.nil and z == y.right:
            z = y
            y = y.parent
        return y.val

    def predecessor(self, val: int):
        z = self.search(val)
        if z is None:
            return z
        if z.left is not self.nil:
            z = z.left
            while z.right is not self.nil:
                z = z.right
            return z.val
        y = z.parent
        while y is not self.nil and y.left == z:
            z = y
            y = y.parent
        return y.val

    def inorder_tree(self):
        x = self.root
        stack = []
        ans = []
        while x is not self.nil or len(stack) > 0:
            if x is not self.nil:
                stack.append(x)
                x = x.left
            else:
                x = stack.pop()
                ans.append(x.val)
                x = x.right
        return ans


if __name__ == '__main__':
    rbt = RedBlackTree(1)
    # for i in range(2, 100):
    #     rbt.insert(i)
    # print(rbt.inorder_tree())
    # rbt.delete(5)
    # print(rbt.inorder_tree())
    # rbt.delete(1)
    # print(rbt.inorder_tree())
    # print(rbt.search(50).val)
    # print(rbt.search(100).val)
    from time import perf_counter

    for i in range(500000):
        rbt.insert(i)
    st = perf_counter()
    print(rbt.search(415000).val)
    print(perf_counter() - st)
