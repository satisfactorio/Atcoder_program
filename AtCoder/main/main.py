import BinaryTree

def main():
    root = BinaryTree.Node(10)
    root.insert(8)
    root.insert(12)

    searchedValue = 9
    root.search(searchedValue)

    root.insert(10)
    root.insert(9)

    root.printTree()


if __name__ == "__main__":
    main()
