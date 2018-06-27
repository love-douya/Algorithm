import sys
#from collections import OrderedDict

class Solution:
    def pop(self, Common_Prefix, pop_number):
        Number = 0
        while Number != pop_number:
            Common_Prefix.pop()
            Number += 1

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        Common_Prefix = []
        #length_of_Set = 0
        String_Num = len(strs)
        try:
            String_Len = min([len(strs[i]) for i in range(String_Num)])
        except Exception as e:
            return ""
        else:
            for i in range(0, String_Len):
                for j in range(0, String_Num):
                    Common_Prefix.append(strs[j][i])
                    print(Common_Prefix[-1:-(String_Len + 1):-1])
                if len(set(Common_Prefix[-1:-(String_Len + 1):-1])) == 1:
                    #length_of_Set = len(set(Common_Prefix))
                    self.pop(Common_Prefix, String_Num - 1)
                    print(Common_Prefix)
                else:
                    self.pop(Common_Prefix, String_Num)
                    print(Common_Prefix)
                    break
            #return "".join(list(OrderedDict.fromkeys(Common_Prefix)))
            return "".join(Common_Prefix)
    
if __name__ == "__main__":
    #sys.stdout.write("Input String Number: \n")
    #String_Num = sys.stdin.read()
    sys.stdout.write("Input Strings List: \n")
    #array = [[0 for i in range(100)] for j in range(100)]
    array = []
    #count = 0
    #sys.stdin.flush()
    string = sys.stdin
    for lines in string:
        array.append(list(lines.strip()))
        #string = sys.stdin.readline()
        #sys.stdout.writelines(str(array[count]))
        #count += 1
    sys.stdout.writelines("Longest Prefix is: \n" + str(Solution().longestCommonPrefix(array)))