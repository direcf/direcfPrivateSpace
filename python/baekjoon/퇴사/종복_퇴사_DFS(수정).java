import java.util.*; 

public class Main {
    
    public static int N;
    
    public static int[] P;
    public static int[] T;
    public static int maxSum; 
    
    public void DFS(int curr, int target, int sum){
        
        if(curr >= target){
            maxSum = Math.max(maxSum, sum);
            return; 
        }
        
        if(curr+T[curr]<=target){
           DFS(curr+T[curr], target, sum+P[curr]);   
        }else{
           DFS(curr+T[curr], target, sum);   
        }
        
        DFS(curr+1, target, sum);
        
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
      
      K.DFS(1, N+1, 0);
      
      System.out.println(maxSum); 
      
    }
}
