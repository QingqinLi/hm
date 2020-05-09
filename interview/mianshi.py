# 数组，重复数字，找到重复的数字
def find_nums(l):
    d = {}
    result_list = []
    for i in l:
        if i not in result_list:
            result_list.append(i)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d, result_list


if __name__ == '__main__':
    l = [1, 3, 4, 5, 5, 6, 7, 6, 1, 10]
    print(find_nums(l))


# 二叉树的遍历

def tree(root):
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def tree2(root):
    result = []

    def dfs(node, result):
        if not node:
            return
        result.append(node.val)
        dfs(node.left, result)
        dfs(node.right, result)
    dfs(root, result)
    return result


# 两个栈实现一个队列
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out == []:
            if self.stack_in:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
            else:
                return -1
        return self.stack_out.pop()

