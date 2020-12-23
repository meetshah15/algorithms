package MyPackage;

public class QuickFind {

    private int[] id;

    public void QuickFindUF(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    private int root(int p) {
        while (id[p] != p) p = id[p];
        return p;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int j = root(p);
        int k = root(q);
        id[j] = k;
    }

}

class mainFunctionv2 {

    public static void main(String[] args) {
        QuickFind qf  = new QuickFind();
        qf.QuickFindUF(10);
    }
}
