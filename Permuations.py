#! /usr/bin/env python

def dbg(msg):
    print(msg)
    pass
  



# What are the permutations of {a,b,c}?
# List them!
# 
# We can find a methodical method:
#  abc
#  acb
#  bac
#  bca
#  cab
#  cba
#  
# 
# 
# 
# ===== recursive method:
#     perms("0123") = [ "0" + perms("123"),
#                       "1" + perms("023"),
#                       "2" + perms("013"),
#                       "3" + perms("012") ]
#    base case: just one (or zero) elements.


   
def perms_recur(letters):
   """Given a string of elements `letters`,
      return a list-of-strings which are permutations of `letters`."""
   n = len(letters)
   if (n==0): 
      return [""]   # There is only one permutation: the empty-permutation.
   else:
      rslt = []
      for i in range(n):
         rslt += prependToEach(letters[i], perms_recur(letters[:i]+letters[i+1:]))
      return rslt 


def prependToEach( e, strs ):
   """strs is a list of strings; e is an string to prepend.
      Return a list like `strs` except that `e` prepended to each str in `strs`."""
   rslt = [ ]
   for string in strs:
       rslt += [e+string]
   return rslt
   
assert prependToEach( 'a', [""] ) == ["a"]
dbg( prependToEach( "a", ["b"] ) )
assert prependToEach( 'a', ["b"] ) == ["ab"]
assert prependToEach( 'a', ["b","c"] ) == ["ab","ac"]
assert prependToEach( 'a', ["bcd","def"] ) == ["abcd","adef"]
assert prependToEach( 'a', ["bcd","def","ghi"] ) == ["abcd","adef","aghi"]

# I wish python had an easy way to generically extend any collection:
#assert prependToEach( 'a', [[]] ) == [['a']]
#assert prependToEach(  7 , [[4]] ) == [[7,4]]
#assert prependToEach(  7 , [[4,5]] ) == [[7,4], [7,5]]
#assert prependToEach( 'a', ["b","c",[8]] ) == ["ab","ac",["a",8]]


assert perms_recur("") == [""]
assert perms_recur("a") == ["a"]
assert perms_recur("ab") == ["ab","ba"]
assert perms_recur("abc") == ["abc","acb","bac","bca","cab","cba"]


###############
# We'll use digits instead of letters, to make it "easier":
# 
# Permutations of 0123:
#    0123  
#    0132  
#    0213
#    0231
#    0312
#    0321   <-- last digits are ascending, R->L.  So we've finished all perms starting with "0".
#    1023   <-- so increment the next digit beyond the "3" (which is "0"), and sort the remaining/suffix (reset them)
#    1032   <-- ..32 is ascending; 0 is first digit to break the pattern, so increment it: 1203
#    1203
#    1230
#    1302
#    
# General rule: walk from right to left, until you see a decrease.  Increment that "digit"
#   (to the next-bigger value to its right),
#   and zero-out -- or at least, put into the smallest order, the remaining characters.
#   (When you don't see a decrease, you're done.)
#    

def firstNonAscendingFromRight( s ):
    """From the right: find first index that isn't ascending."""
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]: return i
    return None
    
assert firstNonAscendingFromRight("") == None
assert firstNonAscendingFromRight("a") == None
assert firstNonAscendingFromRight("ab") == 0
assert firstNonAscendingFromRight("abc") == 1
assert firstNonAscendingFromRight("acb") == 0
assert firstNonAscendingFromRight("cba") == None
assert firstNonAscendingFromRight("abcfed") == 2


def firstGreaterThan( letter, sortedLetterList ):
    """Index of the first element of `sortedLetterList` that exceeds `letter`.
       (Returns its length, if no such element.)
       @pre `letters` must be sorted ascending."""
    for i in range(len(sortedLetterList)):
        #dbg(f"about to compare {letter} and {sortedLetterList[i]} (@{i}).")
        if sortedLetterList[i] > letter: return i
    return len(sortedLetterList)

assert firstGreaterThan("a", sorted("abc")) == 1
assert firstGreaterThan("b", sorted("abc")) == 2
assert firstGreaterThan("c", sorted("abc")) == 3
assert firstGreaterThan("A", sorted("abc")) == 0
assert firstGreaterThan("z", sorted("abc")) == 3


def perms_next( s ):
    """Return the lexicographically-next permutation of `s` (or, None if none)."""
    i = firstNonAscendingFromRight(s)
    if i==None:
        return None
    else:
        # We want to "increment" the digit s[i], and "0 out" (well, minimize) the remaining digits.
        remaining = sorted(s[i:])   # all remaining digits; now just find s[i]'s successor.
        j = firstGreaterThan(s[i],remaining)
        return s[:i] + remaining[j] + ''.join(remaining[:j]+remaining[j+1:])


assert perms_next( "" ) == None
assert perms_next( "a" ) == None

assert perms_next( "ab" ) == "ba"
assert perms_next( "ba" ) == None

assert perms_next( "abc" ) == "acb"
assert perms_next( "acb" ) == "bac"
assert perms_next( "bac" ) == "bca"
assert perms_next( "bca" ) == "cab"
assert perms_next( "cab" ) == "cba"
assert perms_next( "cba" ) == None

assert perms_next( "abcfed" ) == "abdcef"
assert perms_next( "bcfeda" ) == "bdacef"





def perms_v2( s ):
  """Given a string of elements `letters`,
     return a list-of-strings which are all permutations of `letters`."""
  rslts = [''.join(sorted(s))]
  while (True):
      s = perms_next(s)
      if s == None: break
      rslts += [s]
  return rslts


assert perms_v2("a") == ["a"]
assert perms_v2("ab") == ["ab","ba"]
assert perms_v2("abc") == ["abc","acb","bac","bca","cab","cba"]

#print(perms_v2("abcde"))



########### as a python iterator-object (easy/built-in way)
def perms_iterator(s):
  """Given a string of elements `letters`,
     return an *iterator of* all permutations of `letters`."""
  perm = ''.join(sorted(s))
  while (perm != None):
      yield perm                # <--- keyword 'yield' magically causes this func to return a generator.
      perm = perms_next(perm)


p = perms_iterator("xyz")
dbg(f"next perm is {next(p)}")
dbg(f"next perm is {next(p)}")
dbg(f"next perm is {next(p)}")
dbg(f"next perm is {next(p)}")
dbg(f"next perm is {next(p)}")
dbg(f"next perm is {next(p)}")
# dbg(f"next perm is {next(p)}")  <-- would throw a StopIterationException, which you you could catch.

# But normally we don't call an iterator's `next` method manually; we'd use it in a for-loop:
dbg(f"On to ABCs...")
for p in perms_iterator("bac"): 
    dbg(f"next perm is {p}")


########### as a python iterator-object (underlying methods)

class Permutation:
   def __init__(self,word):
      self.w = ''.join(sorted(word))
      self.notMyFirstRodeo = False  # a "one-time" flag, to avoid greedily generating *one* more item than gets asked for.

   def __iter__(self):
      return self

   def __next__(self):
      if self.w == None: 
         return None     # If they keep on 
      else:
         if self.notMyFirstRodeo: 
            self.w = perms_next(self.w)
         self.notMyFirstRodeo = True
         return self.w

myiter = iter(Permutation("hello there"))

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))















print("all asserts passed")


