import java.util.*; 


class BlockGroup implements Comparable<BlockGroup>{
    
    int x;
    int y; 
    int cnt;
    int rainbowCnt;
    int standardBlockRow;
    int standardBlockCol;
    
    public BlockGroup(int x, int y, int cnt, int rainbowCnt, int standardBlockRow, int standardBlockCol){
        this.x = x;
        this.y = y;
        this.cnt = cnt;
        this.rainbowCnt = rainbowCnt;
        this.standardBlockRow = standardBlockRow;
        this.standardBlockCol = standardBlockCol;
    }
    
    @Override
    public int compareTo(BlockGroup cmp){
        if(this.cnt > cmp.cnt){
            return -1;
        }else if(this.cnt == cmp.cnt){
            if(this.rainbowCnt > cmp.cnt){
                return -1;
            }else if(this.rainbowCnt == cmp.rainbowCnt){
                if(this.standardBlockRow > cmp.standardBlockRow){
                    return -1;
                }else if(this.standardBlockRow == cmp.standardBlockRow){
                    if(this.standardBlockCol > cmp.standardBlockCol){
                        return -1;
                    }else{
                        return 1;
                    }
                }else{
                    return 1;
                }
            }else{
                return 1;
            }
        }else{
            return 1; 
        }
        
        
    }
    
    
}



public class Main {
    
    public static int N;
    public static int M;
    public static int[][] map; 
    public static int[][] tmpMap; 
    public static int cnt;
    public static int rainbowCnt; 
    public static int standardBlockRow;
    public static int standardBlockCol; 
    
    public static ArrayList<BlockGroup> arr;
    
    
    public static int[][] visited; 
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1}; 
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=N){
            return true;
        }else{
            return false; 
        }
    }
    
    
    
    public void DFS(int x, int y, int curr){
        
        visited[x][y] = 2;
        cnt++;
        
        if(map[x][y] == 0){
            rainbowCnt++;
        }
        
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!isInside(nx, ny)){
                continue;
            }
            
            if(visited[nx][ny] == 0 && ( (map[nx][ny] == curr) || (map[nx][ny] == 6)) ){
                DFS(nx, ny, curr);
            }
            
            
        }
        
        
        
        
    }
    

    
    
    
    
    public void print(){
        
        System.out.println("출력");
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                System.out.print(visited[i][j] + " ");
            }
            System.out.println(); 
        }
        
        
        
    }
    
    public void print2(){
        
        System.out.println("출력");
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                System.out.print(map[i][j] + " ");
            }
            System.out.println(); 
        }
        
        
        
    }
    
    
    public int move(int x, int y){
        
        int i;
        
        for(i = x+1; i<=N; i++){
            if(map[i][y] == 0){
                continue;
            }else{
                break;
            }
        }
    
        return i-1;
    }
    
    
    public void moveUnclockWard(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                tmpMap[(N+1)-j][i] = map[i][j];
            }
        }
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                map[i][j] = tmpMap[i][j]; 
            }
        }
        
        
        
        
    }
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      int answer = 0; 
      
      N = sc.nextInt();
      M = sc.nextInt();
      
      map = new int[N+10][N+10];
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              map[i][j] = sc.nextInt();
          }
      }
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              if(map[i][j] == 0){
                  map[i][j] = 6; 
              }
          }
      }
      
      
      while(true){
      
      
      visited = new int[N+10][N+10];
      arr = new ArrayList<>();
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              if(1<=map[i][j] && map[i][j] <= M){
                  visited = new int[N+10][N+10];                  
                  cnt = 0;
                  rainbowCnt = 0; 
                  standardBlockRow = Integer.MAX_VALUE;
                  standardBlockCol = Integer.MAX_VALUE;
                  
                  T.DFS(i, j, map[i][j]);
                  boolean isExist = false;
                  
                  for(int k=1; k<=N; k++){
                      for(int l=1; l<=N; l++){
                          if(visited[k][l] == 2 && map[k][l] != 6){
                              standardBlockRow = k;
                              standardBlockCol = l;
                              isExist = true;
                              break;
                          }
                      }
                      if(isExist){
                          break;
                      }
                  }
                  
                  
                  if(cnt >=2){
                    arr.add(new BlockGroup(i, j, cnt, rainbowCnt, standardBlockRow, standardBlockCol));
                  }
                  // T.print(); 
                  
                  
              }
             
          }
    
      }
      
      
      if(arr.size() == 0){
          break; 
      }
      
      Collections.sort(arr);
      
      System.out.println("arr출력");
      for(int i=0; i<arr.size(); i++){
          System.out.println("arr.get(i)는?" + arr.get(i).x + " " + arr.get(i).y + " " + arr.get(i).cnt + " " + arr.get(i).rainbowCnt + " " + arr.get(i).standardBlockRow + " " + arr.get(i).standardBlockCol);
      }
      
      
      
      int selectedX = arr.get(0).x;
      int selectedY = arr.get(0).y;
      
      visited = new int[N+10][N+10];            
      T.DFS(selectedX, selectedY, map[selectedX][selectedY]);
      
      System.out.println("visited는?");
      T.print(); 
      int deletedCnt = 0; 
      
      System.out.println("before는?");
      T.print2();
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              if(visited[i][j] == 2){
                  map[i][j] = 0; 
                  deletedCnt++;
              }
          }
      }
      
      System.out.println("after는?");
      T.print2();
      
      
      answer += Math.pow(deletedCnt, 2);
      // T.print2();
      
      for(int i=N-1; i>=1 ;i--){
          for(int j=1; j<=N; j++){
              if( (1<= map[i][j] && map[i][j]<=M) || map[i][j] == 6 ){
                  int next = T.move(i, j);
                  if(map[next][j] == 0){
                    map[next][j] = map[i][j];
                    map[i][j] = 0; 
                  }
              }
          }
      }
      
    
      // T.print2();
      
      
      tmpMap = new int[N+10][N+10];
      
      T.moveUnclockWard(); 
      
      // T.print2(); 
      
      for(int i=N-1; i>=1 ;i--){
          for(int j=1; j<=N; j++){
              if(0<= map[i][j] && map[i][j]<=M || map[i][j] == 6 ){
                  int next = T.move(i, j);
                  if(map[next][j] == 0){
                    map[next][j] = map[i][j];
                    map[i][j] = 0; 
                  }
              }
          }
      }
      
      System.out.println("최종은?");
      T.print2(); 
      System.out.println("점수는?" + answer);
      
    }
    
}
}
