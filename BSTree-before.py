#! /usr/bin/env python

# How to represent a binary tree?

# datatype def'n:
#  A BSTree is either:
#    - False,                              (interpretation: empty tree)
#    - ( [number], [BSTree], [BSTree] )    (interpretation: number at root, and left-, right- subtrees)
#                                           we'll call this non-empty tree a "Branch".

myData = (57, 
          (18,
           (2,False,False),
            (35, 
            (20,False,False), 
            (40,False,False))),
          (78,
           False,
           False))

#myData[0] -- value at root
#myData[1] -- left  child
#myData[2] -- right child



# wrappers, so we can act like these tuples have named-fields
def val(  aBSTree): return aBSTree[0]
def left( aBSTree): return aBSTree[1]
def right(aBSTree): return aBSTree[2]



# constructor, predicate:
def isEmpty( aBSTree): return aBSTree==mt
def newBranch( val, l, r ): return (val,l,r)

mt = False    # convenient variable/name for the empty-tree



t1 = newBranch(29,       
               newBranch(2,mt,mt),
               newBranch(35,     
                         newBranch(30,mt,mt),
                         newBranch(44,mt,mt)))              

assert val(t1) == 29
assert left(t1) == (2,mt,mt)
assert val(left(right(t1))) == 30 



# Template, for *any* function processing a BSTree:
#
# anyTreeFunc : BSTree -> ???
#
def anyTreeFunc( t ):
  return answer_for_empty  if isEmpty(t) else \
         somehowCombine( val(t), anyTreeFunc(left(t)), anyTreeFunc(right(t)) )


# size : BSTree -> natnum
#
def size( t ):
  return answer_for_empty  if isEmpty(t) \
    else somehowCombine( val(t), size(left(t)), size(right(t)) )

assert size(mt) == 0
assert size((50,mt,mt)) == 1
assert size(t1) == 5


# height : BSTree -> natnum
#
def height( t ):
  return answer_for_empty if isEmpty(t) \
    else somehowCombine( val(t), anyTreeFunc(left(t)), anyTreeFunc(right(t)) )

assert height(mt) == 0
assert height((50,mt,mt)) == 1
assert height(t1) == 3


# contains_v1 : BSTree, number -> boolean
#
def contains_v1( t, target ):
  return answer_for_empty if isEmpty(t) \
    else somehowCombine( val(t), contains_v1(left(t)), contains_v1(right(t)) )

assert contains_v1(mt, 50)         == False
assert contains_v1((50,mt,mt), 50) == True
assert contains_v1((50,mt,mt), 37) == False
assert contains_v1(t1,29) == True
assert contains_v1(t1, 2) == True
assert contains_v1(t1,35) == True
assert contains_v1(t1,30) == True
assert contains_v1(t1,44) == True
assert contains_v1(t1,31) == False


# What is the Running-time of each of the above
# functions, `size`  `height`   `contains_v1` ?



#######################

# The Binary **Search** Tree ("BST") Property:
#   - holds for `mt`
#   - For a non-empty tree t, holds if
#     val(left(t))  <=  val(t)  <= val(right(t))    (assuming those exist)
#     and left(t),right(t) also have the BST Property.



# contains : BSTree, number -> boolean
#
def contains( t, target ):
  return answer_for_empty if isEmpty(t) \
    else somehowCombine( val(t), contains(left(t)), contains(right(t)) )

assert contains(mt, 50)         == False
assert contains((50,mt,mt), 50) == True
assert contains((50,mt,mt), 37) == False
assert contains(t1,29) == True
assert contains(t1, 2) == True
assert contains(t1,35) == True
assert contains(t1,30) == True
assert contains(t1,44) == True
assert contains(t1,31) == False


# smallest : BSTree -> num-or-None
#
def smallest(t):
  return answer_for_empty if isEmpty(t) \
    else somehowCombine( val(t), smallest(left(t)), smallest(right(t)) )
    

# Or, here's a different, sneaky technique:
# Walk down the right-hand-branch, keeping track of the previously-seen item.

# biggest : BSTree -> num-or-None
#
def biggest(t):
    return biggestOr(t,None)

# biggestOr : BSTree, any -> any
#
def biggestOr(t,biggestSeenSoFar):
    return biggestSeenSoFar if isEmpty(t) else \
           biggestOr(right(t),val(t))


assert biggest( (7,mt,mt) ) == 7
#print( biggest( t1 ) )
assert biggest( t1 ) == 44
assert smallest( (7,mt,mt) ) == 7
assert smallest( t1 ) == 2



# insert : BSTree, num -> BSTree
def insert( t, n ):
  if isEmpty(t):
    return some_base_case_answer
  else:
    somehowCombine( val(t),  insert(left(t),n),  insert(right(t),n))



