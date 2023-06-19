import java.util.*; 

public class Main {
    
    public static int N; 
    public static int[][] sands;
    public static int answer; 
    
    public static int[][] dx1 = {{0, 0, -1, 1, -1, 1, -2, 2, -1, 1}, {1, 2, 1, 1, 0, 0, 0, 0, -1, -1}, {0, 0, 1, -1, 1, -1, 2, -2, 1, -1}, {-1, -2, -1, -1, 0, 0, 0, 0, 1, 1}};
    public static int[][] dy1 = {{-1, -2, -1, -1, 0, 0, 0, 0, 1, 1}, {0, 0, -1, 1, -1, 1, 2, -2, -1, 1}, {1, 2, 1, 1, 0, 0, 0, 0, -1, -1}, {0, 0, -1, 1, 1, -1, 2, -2, 1, -1}};
    public static double[][] ratio = {{0.55, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01 }, {0.55, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01}, {0.55, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01},{0.55, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01}};
    
    
    
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {-1, 0, 1, 0};
    
    
    public static boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=N){
            return true;
        }else{
            return false; 
        }
    }
    
    public static void tornado(int x, int y, int dir){
     
        
            
            for(int i=0; i<10; i++){
                int nx = x + dx1[dir][i];
                int ny = y + dy1[dir][i];
                
                if(isInside(nx, ny)){
                    sands[nx][ny] += (int)sands[x][y]*ratio[dir][i];
                }else{
                    System.out.println("answer는?" + answer);
                    System.out.println("x, y, nx, ny는?" + x + " " + y + " " +nx + " " +ny);
                    System.out.println("sands[x][y]는?" + sands[x][y]);
                    System.out.println("ratio[dir][i]는?" + ratio[dir][i]);
                    answer += (int)(sands[x][y]*ratio[dir][i]);
                }
            }
            
        
            sands[x][y] = 0; 
        
          
        
        
        
        
        
    }
    
    
    public static void print(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                System.out.print(sands[i][j] + " ");
            }
            System.out.println(); 
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
            
            if(sands[nx][ny] != 0){
                tornado(nx, ny, dir);
            }
            
            print(); 
            
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
      
      
      System.out.println(answer); 
      
      
      
      
    }
}
