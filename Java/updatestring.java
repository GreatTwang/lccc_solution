//用了两次遍历，第一次把---改成字母，第二次把连续的字母变成加号
class updatestring{
    static String method(String s) {
    char[] cs = s.toCharArray();
    for (int i= 0; i < cs.length; i++) {
      if (cs[i] == '-') {
        int start = i;
        int j = i;
        while (j < cs.length && cs[j] == '-') {
          j++;
        }
        if (j < cs.length && start-1 >= 0 && cs[start-1] == cs[j]) {
          change(cs, i, j-1, cs[j]);
        }
        i = j;
      }
    }
    int index = 0;
    
    while (cs[index] =='-') {
      index++;
    }
    if (index >= cs.length) {
      return new String(cs);
    }
    char c = cs[index];
    int cnt = 1;
    for (int i = index+1; i < cs.length; i++) {

      if (cs[i] == c) {
        cnt++;. Waral 博客有更多文章,
        if(i == cs.length-1) {
          change(cs, i-cnt+1, i, '+');
        }
      } else {
        if(cnt>1) {
          change(cs, i-cnt, i-1, '+');
        }.1point3acres网
        
        if (cs[i] !='-') {
          c = cs[i];
          cnt = 1;
        } else {
          while (i < cs.length && cs[i] == '-') {. Waral 博客有更多文章,
            i++;
          }. 1point 3acres 论坛
          if (i < cs.length) {
            c = cs[i];. from: 1point3acres 
            cnt = 1;
          }
        }
      }. more info on 1point3acres
      
    }
    return new String(cs);
  }
  static void change(char[] cs, int s, int e, char c) {
    for (int i = s; i <= e; i++) {
      cs[i] = c;
    }
  }
 }













