import java.util.*; 


class Pair{
    
    int x;
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y; 
    }
}



public class Main {
    
    public static int N;
    public static int M;
    public static int[][] map;
    
    public static int maxCnt; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    
    public boolean isInside(int x, int y){
        if(0<=x && x< N && 0<=y && y<M){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public void bfs(int sx, int sy){
        
        
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(sx, sy));
        
        
        while(!q.isEmpty()){
            
            Pair curr = q.poll();
            
            int x = curr.x;
            int y = curr.y;
            
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(isInside(nx,ny) && map[nx][ny] == 0){
                    map[nx][ny] = 3;
                    q.add(new Pair(nx, ny));
                }
            }
            
            
            
        }
        
        
        
        
    }
    
    
    
    
    
    
    public void spread(){
        
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 2){
                    bfs(i, j);
                }
            }
        }
        
    }
    
    
    public int calculate(){
        
        int cnt = 0; 
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 0){
                    cnt++;      
                }
            }
        }
        
        return cnt; 
        
    }
    
    
    public void unspread(){
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 3){
                    map[i][j] = 0; 
                }
            }
        }
        
    }
    
    
    
    public void DFS(int cnt){
        
        if(cnt == 3){
            spread();
            int areaCnt = calculate();
            maxCnt = Math.max(maxCnt, areaCnt);
            unspread();
            return; 
        }
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 0){
                    map[i][j] = 1;
                    DFS(cnt+1);
                    map[i][j] = 0; 
                }
            }
        }
        
        
        
    }
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      Main T = new Main(); 
      ;
      N = sc.nextInt();
      M = sc.nextInt();
      
      map = new int[N+1][M+1];
      
      maxCnt = Integer.MIN_VALUE; 
      
      
      for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            map[i][j] = sc.nextInt();
        }   
      }
      
      
      T.DFS(0);
      
      
      System.out.println(maxCnt); 
      
    }
}
