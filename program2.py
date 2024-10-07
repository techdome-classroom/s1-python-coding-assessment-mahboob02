def decode_message(s: str, p: str) -> bool:
    
    m = len(s)
    p_len = len(p)
    
    
    dp = [[False] * (p_len + 1) for _ in range(m + 1)]
    
    
    dp[0][0] = True
    
    
    for j in range(1, p_len + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  
    
    
    for i in range(1, m + 1):
        for j in range(1, p_len + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
   
    return dp[m][p_len]

# Example usage:
print(decode_message("aa", "a"))   # Output: False
print(decode_message("aa", "*"))   # Output: True
print(decode_message("cb", "?a"))  # Output: False
