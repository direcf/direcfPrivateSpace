import java.util.*; 

public class Main {
    
    public static int N; 
    public static int[][] sands;
    public static int answer; 
    
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {-1, 0, 1, 0};
    
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=N){
            return true;
        }else{
            return false; 
        }
    }
    
    public void tornado(int x, int y, int dir){
        
            int init = sands[x][y]; 
            
            
            if(dir == 0){
                int nx, ny;
                
                nx = x;
                ny = y-1;
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.55; 
                }else{
                    answer += (int)init*0.55; 
                }
                
                
                nx = x-1;
                ny = y-1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x+1;
                ny = y-1;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x-1;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                
                    
                nx = x+1;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                nx = x;
                ny = y-2;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.05; 
                }else{
                    answer += (int)init*0.05; 
                }
                
                
                       
                nx = x-2;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x+2;
                ny = y;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x-1;
                ny = y+1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                nx = x+1;
                ny = y+1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                
                
            }else if(dir == 1){
                
             
             
                int nx, 
                nx = x;
                ny = y-1;
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.55; 
                }else{
                    answer += (int)init*0.55; 
                }
                
                
                nx = x-1;
                ny = y-1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x+1;
                ny = y-1;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x-1;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                
                    
                nx = x+1;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                nx = x;
                ny = y-2;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.05; 
                }else{
                    answer += (int)init*0.05; 
                }
                
                
                       
                nx = x-2;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x+2;
                ny = y;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x-1;
                ny = y+1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                nx = x+1;
                ny = y+1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                
                
                
                
                
                
                
                
            }else if(dir == 2){
                
            }else if(dir == 3){
                
                
                int nx, ny;
                
                nx = x-1;
                ny = y;
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.55; 
                }else{
                    answer += (int)init*0.55; 
                }
                
                
                nx = x-1;
                ny = y-1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x-1;
                ny = y+1;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.1; 
                }else{
                    answer += (int)init*0.1; 
                }
                
                
                
                    
                nx = x;
                ny = y-1;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                
                    
                nx = x;
                ny = y+1;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.07; 
                }else{
                    answer += (int)init*0.07; 
                }
                
                       
                nx = x-2;
                ny = y;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.05; 
                }else{
                    answer += (int)init*0.05; 
                }
                
                
                       
                nx = x;
                ny = y-2;
                
                   
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x;
                ny = y+2;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.02; 
                }else{
                    answer += (int)init*0.02; 
                }
                
                
                nx = x+1;
                ny = y-1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                nx = x+1;
                ny = y+1;
                
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)init*0.01; 
                }else{
                    answer += (int)init*0.01; 
                }
                
                
                
                
                
                
            }
        
        
        
        
        
    }
    
    
    
    
    
    
    
    public static void DFS(int x, int y, int dir, int len, int lenCnt, int stage){
        
        if(len == lenCnt){
            dir += 1;
            dir %= 4;
            
            if(stage == 1){
                stage = 2;
                lenCnt = 0;
            }else if(stage == 2){
                stage = 1;
                len++;
                lenCnt = 0; 
            }
        }
        
        
           
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            
            if(sand[nx][ny] != 0){
                tornado(nx, ny, dir);
            }
            
            
            
            if(nx == 1 && ny == 0){
                return; 
            }
            System.out.println("nx, ny는?" + nx + " " + ny);
            DFS(nx, ny, dir, len, lenCnt+1, stage); 
        
        
        
        
    }
    
    
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      N = sc.nextInt();
      sands = new int[N+10][N+10];
      answer = 0; 
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              sands[i][j] = sc.nextInt();
          }
      }
      
      
      DFS((N+1)/2, (N+1)/2, 0, 1, 0, 1);
      
      
      
      
      
      
      
    }
}
