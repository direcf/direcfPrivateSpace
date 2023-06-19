import java.util.*; 


public class Main {
    
    public static int N;
    public static int[][] arr;
    public static boolean[] selected;
    public static int minGap;
    public static int total; 
    
    
    public void DFS(int curr, int cnt){
        
        if(curr == N+1){
            return;
        }    
        
        
        if(cnt == (N/2)){
             
            ArrayList<Integer> selectedArr = new ArrayList<>();
            ArrayList<Integer> notSelectedArr = new ArrayList<>();
            int sum = 0;
            int left = 0; 
            
            for(int i=1; i<=N; i++){
                if(selected[i] == true){
                    selectedArr.add(i); 
                }else{
                    notSelectedArr.add(i);
                }
            }
            
            
            for(int i=0; i<selectedArr.size(); i++){
                for(int j=0; j<selectedArr.size(); j++){
                    if(i != j){
                        sum += arr[selectedArr.get(i)][selectedArr.get(j)];
                    }
                }
            }
            
            for(int i=0; i<notSelectedArr.size(); i++){
                for(int j=0; j<notSelectedArr.size(); j++){
                    if(i != j){
                        left += arr[notSelectedArr.get(i)][notSelectedArr.get(j)];
                    }
                }
            }
            
            
            minGap = Math.min(minGap, Math.abs(left-sum));

            
            return; 
            
        }
        
    
        
        
        selected[curr] = true;
        DFS(curr+1, cnt+1);
        selected[curr] = false;
        DFS(curr+1, cnt);
        
        
    }
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt(); 
      minGap = Integer.MAX_VALUE;
      
      arr = new int[N+10][N+10];
      selected = new boolean[N+10];
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              int num = sc.nextInt();
              arr[i][j] = num; 
          }
      }
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              if(i!=j){
                  total += arr[i][j];
              }
          }
      }
      
      
      T.DFS(1, 0);
      
      
      System.out.println(minGap);
      
      
      
      
      
    }
}
