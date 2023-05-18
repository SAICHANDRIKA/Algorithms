#! /usr/bin/env python

import math

### An Implementation of singly-linked, immutable list (from scratch)
### Why? To see it's easy, and to let us talk about exact-code when
### discussing Binary Search Trees (immutable).


# A list is:
#  - the empty list, OR
#  - one number tacked on the front of an existing list of numbers


# Let's represent each of empty-list and number-tacked-onto-front-of-list,
# using our own python (NOT python's built-in lists):
#
# A SList is:
#  - "e", OR
#  - (n,lst) where n is a number, and lst is a SList
  

#Let's have some examples of SList (by this def'n):
"e"                # the empty-list
(2,"e")            # the list containing 2 (and nuttin' else)
(1,(2,"e"))        # the list containing 1 and 2 (and nuttin' else)
(0, (1,(2,"e")) )  # a list of length three


#Given a non-empty SList `lst`, how do I extract the first number in it?
#   (1, (2,"e"))[0]   = 1             (Or, `lst[0]` is named).
#   (1, (2,"e"))[1]   = (2,"e")       
#
#   (1, (2,'e'))[1][0] = (2,"e")[0] = 2
#
#  Here's what I *want* to write:
#      if lst = (0, (1, (2,"e"))), then I want to write:
#      first( lst ) = 0
#      rest( lst ) = (1,(2,"e"))
#
#  To extract the 2nd item:
#      first(rest(lst))
#  To extract the 3rd item:
#      first(rest(rest(lst)))

def first(lst): return lst[0]
def rest(lst):  return lst[1]

#
# in Java people may have written:
#new Node(2, null)
#new Node(1, new Node(2, null) )
#new Node(0, new Node(1, new Node(2, null) ))


#      How to extract the 3rd element from a Slist `lst`?
#      TODO in class
lst = ('a', ('b',('c',"e")) )
# Now extract the item at index 2, using calls to `first`,`rest`:

first(rest(rest(lst))) == 'c'


# isEmpty : SList -> Boolean
# is `lst` empty?
#
def isEmpty(lst):
    return lst=="e"

assert isEmpty("e") == True
assert isEmpty((2,"e")) == False
assert isEmpty((1,(2,"e"))) == False


### We could even write constructors, using conventional names:
def Empty():
    return "e"

def Cons(_first, _rest):
    return (_first,_rest)    # just make a two-tuple







# sum : SList -> number
# return the sum of the elements of `lst`
def sum(lst):
   if isEmpty(lst):
      return 0
   else: 
      return first(lst) + sum(rest(lst))
    

assert sum("e") == 0
assert sum((2,"e")) == 2
assert sum((1,(2,"e"))) == 3

# template for ANY function handling an SList:
#
#def funcForSList( aLst ):
#    if (isEmpty(aLst)):
#        return ...
#    else:
#        return ... first(aLst) ... funcForSList( rest(aLst) )


# - TODO: write the function `length`

# length : SList -> naturalNumber
def length( aLst ):
   if isEmpty(aLst):
      return 0
   else: 
      return 1 + length(rest(aLst))


assert length( "e" ) == 0   
assert length( (17,"e") ) == 1   
assert length( (11,(22,"e")) ) == 2  # because the input is the list containing 1,2  (two items)




# - contains


# contains : number, list-of-number -> boolean
# Return whether `target` occurs in `aLst`.
#
def contains( target, aLst ):
   if isEmpty(aLst):
      return False
   else: 
      return first(aLst)==target or contains(target, rest(aLst))

assert contains( 17, "e" ) == False
assert contains( 17, (5,"e") ) == False
assert contains( 17, (17,"e") ) == True
assert contains( 17, (12, (17,"e")) ) == True
assert contains( 12, (12, (17,"e")) ) == True
assert contains( 99, (12, (17,"e")) ) == False



## can theoretically by more pythonic:
#def contains( target, aLst ):
#    """contains : number, list-of-number -> boolean
#       Return whether `target` occurs in `aLst`."""
#    return False if isEmpty(aLst) else first(aLst)==target or contains( target,  rest(aLst) )



## Steps to follow when writing any function:  (GENERAL design recipe)
#  - make unit tests
#  - template for our data (SList):
#    - handle both cases (empty, and tuple-of-length-2)  with an `if`
#    - if we have several fields, pull them out
#      (think about the type of each, and what function we might want to call on that type)
#      (nine times out of ten: add a recursive, if the types suggest it)
#  - complete the body


# - `max`: 

# This doesn't work -- recurs to base-case, which then raises Excpn.:
#
#def myMax(lst):
#   if isEmpty(lst):
#      raise Exception("can't take myMax of empty lst")
#   else: 
#      return max( first(lst), myMax(rest(lst)) )

# Instead, we use a helper:
#
def myMax(lst):
   if isEmpty(lst):
      raise Exception("can't take myMax of empty lst")
   else: 
      return myMaxOr( rest(lst), first(lst) )
    
  
