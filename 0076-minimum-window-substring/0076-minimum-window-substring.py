class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        t_freq={}
        for ch in t:
            t_freq[ch]=t_freq.get(ch,0)+1
        l=0
        count=len(t)
        ans=""
        for r in range(len(s)):
            ch=s[r]
            if ch in t_freq and t_freq[ch]>0:
                count-=1
            t_freq[ch]=t_freq.get(ch,0)-1
            while count==0:
                if ans=="" or r-l+1<len(ans):
                    ans=s[l:r+1]
                t_freq[s[l]]=t_freq.get(s[l],0)+1
                if t_freq[s[l]]>0:
                    count+=1
                l+=1
        return ans
                