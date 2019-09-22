class add{
    public String bigNumberPlus(String a, String b) {
    int lenA = a.length();
    int lenB = b.length();
    if(lenA > lenB) {
        b = StringUtils.leftPad(b, lenA, "0");
    } else {
        a = StringUtils.leftPad(a, lenB, "0");
    }

    int[] arrC = new int[a.length() + 1];

    for(int i = a.length()-1; i>=0; i--) {
        int ai = Integer.parseInt(a.charAt(i) + "" );
        int bi = Integer.parseInt(b.charAt(i) + "" );
        int ci = arrC[i+1];
        int t = ai + bi + ci;
        arrC[i+1] = t%10;
        arrC[i] = t/10;
    }

    StringBuffer res = new StringBuffer();
    for(int i = 0; i<arrC.length; i++) {
        if(i==0 && arrC[i]==0) continue;
        res.append(arrC[i]);
    }
    return res.toString();
}

---------------------

本文来自 likeflower950 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/likeflower950/article/details/73359175?utm_source=copy 
}












