import sys

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        pass

# def ask_username():
#     stdout.write("Username: ".encode('utf-8'))
#     raw_username = raw_input()
#     try:
#         get_user(config.temboard['users'], raw_username)
#     except HTTPError:
#         pass
#     except ConfigurationError:
#         pass
#     else:
#         stdout.write("User already exists.\n")
#         return ask_username(config)
#     try:
#         username = raw_username
#         validate_parameters({'username': username},
#                             [('username', T_USERNAME, False)])
#     except HTTPError:
#         stdout.write("Invalid username.\n")
#         return ask_username(config)
#     return username 

if __name__ == "__main__":
    #Row Number
    sys.stdout.write("Input Row Number: \n")
    Row_Number = sys.stdin.read()
    #Column Number
    sys.stdout.write("Input Row Number: ")
    Column_Number = sys.stdin.read()
    Graph = [Row_Number][Column_Number]
    #Initialize Land And Sea
    sys.stdout.write("Input Value: ")
    for i in range(0, Row_Number):
        for j in range(0, Column_Number):
            Graph[i][j] = sys.stdin.read()
    sys.stdout.write(Solution().numIslands(Graph))