class Solution {
    public String reverseWords(String s) {
        String[] set = s.trim().split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i=set.length-1;i>=0;i--){
        sb.append(set[i].trim());
        if(i != 0 && !set[i].equals("")) 
            sb.append(" ");
        }
        return sb.toString();
    }
}

//another solution
public String reverseWords(String s) 
    {
        if(s == null)
            return null;
        if(s.trim().isEmpty())
            return "";
        StringBuilder sb = new StringBuilder();
        String[] words = s.split(" ");
        
        for(int i = words.length-1; i>=0; i--)
        {
            if(!words[i].equals(""))
            {
                sb.append(words[i]).append(" ");
            }
        }
        return sb.toString().trim();
    }











