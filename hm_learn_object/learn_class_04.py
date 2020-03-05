class Tool(object):
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        # 访问类属性
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("刀")
print(Tool.count, tool1.name)