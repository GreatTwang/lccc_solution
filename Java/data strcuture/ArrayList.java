
public class MyArrayList {
    Object[] obj = new Object[4];
    int size = 0;//集合的大小

    public int getSize() {
        return size;
    }

    //添加
    public void add(Object value) {
        //判断size是否达到数组的长度，若已经达到了，则要搬家，即搬到一个比现在数组长的新数组里面去
        if(size >= obj.length) {
            Object[] temp = new Object[obj.length*3/2+1];
            //搬家
            for(int i=0; i<obj.length; i++) {
                temp[i] = obj[i];
            }
            obj = temp;
        }
        obj[size] = value;
        size ++;
    }

    //判断下标是否合法
    public void isIndexLegal(int index) {
        if(index<0 || index>=size) { //index<0表示数组越界，index>=size超过了已放的数量，数组表示的是可放数量，我们要模拟的是已放数量
            try {
                throw new Exception("超出范围！");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    //修改下标为index的值为value
    public void set(int index, Object value) {
//        if(index<0 || index>=size) { //index<0表示数组越界，index>=size超过了已放的数量，数组表示的是可放数量，我们要模拟的是已放数量
//            try {
//                throw new Exception("超出范围！");
//            } catch (Exception e) {
//                e.printStackTrace();
//            }
//        }
        isIndexLegal(index);
        obj[index] = value;
    }

    //获取下标为index的值
    public Object get(int index) {
        isIndexLegal(index);
        return obj[index];
    }

    //清除所有
    public void clear() {
        size = 0; //用户读不到
        obj = new Object[4]; //原来的数据都会被清除掉，原来的引用没了，最终会被GC回收掉
    }

    //删除指定下标的值
    public void removeAt(int index) {
        isIndexLegal(index);
        for(int i=index+1; i<size; i++) {
            obj[i-1] = obj[i];
        }
        size --;












