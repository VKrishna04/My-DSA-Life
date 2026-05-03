/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const MOD = 1000000007;
    let dp = new Array(target + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        let nextDp = new Array(target + 1).fill(0);
        for (let j = 1; j <= target; j++) {
            for (let face = 1; face <= k; face++) {
                if (j >= face) {
                    nextDp[j] = (nextDp[j] + dp[j - face]) % MOD;
                }
            }
        }
        dp = nextDp;
    }

    return dp[target];
};