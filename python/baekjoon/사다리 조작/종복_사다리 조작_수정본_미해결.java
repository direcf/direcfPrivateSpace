import java.util.*; 

public class Main {
    
    
    public static int N;
    public static int M;
    public static int H;
    public static int[][] map;
    public static int minCnt; 
    public static boolean flag;
    
    
    public static boolean check(){
    
    
        
        for(int i=1; i<=N; i++){
            
            int h = 1;
            int y = i;
            
            for(int j=1; j<=H-1; j++){
                if(map[h][y] == 1){
                     y++;  
                }else if(map[h][y] == 2){
                     y--;
                }
                h++;
            }
            
            
            if(i != y){ 
                return false;
            }
        }
        
        
        return true; 
        
        
    }
    
    
    
    
    
    public static void DFS(int cnt){
        
            
        
        boolean result = check();
      
        if(result == true){
            minCnt = Math.min(minCnt, cnt);
            return; 
        }
        
        if(cnt == 3){
            return; 
        }
        
        for(int i=1; i<=H; i++){
            for(int j=1; j<=N-1; j++){
                if(map[i][j] == 0 && map[i][j+1] == 0){
                    map[i][j] = 1;
                    map[i][j+1] = 2;
                    DFS(cnt+1);
                    map[i][j] = 0;
                    map[i][j+1] = 0; 
                }
            }
        }
        
        
        
        
        
    }
    
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      M = sc.nextInt();
      H = sc.nextInt();
      
      map = new int[H+10][N+10];
      
      for(int i=1; i<=M; i++){
          int a = sc.nextInt();
          int b = sc.nextInt();
          map[a][b] = 1;
          map[a][b+1] = 2; 
      }
      
      minCnt = 987654321;
      
      
      DFS(0);
      
      
      if(minCnt == 987654321){
          minCnt = -1;
      }
      
      System.out.println(minCnt); 
      
      
      
      
      
    }
}