assert insert( mt, 77 ) == (77,mt,mt)
assert insert( (50,mt,mt), 77 ) == (50,mt,(77,mt,mt))
assert insert( (50,mt,mt), 22 ) == (50,
                                    (22,mt,mt),
                                    mt)
assert t1 == (29,       
              (2,mt,mt),
              (35,     
               (30,mt,mt),
               (44,mt,mt)))   

assert insert(t1,32) == (29,       
                          (2,mt,mt),
                          (35,     
                           (30,
                             mt,
                             (32,mt,mt)),
                           (44,mt,mt)))   


# Btw: we can use `and`,`or` if we *really* wanted to keep using
# the 'if-else' expression rather than the 'if-else' statement:
#
#def insert( t, n ):
#  return newBranch(n,mt,mt) if isEmpty(t) else \
#         ((val(t) < n) and newBranch(val(t),left(t),insert(right(t),n))) \
#         or newBranch(val(t),insert(left(t),n),right(t)) 






# To delete from a BSTRee:
#   - deleting a leaf easy -- just return empty tree
#   - deleting the root: "replace" it with the smallest(right)),
#      OR biggest(left(t))

# delete : BSTree, num -> BSTree
#    pre-condition: t != mt
#
def delete( t, n ):
  if isEmpty(t):
    raise f"can't delete {n} from the empty-tree {t}"
  else:
    if n < val(t):
      return newBranch(val(t), delete(left(t),n), right(t))
    elif n > val(t):
      return newBranch(val(t), left(t), delete(right(t),n))
    else: # n==val(t) -- delete the root
      if not(isEmpty(right(t))):
         replacement = smallest(right(t))
         return newBranch(replacement, left(t), delete(right(t),replacement))
      elif not(isEmpty(left(t))):
         replacement = biggest(left(t))
         return newBranch(replacement, delete(left(t),replacement), right(t))
         # Alternately, since we know isEmpty(right), we could just return left(t)
      else: # deleting root, whose children are both empty:
        return mt
        

# run-time of contains, insert, and delete, in a BSTree:
#     for a tree of height h, it takes O(h) steps.
#
#  IF the tree is (relatively) balanced, then height is log(n) -- yay!
#
# BUT: how to keep tree balanced???

###############
# "AVL Trees" -- self-balancing, after inserts and deletes.
#
#
#  We call a tree t "AVL Balanced" if:
#    | height(left) - height(right) | <= 1,
#  and both left and right are themselves AVL balanced.
#
# We will show how to insert/delete into a balanced, so that they *stay* balanced.
#
# - We'll do it by using tree rotations:
#   

t23 = (60,mt,mt)
t4  = (99,mt,mt)

# do a counter-clockwise rotation on a BSTree,
# maintaining the binary-search-tree invariant (ordering).
# pre-condition: t and right(t) are both non-empty BSTrees.
#
def rotateCCW( t ):
    # see diagram https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/AVL-simple-left_K.svg/388px-AVL-simple-left_K.svg.png
    X   = val(t)
    t1  = left(t)
    Z   = val(right(t))
    t23 = left(right(t))
    t4  = right(right(t))
    return (Z, (X,t1,t23), t4)

assert rotateCCW(  (50,mt,(75,mt,mt)) )  == (75,(50,mt,mt),mt)
assert rotateCCW(  (50,t1,(75,t23,t4)) ) == (75, (50,t1,t23), t4)

# AVL observation:
# when you do an insert or delete, the 
# balance gets messed up by at most 1, so the unbalance is at most 2.
# - if the left side is shorter than the outside-right (by two),
#   then a single rotateCCW fixes.
# - if the left side is shorter than the inside-right (by two),
#   then first rotateCW the right-child, then do a rotateCCW at root.
# - other two mirror-images similarly.
#

# balance: BSTree -> BStree
#   precondition:  abs(height(left(t)) - height(right(t))) <= 2
#   postcondition: for the returned tree `r`,
#                  abs(height(left(r)) - height(right(r))) <= 1
#                  and it still has binary-search-tree property.
#
def balance(t):
   if t==mt: return t
   elif height(left(t)) - height(right(t)) <= 1: return t
   else:
       hl = height(left(t))
       hr = height(right(t))
       if (hl == hr - 2): # left side short
          if hl == height(right(right(t))) - 1: 
             # the unbalance is on outside
             return rotateCW(t)
          else:
             # the unbalance is on inside; 2 rotations needed:
             return rotateCCW( (val(t),left(t),rotateCW(right(t))) )
       else:             # right side short
          # TODO: add mirror-image of above if-else
          pass

# TODO: update our 3-tuple to keep one more field: the (cached) height,
#    to avoid O(n) time for each call to `height`.

