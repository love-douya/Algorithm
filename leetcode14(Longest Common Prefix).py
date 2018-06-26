import sys

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        Common_Prefix = []
        length_of_tuple = 0
        for i in range(0, len(strs[0])):
            for j in range(0, len(strs)):
                Common_Prefix.append(strs[j][i])
                if len(tuple(Common_Prefix)) == (length_of_tuple + 1):
                    length_of_tuple = len(tuple(Common_Prefix))
                else:
                    break
        return tuple(Common_Prefix)
    
if __name__ == "__main__":
    sys.stdout.write("Input String Number: \n")
    String_Num = sys.stdin.read()
    sys.stdout.write("Input Strings List: \n")
    #array = [[0 for i in range(100)] for j in range(100)]
    array = [[String_Num]]
    count = 0
    sys.stdin.flush()
    string = sys.stdin
    for lines in string:
        array[count].append(lines)
        #string = sys.stdin.readline()
        sys.stdout.writelines(str(array[count]) + "\n")
        count += 1
    sys.stdout.writelines("Longest Prefix is: \n" + str(Solution().longestCommonPrefix(array)))