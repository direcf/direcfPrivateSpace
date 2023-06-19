import java.util.*;

public class Main {
    
    public static int N;
    public static int M;
    public static int[][] map;
    public static boolean[][] visited; 
    public static int maxSum;
    
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=M){
            return true;
        }else{
            return false; 
        }
    }
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    
    public void DFS(int x, int y, int sum, int cnt){
        
        if(cnt == 4){
            maxSum = Math.max(maxSum, sum);
            return; 
        }
        
        
        
        for(int i=0; i<4; i++){
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!isInside(nx, ny)){
                continue;
            }
            
            
            if(visited[nx][ny] == false){
                
                  
                if(cnt == 2){
                    visited[nx][ny] = true;
                    DFS(x, y, sum+map[nx][ny], cnt+1); 
                    visited[nx][ny] = false;
                }
            
            
                visited[nx][ny] = true;
                DFS(nx, ny, sum+map[nx][ny], cnt+1);
                visited[nx][ny] = false; 
            
                
                
                
            }
            
          
            
            
        }
        
        
    }
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      M = sc.nextInt();
      maxSum = Integer.MIN_VALUE;
      
      map = new int[N+10][M+10];
      visited = new boolean[N+10][M+10];
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              map[i][j] = sc.nextInt();
          }
      }
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              visited[i][j] = true;
              T.DFS(i, j, map[i][j], 1);
              visited[i][j] = false; 
          }
      }
      
      
      System.out.println(maxSum); 
      
      
      
      
      
      
      
      
    }
}
