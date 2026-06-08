# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }

# Example 1:

# Input: strs = ["Hello","World"]

# Output: ["Hello","World"]
# Explanation:

# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2

# List<String> decoded_strs = solution.decode(encoded_string);

# Example 2:

# Input: strs = [""]

# Output: [""]


# Brute force solution
# Adding an character between string to decode it:
 def encode(self, strs: List[str]) -> str:
        result = "#".join(strs)
        return result

 def decode(self, s: str) -> List[str]:
        result = s.split("#")
        return result


#Time complexity : O(n)
#Space complexity: O(n)


# Problem : string = [abc#def,ghij]  Encoding = abc#def#ghij
            #    decoding    = [abc,def,ghij]

Similarly if adding of ','

def encode(self, strs: List[str]) -> str:
        result = ",".join(strs)
        return result

def decode(self, s: str) -> List[str]:
        result = s.split(",")
        return result

# Problem : string  ["hello,world","pop"]  Encoding = [hello,world,pop]
#  Decoding = [hello, world, pop]

Better approach:

# ["Hello","World"]
#  Encoding : 5#Hello5#World
#  Decoding : "Hello","World"
    
    def encode(self, strs: List[str]) -> str:
          res = ""
          for s in strs:
             res += str(len(s)) + "#" + s
          return res


# Time complexity = O(n^2)
# coz first we will have to the string concatenation one by one
# dry run:
# first iteration  is :  5#hello
#second is : 5#hello + 5#world -> 5#hello#world until m 


#however using the list :

  res = []

  for s in strs:
        res.append(str(len(s)) + "#" + s)
  return "".join(res)

  # Time complexity = O(n)
  # dry run :
  # first iteration : [5#hello, 5#world] // nothing is being copied repeatedly
  # so the output : .join(res) -> 5#hello5#world

  #Space complexity = O(n)

    def decode(self, s: str) -> List[str]:
           res=[]
           i=0

           while i<len(s):
             j=i
 
             while s[j]!="#":
              j+=1
        
             length = int(s[i:j])  # returns 5

             word = s[j + 1 : j + 1 + length]
             res.append(word)
             i=length+1+j
           return res

#Time complexity : O(n)
#Space complexity: O(n)
