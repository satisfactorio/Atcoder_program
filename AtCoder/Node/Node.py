class Node:
    # コンストラクタ
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Search the given value.
    # If this operation is successful, return true, otherwise, false.
    def search(self, value):
        # 探索目標と一致したらTrueを返す
        if (value == self.value):
            print("Exist {}.".format(value))
            return True

        # 探索目標がノードの値より小さいならば左のノードを探索する
        if (value < self.value):
            if (self.left != None):
                return self.left.search(value)

            # このノードが葉の場合探索失敗
            print("Not exist {}.".format(value))
            return False

        # 探索目標がノードの値より大きいならば右のノードを探索する
        if (value > self.value):
            if (self.right != None):
                return self.right.search(value)

            # このノードが葉の場合探索失敗
            print("Not exist {}.".format(value))
            return False

    # Insert the given value to the node.
    # If this operation is successful, return true, otherwise false.
    def insert(self, value):
        # 挿入する値が存在する場合は挿入失敗とする
        if (value == self.value):
            print("Failed to insert {}.".format(value))
            return False

        # 挿入する値がノードの値より小さいなら左のノードに入れる
        if (value < self.value):
            # ノードがないなら新しく作る
            if (self.left == None):
                self.left = Node(value)
                print("Succeeded to insert {}.".format(value))
                return True

            # ノードがあるならそのノードに挿入処理をさせる
            else:
                return self.left.insert(value)

        # 挿入する値がノードの値より大きいなら右のノードに入れる
        if (value > self.value):    
            if (self.right == None):
                self.right = Node(value)
                print("Succeeded to insert {}.".format(value))
                return True
            else:
                return self.right.insert(value)

    def printTree(self):
        print("Value: {}".format(self.value))
        if(self.left != None):
            self.left.printTree()
        if(self.right != None):
            self.right.printTree()
        
        
    
    
