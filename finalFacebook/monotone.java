class solution{
        public boolean isMonotonic(int[] A) {
        //递增
        boolean isIncreasing=true;
        //递减
        boolean isDiminishing=true;
        //判断单调递增
        for(int i=0;i<A.length-1;i++){
            if(A[i]>A[i+1]){
                isIncreasing=false;
                break;
            }
        }
        //判断单调递减
        for(int i=0;i<A.length-1;i++){
            if(A[i]<A[i+1]){
                isDiminishing=false;
                break;
            }
        }
        return isIncreasing || isDiminishing;
    }
}