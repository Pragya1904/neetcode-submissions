class Solution {
public:
    int countWays(int n, vector<int>& dp)
    {
        if(n==0 || n==1)
            return 1;
        if(n==2)
            return 2;
        
        if(dp[n]!=-1)
            return dp[n];
        
        int leftSubtree=0, rightSubtree=0;
        if(n>2)
            rightSubtree=countWays(n-2,dp);
            
        leftSubtree=countWays(n-1,dp);

        return dp[n]=rightSubtree+leftSubtree;
    }
    int climbStairs(int n) {
        vector<int> dp(n+1,-1);

        return countWays(n,dp);
    }
};
