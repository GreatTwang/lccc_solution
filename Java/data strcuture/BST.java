// JAVA implementation of tree using array
// numbering starting from 0 to n-1.
import java.util.*;
import java.lang.*;
import java.io.*;


class Array_imp {
    static int root = 0;
    static String[] str = new String[10];

    /*create root*/
    public void Root(String key)
    {
        str[0] = key;
    }

    /*create left son of root*/
    public void set_Left(String key, int root)
    {
        int t = (root * 2) + 1;

        if(str[root] == null){
            System.out.printf("Can't set child at %d, no parent found\n",t);
        }else{
            str[t] = key;
        }
    }

    /*create right son of root*/
    public void set_Right(String key, int root)
    {
        int t = (root * 2) + 2;

        if(str[root] == null){
            System.out.printf("Can't set child at %d, no parent found\n",t);
        }else{
            str[t] = key;
        }
    }

    public void print_Tree()
    {
        for (int i = 0; i < 10; i++) {
            if (str[i] != null)
                System.out.print(str[i]);
            else
                System.out.print("-");

        }
    }
}
