# return the largest element in `lst`, or `maxSoFar` (whichever larger)
def myMaxOr(lst, maxSoFar):
   if isEmpty(lst):
      return maxSoFar
   else: 
      return myMaxOr(rest(lst), max(maxSoFar, first(lst)))

print( f"I got {myMaxOr( 'e', -2 )}")

assert myMaxOr( "e", -2 ) == -2
assert myMaxOr( (5,"e"), -2 ) == 5
assert myMaxOr( (-5,"e"), -2 ) == -2

assert myMaxOr( (7, (-5,"e")), -2 ) == 7
assert myMaxOr( (-8, (-5,"e")), -2 ) == -2


#assert myMax( "e" ) == -math.inf
assert myMax( (-2,"e") ) == -2
assert myMax( (17,(2,(99,(20,"e")))) ) == 99


#    hmm, what of empty-list?     one soln: `maxHelp(lst,maxSoFar)`; "accumulator"

# - `ref`:
#assert ref( (1,(2,"e")),  0 ) == 1
#assert ref( (1,(2,"e")),  1 ) == 2
#
# Hmm, instead of recurring on list, recur on Natural Numbers.
#  Just like SList was "empty, or Cons(..,lst)", a Natural-Number is either "0, or add1(n)"



    



# - removeAll
#  return a new list, with all occurrences of `target` removed.
def removeAll( target, aLst ):
    if (isEmpty(aLst)):
        return "e"
    else:
        f = first(aLst) 
        restRemoved = removeAll(target, rest(aLst))  
        return restRemoved if target==f else (f, restRemoved )
                   

assert removeAll( 17, "e" ) == "e"
assert removeAll( 17, (5,"e") ) == (5,"e")
assert removeAll( 17, (17,"e") ) == "e"
assert removeAll( 17, (12,(17,"e")) ) == (12,"e")
assert removeAll( 12, (12,(17,"e")) ) == (17,"e")
assert removeAll( 99, (12,(17,"e")) ) == (12,(17,"e"))
assert removeAll( 17, (17,(17,"e")) ) == 'e'
assert removeAll( 17, (17,(18,(17,"e"))) ) == (18,'e')
assert removeAll( 17, (19,(18,(17,"e"))) ) == (19,(18,'e'))


# Our SLists are "immutable" -- once a tuple-of-size-2 is created, it never changes.

x = (19,(18,(17,"e")))
print( f"call remove on x: {removeAll(17,x)}" )
print( f"but x is still: {x}" )
x2 = removeAll(17,x)

# This is how R works:
# if you call 'transpose', you get back a *new* matrix; the original data is untouched.

# very different from:
y = [19,18,17]
print( f"y before removal is {y}" )
print( f"result of calling `remove` is: {y.remove(17)}" )
print( f"y after removal is {y}" )

# Why the two approaches?  Is mutable better/worse than immutable?
#  - immutable data is easier to reason about
#     (you won't have a variable change its value somewhere far away in your code)
#  - mutable data can be more space-efficient -- don't keep around the original
#    *and* the function-result

#But consider the memory-use here:
xAndMore = Cons(99,x)
# where I want to keep the list x, AND the list xAndMore, and be able to work with them independently.

# Memory diagram: how much more memory does this take?  Only *one* add'l tuple (2words),
# because x and xAndMore are able to share their tail.
# (BUT if we call functions on `x`, `xAndMore` won't suddently change on us -- our code will
#  use new memory/space if necessary.)
#
# But in Python, if `y` and `yAndMore` both involved the same list ("aliasing"),
#  then mutably modifying `y` will also (accidentally??) modify `yAndMore`.




# Draw pictures (memory-diagrams)
# - mutable vs immutable
# - run-time for contains
# - singly- vs doubly-linked lists, w/ and w/o mutation


def insert( itm, sordid ):
    """insert : number, SList<Comparable> -> SList<Comparable>
     Given an already-sorted SList `sordid`, return that same list 
     but with `itm` inserted so that result is still sorted.
     """
    if (isEmpty(sordid)):
        return (itm,"e")
    else:
        if itm <= first(sordid):
            return (itm, sordid)
        else:
            return (first(sordid), 
                    insert(itm, rest(sordid)))
 
assert insert( 9, 'e') == (9,'e')

assert insert( 9, (1,'e')     ) == (1,(9,'e'))
assert insert( 9, (31,'e')     ) == (9,(31,'e'))

assert insert( 9, (5,(31,'e')) )     == (5,(9,(31,'e')))
assert insert( 9, (2,(5,(22,(31,'e')))) )     == (2,(5,(9,(22,(31,'e')))))

# running time of `insert`: O(n)   (Ω(1))
#   best  case: Θ(1)
#   avg   case: Θ(n)
#   worst case: Θ(n)


def insertSort( aLst ):
   """insertSort : SList -> SList
   Return a new list of numbers, with items of `aLst` sorted by `<=`.
   """
    if (isEmpty(aLst)):
        return "e"
    else:
        return insert( first(aLst),   insertSort(rest(aLst)) )
                   
