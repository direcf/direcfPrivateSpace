import java.util.*; 

public class Main {
    
    public static int R;
    public static int C;
    public static int T;
    public static int[][] map;
    public static int[][] tempDiffuse;
    public static int[][] tempClean;
    public static int answer; 
    
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {1, 0, -1, 0};
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=R && 1<=y && y<=C){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public void doDiffuse(int x, int y){
        
        int initNum = map[x][y];
        
        for(int i=0; i<4; i++){
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(isInside(nx,ny) && map[nx][ny] != -1){
                map[x][y] -= (initNum/5);
                tempDiffuse[nx][ny] += (initNum/5);
             }
        }
        
        
        
    }
    
    
    
    
    public void diffuse(){
        
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                if(map[i][j] != 0){
                    doDiffuse(i, j);
                }
            }
        }
        
        
        
    }
    
    
    public void plus(){
        
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                map[i][j] += tempDiffuse[i][j]; 
            }
        }
        
        
        
    }
    
    
    public void upWard(int sx, int sy, int direction){
        
        int x = sx;
        int y = sy;
        int dir = direction;
        int nx;
        int ny; 
        
        while(true){
            
            nx = x + dx[dir];
            ny = y + dy[dir];
            
            if(map[nx][ny] == -1){
                break; 
            }
            
            if(isInside(nx,ny)){
                tempClean[nx][ny] = map[x][y];
            }else{
                
                dir+=1;
                
                nx = x + dx[dir];
                ny = y + dy[dir];
                
                tempClean[nx][ny] = map[x][y];
            }
            
            
            x = nx;
            y = ny; 
            
            
        }
        
    }
    
    public void downWard(int sx, int sy, int direction){
        
        int x = sx;
        int y = sy;
        int dir = direction;
        int nx;
        int ny; 
        
        while(true){
            
            nx = x + dx[dir];
            ny = y + dy[dir];
            
            if(map[nx][ny] == -1){
                break; 
            }
            
            if(isInside(nx,ny)){
                tempClean[nx][ny] = map[x][y];
            }else{
                if(dir == 0){
                    dir = 3;
                }else{
                    dir -= 1;
                }
                
                nx = x + dx[dir];
                ny = y + dy[dir];
                
                tempClean[nx][ny] = map[x][y];
            }
            
            
            x = nx;
            y = ny; 
            
            
        }
        
    }
    
    
    public void cleanPlus(){
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                if(map[i][j] != tempClean[i][j]){
                    map[i][j] = tempClean[i][j];
                }
            }
        }
        
    }
    
    
    public void clean(){
        
        int cnt = 0; 
        tempClean = new int[R+10][C+10];
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                tempClean[i][j] = map[i][j]; 
            }
        }
        
        
        for(int i=1; i<=R; i++){
            
            if(map[i][1] == -1 && cnt == 0){
                cnt++;
                upWard(i, 2, 0);
            }else if(map[i][1] == -1 && cnt == 1){
                downWard(i, 2, 0);
                break; 
            }
        }
        
        
        
        
    }
    
    
    public void calculate(){
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                if(map[i][j] != -1){
                    answer += map[i][j]; 
                }
            }
        }
        
    }
    
    
       
    public void finalClean(){
        
        for(int i=1; i<=R; i++){
            if(map[i][1] == -1){
                map[i][2] = 0; 
            }
        }
        
    }
    
    
    
    
    
    public void diffusion(){
        
        
        int time = 0; 
        
        
        while(true){
            
            if(time== T){
                break; 
            }
            
            tempDiffuse = new int[R+10][C+10];
            
            diffuse(); 
            
            plus();
            
            clean();
            
            cleanPlus(); 
            
            finalClean(); 
            
            time++;
            
        }
        
        
        calculate(); 
        
        
        
        
        
    }
    
    
    
    
    
    
    public static void main(String args[]) {
      Main K = new Main();
      
      Scanner sc = new Scanner(System.in); 
      
      R = sc.nextInt();
      C = sc.nextInt();
      T = sc.nextInt();
      
      answer = 0; 
      
      map = new int[R+10][C+10];
      
      for(int i=1; i<=R; i++){
          for(int j=1; j<=C; j++){
              map[i][j] = sc.nextInt(); 
          }
      }
      
      
      K.diffusion();
      
      System.out.println(answer); 
      
      
    }
}
