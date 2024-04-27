class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> Smap;
        unordered_map<char, int> Tmap;
        if (s.length()!=t.length())
            return false;
        for (int i=0;i<s.length();i++)
        {
            Smap[s[i]]++;
        }
        for (int i=0;i<t.length();i++)
        {
            Tmap[t[i]]++;
        }
        for (int i=0;i<t.length();i++)
        {
            if (Smap[s[i]]!=Tmap[s[i]])
                return false;
        }
        return true;

        
    }
};