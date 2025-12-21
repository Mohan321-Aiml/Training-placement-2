class Solution {
    public int flipLights(int n, int p) {
        if(p==0)return 1;
        else if(p==1)return Math.min(n+1,4);
        if(p>=4){
            if(p%2==0)p=4;
            else p=3;
        }
        if(n>6)n=6;
        boolean[] visit = new boolean[1<<n];
        
        int[] sw = new int[4];
        sw[0]=(1<<n)-1;
        for(int i=2; i<(1<<n); i<<=2)sw[1] |= i;
        for(int i=1; i<(1<<n); i<<=2)sw[2] |= i;
        for(int i=1; i<(1<<n); i<<=4)sw[3] |= i;

        dfs(0, 0, p, sw, visit);
        int a=0;
        for(boolean v:visit)if(v)a++;
        return a;
    }
    private void dfs(int c, int s, int p, int[] sw, boolean[] visit){
        if(s==4){
            if(p==0)visit[c]=true;
        }else{
            int t;
            //choose current
            if(p>0){
                t=c^sw[s];
                for(int q=p-1; q>=0; q-=2)dfs(t, s+1, q, sw, visit);
            }
            //not choose
            t=c;
            for(int q=p; q>=0; q-=2)dfs(t, s+1, q, sw, visit);
        }
    }
}
