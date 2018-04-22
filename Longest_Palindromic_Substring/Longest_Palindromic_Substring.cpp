#include <string>
#include <iostream>
#include <locale>

using namespace std;

//General Time complexity O(n*n)
class Solution1{
public:
    string longestPalindrome (string s){
        int startIdx = 0, left = 0, right = 0, len = 0;
        for(int i = 0; i < s.size(); ++i){
            if (s[i] == s[i + 1]){
                left = i;
                right = i + 1;
                searchPalindrome(s, left, right, startIdx, len);
            }
            left = right = i;
            searchPalindrome(s, left, right, startIdx, len);
        }
        if(len == 0)
            len = s.size();
        return s.substr(startIdx, len);
    }
    
    void searchPalindrome(string s, int left, int right, int &startIdx, int &len){
        int step = 1;
        while((left - step) >= 0 && (right + step) < s.size()){
            if (s[left - step] != s[right + step])
                break;
            ++step;
        }
        int wide = right - left + 2 * step - 1;
        if(len < wide){
            len = wide;
            startIdx = left - step + 1;
        }
    }
};

//DP
class Solution_DP{
public:
    string longestPalindrome(string s){
        int dp[s.size()][s.size()] = {0}, left = 0, right = 0, len = 0;
        for (int i = 0; i < s.size(); ++i){
            for (int j = 0; j < i; ++j){
                dp[j][i] = (s[i] == s[j] && (i - j < 2 || dp[j + 1][i - 1]));
                if(dp[j][i] && len < i - j + 1){
                    len = i - j + 1;
                    left = j;
                    right = i;
                }
            }
            dp[i][i] = 1;
        }
        return s.substr(left, right - left + 1);
    }
};

//Manacher's Algorithm
class Solution_Manacher{
public:
    string longestPalindrome(string s){
        string t = "$#";
        for(int i = 0; i < s.size(); ++i){
            t += s[i];
            t += '#';
        }
        int p[t.size()] = {0}, id = 0, mx = 0, resId = 0, resMx = 0;
        for(int i = 0; i < t.size(); ++i){
            p[i] = mx > i ? min(p[2 * id - 1], mx - i) : 1;
            while(t[i + p[i]] == t[i - p[i]]) ++p[i];
            if(mx < i + p[i]){
                mx = i + p[i];
                id = i;
            }
            if(resMx < p[i]){
                resMx = p[i];
                resId = i;
            }
        }
        return s.substr((resId - resMx) / 2, resMx - 1);
    }
};

int main()
{
    //locale::global(locale(""));
    //setlocale(LC_CTYPE, "");    // MinGW gcc.
    //wcout.imbue(locale(""));
    Solution1 *Solution = new Solution1();
    cout << "General" << endl << Solution->longestPalindrome("adhjhdf") << endl;
    Solution_DP Solution_1;
    cout << "DP" << endl << Solution_1.longestPalindrome("adhjhdf") << endl;
    Solution_Manacher Solution_2;
    cout << "Manacher" << endl << Solution_2.longestPalindrome("adhjhdf") << endl;
}



