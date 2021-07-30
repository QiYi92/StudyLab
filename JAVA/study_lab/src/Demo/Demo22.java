package Demo;

public class Demo22 {
    static int N = 1000010;
    static boolean st[] = new boolean[N];
    public static void main(String[] args) {
        for (int i = 2; i < 100; i++) {
            if(!st[i]){
                System.out.println(i);
                for(int j = i;j <= 100;j += i){
                    st[j] = true;
                }
            }
        }
    }
}
