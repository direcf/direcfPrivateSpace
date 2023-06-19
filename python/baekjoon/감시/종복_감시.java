import java.util.*; 

class CCTV{
    
    int x;
    int y;
    int type;
    int dir;
    
    public CCTV(int x, int y, int type){
        this.x = x;
        this.y = y;
        this.type = type; 
    }
    
}


public class Main {
    
    public static int N;
    public static int M;
    public static int[][] map;
    public static int[][] calculateMap;
    public static ArrayList<CCTV> arr; 
    public static int total; 
    
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {1, 0, -1, 0};
    public static int minCnt; 
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=M){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public void change(int x, int y, int dir){
        
        
        int nx;
        int ny;
        
        while(true){
            
            nx = x + dx[dir];
            ny = y + dy[dir];
            
            if(isInside(nx,ny) && calculateMap[nx][ny] != 6){
               if(calculateMap[nx][ny] == 1 || calculateMap[nx][ny] == 2 || calculateMap[nx][ny] == 3 || calculateMap[nx][ny] == 4 || calculateMap[nx][ny] == 5){
               }else{
                   calculateMap[nx][ny] = 100; 
               }
            }else{
                break; 
            }
            
            x = nx;
            y = ny;
            
            
        }
        
          
        
        
        
        
        
    }

    
    
    public int calculate(){
        
        int cnt = 0; 
        
        calculateMap = new int[N+1][M+1];
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=M; j++){
                calculateMap[i][j] = map[i][j];
            }
        }
        
        
        
        for(int i=0; i<total; i++){
            
            int x = arr.get(i).x;
            int y = arr.get(i).y;
            int type = arr.get(i).type;
            int dir = arr.get(i).dir;
            
            if(type == 1){
                
                if(dir == 0){
                    change(x, y, 0);
                }else if(dir == 1){
                    
                    change(x, y, 1);
                }else if(dir == 2){
                    
                    change(x, y, 2);
                }else if(dir == 3){
                    
                    change(x, y, 3);
                }
                
                
            }else if(type == 2){
                
                 
                if(dir == 0){
                    change(x, y, 0);
                    change(x, y, 2);
                }else if(dir == 1){
                    change(x, y, 1);
                    change(x, y, 3);
                }
                
            }else if(type == 3){
                
                if(dir == 0){
                    change(x, y, 0);
                    change(x, y, 1);
                }else if(dir == 1){
                    change(x, y, 1);
                    change(x, y, 2);
                }else if(dir == 2){
                    change(x, y, 2);
                    change(x, y, 3);
                }else if(dir == 3){
                    change(x, y, 3);
                    change(x, y, 0);
                }
                
                
            }else if(arr.get(i).type == 4){
                
                if(dir == 0){
                    change(x, y, 0);
                    change(x, y, 1);
                    change(x, y, 2);
                }else if(dir == 1){
                    change(x, y, 1);
                    change(x, y, 2);
                    change(x, y, 3);
                }else if(dir == 2){
                    change(x, y, 2);
                    change(x, y, 3);
                    change(x, y, 0);
                }else if(dir == 3){
                    change(x, y, 3);
                    change(x, y, 0);
                    change(x, y, 1);
                }
                
            }else if(arr.get(i).type == 5){
                if(dir == 0){
                    change(x, y, 0);
                    change(x, y, 1);
                    change(x, y, 2);
                    change(x, y, 3);
                }
            }
            
            
        }
            
        for(int i=1; i<=N; i++){
            for(int j=1; j<=M; j++){
                if(calculateMap[i][j] == 0){
                    cnt++;
                }
            }
        }
        
        return cnt; 
        
        
        
    }
    
    public void DFS(int curr){
        
        
        if(curr == total){
            int result = calculate();
            minCnt = Math.min(minCnt, result); 
            return; 
        }
        
        
        
        if(arr.get(curr).type == 1){
            for(int i=0; i<4; i++){
                arr.get(curr).dir = i;
                DFS(curr+1);
                arr.get(curr).dir = -1; 
            }
        }else if(arr.get(curr).type == 2){
            for(int i=0; i<2; i++){
                arr.get(curr).dir = i;
                DFS(curr+1);
                arr.get(curr).dir = -1; 
            }
        }else if(arr.get(curr).type == 3){
            for(int i=0; i<4; i++){
                arr.get(curr).dir = i;
                DFS(curr+1);
                arr.get(curr).dir = -1; 
            }
        }else if(arr.get(curr).type == 4){
            for(int i=0; i<4; i++){
                arr.get(curr).dir = i;
                DFS(curr+1);
                arr.get(curr).dir = -1; 
            }
        }else if(arr.get(curr).type == 5){
            arr.get(curr).dir = 0;
            DFS(curr+1);
            arr.get(curr).dir = -1; 
        }
        
        
        
        
           
        
        
    }
    
    
    
    public static void main(String args[]) {
        

      Main T = new Main();        
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      M = sc.nextInt();
      
      map = new int[N+1][M+1];
      arr = new ArrayList<>(); 
      minCnt = Integer.MAX_VALUE; 
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              map[i][j] = sc.nextInt();
          }
      }
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              if(map[i][j] != 0 && map[i][j] != 6){
                  arr.add(new CCTV(i, j, map[i][j]));
              }
          }
      }
      
      
      
      total = arr.size(); 
      
      T.DFS(0);
      
      System.out.println(minCnt); 
      
      
      
    }
}
