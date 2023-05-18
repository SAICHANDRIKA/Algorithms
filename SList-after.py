#! /usr/bin/env python

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
                   # the empty-list
                   # the list containing 2 (and nuttin' else)
                   # the list containing 1 and 2 (and nuttin' else)
                   # a list of length three


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
#
#      How to extract the 3rd element from a list `lst`?
#      TODO in class




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
    return (first,rest)    # just make a two-tuple

# first : Cons -> number
#
def first( sList ):
    return sList[0]

# rest : Cons -> SList
def rest( sList ):
    return sList[1]






# sum : SList -> number
# return the sum of the elements of `lst`
def sum(lst):
   if isEmpty(lst):
      return 99 # TODO in class
   else: 
      return 88 # TODO in class
    

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


# YOUR CHALLENGE for Thu.:
# - write the function `length`
def length( aLst ):
    return 99


assert length( "e" ) == 0   
assert length( (17,"e") ) == 1   
assert length( (11,(22,"e")) ) == 2  # because the input is the list containing 1,2  (two items)




# - contains

# contains : number, list-of-number -> boolean
# Return whether `target` occurs in `aLst`.
#
def contains( target, aLst ):
    return True # TODO in class


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
#    hmm, what of empty-list?     one soln: `maxHelp(lst,maxSoFar)`; "accumulator"

# - `ref`:
#assert ref( (1,(2,"e")),  0 ) == 1
#assert ref( (1,(2,"e")),  1 ) == 2
#
# Hmm, instead of recurring on list, recur on Natural Numbers.
#  Just like SList was "empty, or Cons(..,lst)", a Natural-Number is either "0, or add1(n)"



    

assert contains( 17, "e" ) == False
assert contains( 17, (5,"e") ) == False
assert contains( 17, (17,"e") ) == True
assert contains( 17, (12, (17,"e")) ) == True
assert contains( 12, (12, (17,"e")) ) == True
assert contains( 99, (12, (17,"e")) ) == False




# - removeAll
#  return a new list, with all occurrences of `target` removed.
def removeAll( target, aLst ):
    if (isEmpty(aLst)):
        return baseCaseAnswer()
    else:
        return somehowCombine( first(aLst), removeAll(target, rest(aLst) ))

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
xAndMore = (99,x)
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







def quickSort( nums ):
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


