from typing import List

class Node:
  def __init__(self,val="",children=[]):
    self.val = val
    self.children = []
class Solution:
  def findHierarchy(array:List[List[str]]):
    # Find top level parent:
    top = set()
    children = []
    mydict = {}
    #print(array)
    for member in array:
      #print(member)
      children.append(member[1])
      if member[0] not in mydict:
        mydict[member[0]] = []
      mydict[member[0]].append(member[1])
    for member in array:
      if member[0] not in children:
        top.add(member[0])
    print(mydict)
    def buildTree(parent,childNames):
      nonlocal mydict
      if not parent or len(childNames) == 0:
        return
      for children in childNames:
        print(children)
        newNode = Node(children)
        if children in mydict:
          buildTree(newNode,mydict[children])
        parent.children.append(newNode)
    top = list(top)
    root = Node(top[0])
    buildTree(root,mydict[top[0]])
    def print_tree(root,space):
      if root:
        print(" "*space + root.val)
      if len(root.children) > 0:
        for child in root.children:
          print_tree(child,space*2)

    print_tree(root,1)