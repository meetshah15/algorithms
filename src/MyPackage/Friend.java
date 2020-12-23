package MyPackage;

public class Friend {
    private int[] friends;
    private int connectedFriends;

    private int root(int p) {
        while (friends[p] != p) {
            p = friends[p];
        }
        return p;
    }

    private boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    private void unionFriends(int p, int q) {
        if (!connected(p, q)) {
            int j = root(p);
            int k = root(q);
            friends[j] = k;
            connectedFriends += 1;
        }
    }
}
