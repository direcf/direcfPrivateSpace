import java.util.*; 

public class Main {
    
    public static int N;
    
    public static int[] P;
    public static int[] T;
    public static int maxSum; 
    
    public void DFS(int curr, int sum){
        
        if(curr+T[curr] > N+1 || curr >= N+1){
            maxSum = Math.max(maxSum, sum);
            return; 
        }
        
        DFS(curr+T[curr], sum+P[curr]);
        DFS(curr+1, sum);
        
    }
    
    
    public static void main(String args[]) {
      Main K = new Main();
      
      Scanner sc = new Scanner(System.in);
      maxSum = 0; 
      
      
      N = sc.nextInt(); 
      
      P = new int[30];
      T = new int[30];
      
      for(int i=1; i<=N; i++){
          int time = sc.nextInt();
          int price = sc.nextInt();
          
          
          T[i] = time;
          P[i] = price;
      }
      
      for(int i=1; i<=N; i++){
            K.DFS(i, 0);   
      }
      
      System.out.println(maxSum); 
      
    }
}
