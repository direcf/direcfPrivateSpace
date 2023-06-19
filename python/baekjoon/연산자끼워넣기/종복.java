import java.util.*;

public class Main {
    
    
    public static int[] nums;
    public static int[] arr;
    public static int N;
    public static int maxResult;
    public static int minResult;
    
    
    public void DFS(int curr, int pos){
        
          if(pos == N){
              maxResult = Math.max(maxResult, curr);
              minResult = Math.min(minResult, curr);
              return; 
          }
        
        
          for(int i=0; i<4; i++){
              if(arr[i] != 0){
                  arr[i] -= 1;
                  if(i == 0){
                      curr += nums[pos];
                      DFS(curr, pos+1);
                      curr -= nums[pos];
                      
                  }else if(i == 1){
                      curr -= nums[pos];
                      DFS(curr, pos+1);
                      curr += nums[pos];
                  }else if(i == 2){
                      curr *= nums[pos];
                      DFS(curr, pos+1);
                      curr /= nums[pos];
                  }else if(i == 3){
                      curr /= nums[pos];
                      DFS(curr, pos+1);
                      curr *= nums[pos];
                  }
                  arr[i] += 1; 
                  
              }
          }
        
        
    }
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      Main T = new Main();
      
      arr = new int[10];
      nums = new int[20];
      
      maxResult = Integer.MIN_VALUE;
      minResult = Integer.MAX_VALUE; 
      
      N = sc.nextInt();
      
      for(int i=0; i<N; i++){
          int num = sc.nextInt();
          nums[i] = num;
      }
      
      for(int i=0; i<4; i++){
          int cnt = sc.nextInt();
          arr[i] = cnt;
      }
      
      T.DFS(nums[0], 1);
        
      System.out.println(maxResult);
      System.out.println(minResult);
        
        
        
    }
}