# running time of `insertSort`, worst case:
#   worst case: Θ(n²) = (n + worstCase(n-1)) = (n + [n-1 + worstCase(n-2)]) + ... ~ 1/2 n² ∈ Θ(n²)
#   best  case: Θ(n)
#   avg   case: Θ(n²)

assert insertSort( "e" ) == "e"
assert insertSort( (9,"e") ) == (9,'e')

assert insertSort( (17, (9,"e")) ) == (9,(17,'e'))
assert insertSort( (7, (9,"e")) ) == (7,(9,'e'))

assert insertSort( (8, (17, (9,"e"))) ) == (8,(9,(17,'e')))
assert insertSort( (11, (17, (9,"e"))) ) == (9,(11,(17,'e')))
assert insertSort( (38, (17, (9,"e"))) ) == (9,(17,(38,'e')))



#  quickSort : SList -> SList
#
def quickSort( nums ):
   """quickSort : SList -> SList
   Return a new list of numbers, with items of `aLst` sorted by `<=`.
   """
   if len(nums)==0:
       return []
   else:
       pivot = nums[ 0 ]
       return   quicksort( filterBiggerThan(nums, pivot) )  \
              +            filterEqualTo(   nums, pivot)    \
              + quicksort( filterLessThan(  nums, pivot ) )

# using "filterBiggerThan" etc   is NOT in-place, but this
# does convey the essence of quicksort.
# Tony Hoare (inventor quicksort, early 1960s?) instead used
# "partitioning" so that an ARRAY implementation can be done in-place.
# Doing so nets us a factor of two improvement
# (at the cost of obscuring the straightforward kernel of how quicksort works).

def filterBiggerThan( nums, threshold ):
   """filterBiggerThan : SList<Comparable>, Comparable -> SList<Comparable>
   Return all the elements of `nums` that are > than `itm`.
   """
   if isEmpty(nums):
      pass
   else:
      pass # first(nums) filterBiggerThan(rest(nums), threshold)

assert filterBiggerThan( "e", 17 ) == "e"
assert filterBiggerThan( (9,"e"), 17 ) == "e"
assert filterBiggerThan( (99,"e"), 17 ) == (99,"e")
assert filterBiggerThan( (5,(99,"e")), 17 ) == (99,"e")
assert filterBiggerThan( (99,(5,"e")), 17 ) == (99,"e")
assert filterBiggerThan( (99,(95,"e")), 17 ) == (99,(95,"e"))
assert filterBiggerThan( ( 9,( 5,"e")), 17 ) == "e"
assert filterBiggerThan( (99,(17,(95,"e"))), 17 ) == (99,(95,"e"))



def myFilter( lst, keepIt ):
   """
   Return all the elements of `lst` that satisfy `keepIt`.
   """
   return 'e'

assert myFilter( ( 9,( 5,"e")), lambda x: x>17 ) == "e"
assert myFilter( ( 9,( 5,"e")), lambda x: x<17 ) == (9,(5,"e"))
assert myFilter( ( 9,( 5,"e")), lambda x: x<=5 ) == (5,"e")
assert myFilter( ( 5,( 9,"e")), lambda x: x<=5 ) == (5,"e")

assert quickSort( "e" ) == "e"
assert quickSort( (9,"e") ) == (9,'e')

assert quickSort( (17, (9,"e")) ) == (9,(17,'e'))
assert quickSort( (7, (9,"e")) ) == (7,(9,'e'))

assert quickSort( (8, (17, (9,"e"))) ) == (8,(9,(17,'e')))
assert quickSort( (11, (17, (9,"e"))) ) == (9,(11,(17,'e')))
assert quickSort( (38, (17, (9,"e"))) ) == (9,(17,(38,'e')))



# SList -> SList
# return an SList which is sorted (and contains the elements of `nums`)
#
def mergesort( nums ):
    n = length(nums)
    if (n==0 or n==1):
         return nums
    else:
        firstHalf =    take(nums, n//2)
        secondHalf =   drop(nums, n//2)
        return merge( mergesort(firstHalf),
                      mergesort(secondHalf) )



#   pre-condition: s,t already sorted
#   we return a sorted list w/ all the element of s,t.
#
def merge( s, t ):
   pass
   # TODO

## NOTE: the work to merge two lists that had a total of n elements is Θ(n).



assert mergeSort( "e" ) == "e"
assert mergeSort( (9,"e") ) == (9,'e')

assert mergeSort( (17, (9,"e")) ) == (9,(17,'e'))
assert mergeSort( (7, (9,"e")) ) == (7,(9,'e'))

assert mergeSort( (8, (17, (9,"e"))) ) == (8,(9,(17,'e')))
assert mergeSort( (11, (17, (9,"e"))) ) == (9,(11,(17,'e')))
assert mergeSort( (38, (17, (9,"e"))) ) == (9,(17,(38,'e')))

