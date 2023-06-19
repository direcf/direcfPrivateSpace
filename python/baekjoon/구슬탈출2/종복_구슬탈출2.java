import java.util.*; 

class Ball{
    
    int x;
    int y; 
    char type; 
    
    public Ball(int x, int y, char type){
        this.x = x; 
        this.y = y;
        this.type = type; 
    }
    
}



public class Main {
    
    public static int N;
    public static int M; 
    public static char[][] map;
    public static boolean redIsInHole;
    public static boolean blueIsInHole; 
    public static int rx;
    public static int ry;
    public static int bx;
    public static int by; 
    public static Ball red;
    public static Ball blue; 
    public static int answer; 
    
    public static int[] dx = {-1, 0, 1, 0};
    public static int[] dy = {0, -1, 0, 1};
    
    
    public void move(int x, int y, char ball, int dir){
        
           
           
           int nx = x + dx[dir];
           int ny = y + dy[dir];
           
           if(map[nx][ny] == '.'){
               move(nx, ny, ball, dir);
           }else if(map[nx][ny] == 'O'){
               if(ball == 'R'){
                   redIsInHole = true;
               }else if(ball == 'B'){
                   blueIsInHole = true; 
               }
               return; 
           }else{
               
               
               if( (x != red.x || y != red.y) && ball == 'R'){
                   rx = x;
                   ry = y;
                   map[rx][ry] = 'R';
                   map[red.x][red.y] = '.';
               }else if(x == red.x && y == red.y && ball == 'R'){
                   rx = x;
                   ry = y;
               }
               
               
               
               if( (x != blue.x || y != blue.y) && ball == 'B'){
                   bx = x;
                   by = y; 
                   map[bx][by] = 'B';
                   map[blue.x][blue.y] = '.';
               }else if(x == blue.x && y == blue.y && ball == 'B'){
                   bx = x;
                   by = y; 
               }
               
               return; 
           }
        
        
        
    }
    
    
    public void print(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=M; j++){
                System.out.print(map[i][j]+ " ");
            }
            System.out.println(); 
        }
        
        
        
        
    }
    
    
    
    
    public void dfs(int dir, int cnt){
        
        
        
           if(cnt == 11){
               return; 
           }        
        
        
           if(dir == 0){
               
               for(int j=1; j<=M; j++){
                   for(int i=1; i<=N; i++){
                       if(map[i][j] == 'R' || map[i][j] == 'B'){
                           move(i, j, map[i][j], dir);
                       }
                   }
               }
               
           }else if(dir == 1){
               
               for(int i=1; i<=N; i++){
                   for(int j=1; j<=M; j++){
                       if(map[i][j] == 'R' || map[i][j] == 'B'){
                           move(i, j, map[i][j], dir);
                       }
                   }
               }
               
               
               
           }else if(dir == 2){
               
               for(int j=1; j<=M; j++){
                   for(int i=N; i>=1; i--){
                       if(map[i][j] == 'R' || map[i][j] == 'B'){
                           move(i, j, map[i][j], dir);
                       }
                   }
               }
               
               
               
           }else if(dir == 3){
               
                for(int i=N; i>=1; i--){
                   for(int j=1; j<=M; j++){
                       if(map[i][j] == 'R' || map[i][j] == 'B'){
                           move(i, j, map[i][j], dir);
                       }
                   }
               }
               
           }
           
           
           if(redIsInHole == true && blueIsInHole == false){
               answer = cnt;
               return; 
           }else if(redIsInHole == true && blueIsInHole == true){
               return; 
           }else if(redIsInHole == false && blueIsInHole == true){
               return; 
           }else if(redIsInHole == false && blueIsInHole == false){
               
             
               if( (rx == red.x) && (ry == red.y) && (bx == blue.x) && (by == blue.y)){
                   return;
               }
               
               
               red.x = rx;
               red.y = ry;
               blue.x = bx;
               blue.y = by; 
               
               
               
               
               for(int i=0; i<4; i++){
                   dfs(i, cnt+1); 
               }
               
           }
          
        
        
        
    }
    
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      answer = -1; 
      
      N = sc.nextInt();
      M = sc.nextInt();
      
      map = new char[N+10][M+10];
      
      
      for(int i=1; i<=N; i++){
          String str = sc.next(); 
          
          for(int j=1; j<=M; j++){
              map[i][j] = str.charAt(j-1);
          }
      }
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              if(map[i][j] == 'R'){
                  red = new Ball(i, j, 'R');
              }else if(map[i][j] == 'B'){
                  blue = new Ball(i, j, 'B');
              }
          }
      }
      
      
      for(int dir=0; dir<4; dir++){
          redIsInHole = false;
          blueIsInHole = false; 
          T.dfs(dir, 1); 
      }
      
      
      System.out.println(answer); 
      
      
      
      
      
      
      
      
    }
}
