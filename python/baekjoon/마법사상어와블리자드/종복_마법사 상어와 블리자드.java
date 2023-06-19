import java.util.*; 

public class Main {
    
    public static int N;
    public static int M;
    public static int[][] map;
    public static boolean[][] empty;
    public static ArrayList<Integer> finalMarbles; 
    public static ArrayList<Integer> tmpMarbles; 
    public static ArrayList<Integer> marbles; 
    public static boolean[] explode; 
    public static int[] cnt; 
    public static int answer; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    
    public static void throwingIce(int x, int y, int dir, int cnt, int dist){
        
        if(cnt == dist){
            return; 
        }
        
        
        int nx = x + dx[dir-1];
        int ny = y + dy[dir-1];
        
        map[nx][ny] = 0;
        empty[nx][ny] = true;
        
        throwingIce(nx, ny, dir, cnt+1, dist); 
        
    }
    
    
    public static void dfs(int x, int y, int dir, int length, int lengthCnt, int stage){
        
        
          if(length == lengthCnt){
              
              if(stage == 1){
                  lengthCnt = 0;
                  stage = 2;
                  
                  if(dir == 3){
                      dir = 2;
                  }else if(dir == 2){
                      dir = 4;
                  }else if(dir == 4){
                      dir = 1;
                  }else if(dir == 1){
                      dir = 3;
                  }
              }else if(stage == 2){
                  length++;
                  lengthCnt = 0; 
                  stage = 1;
                  
                  
                  if(dir == 3){
                      dir = 2;
                  }else if(dir == 2){
                      dir = 4;
                  }else if(dir == 4){
                      dir = 1;
                  }else if(dir == 1){
                      dir = 3;
                  }
              }
              
              
          }
          
          
          int nx = x + dx[dir-1];
          int ny = y + dy[dir-1];
          
          if(map[nx][ny] != 0){
              marbles.add(map[nx][ny]);
          }
          
          if(empty[nx][ny] == false && map[nx][ny] == 0){
              return; 
          }
          
          dfs(nx, ny, dir, length, lengthCnt+1, stage);
        
    }
    
    
    
    
    
    public static void dfs2(int x, int y, int dir, int length, int lengthCnt, int stage){
        
        
          if(length == lengthCnt){
              
              if(stage == 1){
                  lengthCnt = 0;
                  stage = 2;
                  
                  if(dir == 3){
                      dir = 2;
                  }else if(dir == 2){
                      dir = 4;
                  }else if(dir == 4){
                      dir = 1;
                  }else if(dir == 1){
                      dir = 3;
                  }
              }else if(stage == 2){
                  length++;
                  lengthCnt = 0; 
                  stage = 1;
                  
                  
                  if(dir == 3){
                      dir = 2;
                  }else if(dir == 2){
                      dir = 4;
                  }else if(dir == 4){
                      dir = 1;
                  }else if(dir == 1){
                      dir = 3;
                  }
              }
              
              
          }
          
          
          int nx = x + dx[dir-1];
          int ny = y + dy[dir-1];
          
          if(map[nx][ny] != 0){
              marbles.add(map[nx][ny]);
          }
          
          if(empty[nx][ny] == false && map[nx][ny] == 0){
              return; 
          }
          
          dfs(nx, ny, dir, length, lengthCnt+1, stage);
        
    }
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main(); 
      Scanner sc = new Scanner(System.in); 
      N = sc.nextInt();
      M = sc.nextInt();
      answer = 0; 
      
      map = new int[N+10][N+10];
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              map[i][j] = sc.nextInt(); 
          }
      }
      
      
      
      for(int i=1; i<=M; i++){
          
          marbles = new ArrayList<>(); 
          empty = new boolean[N+10][N+10];
          int dir = sc.nextInt();
          int dist = sc.nextInt(); 
          
          throwingIce((N+1)/2, (N+1)/2, dir, 0, dist);
          
          dfs((N+1)/2, (N+1)/2, 3, 1, 0, 1);
          
          System.out.println("구슬은?" + marbles.size());
          
          
          
          while(true){
              
              
              int explodeCnt = 0; 
              
              
              
              explode = new boolean[marbles.size()];
              cnt = new int[10];
              
              for(int j=0; j<marbles.size(); j++){
                  
                  int num = marbles.get(j);
                  
                  if(num == 1){
                      cnt[num] += 1;
                      
                      if(cnt[2] >= 4){
                         
                           answer += 2*cnt[2];
                           explodeCnt++;
                           int len = cnt[2];
                           int pos = j-1;
                           
                           while(len!=0){
            
                               len--;
                               explode[pos--] = true; 
                           
                           }
                           
                             
                        
                           
                      }else if(cnt[3] >= 4){
                          
                           answer += 3*cnt[3];
                          explodeCnt++;
                          int len = cnt[3];
                          int pos = j-1;
                           
                          while(len!=0){
                               len--; 
                               explode[pos--] = true; 
                           
                          }
                          
                          
                          
                      }
                      
                      cnt[2] = 0;
                      cnt[3] = 0; 
                      
                      
                  }else if(num == 2){
                      cnt[num] += 1;
                      
                      if(cnt[1] >= 4){
                          
                           answer += 1*cnt[1];
                           explodeCnt++;
                           int len = cnt[1];
                           int pos = j-1;
                           
                           while(len!=0){
                               len--; 
                               explode[pos--] = true; 
                           
                           }
                           
                           
                      }else if(cnt[3] >= 4){
                          
                           answer += 3*cnt[3];
                          explodeCnt++;
                          int len = cnt[3];
                          int pos = j-1;
                           
                          while(len!=0){
                               len--; 
                               explode[pos--] = true; 
                           
                          }
                          
                          
                          
                      }
                      
                      cnt[1] = 0;
                      cnt[3] = 0; 
                  }else if(num == 3){
                      cnt[num] += 1;
                      
                      if(cnt[1] >= 4){
                          
                           answer += 1*cnt[1];
                           explodeCnt++;
                           int len = cnt[1];
                           int pos = j-1;
                           
                           while(len!=0){
                               len--; 
                               explode[pos--] = true; 
                           
                           }
                           
                           
                      }else if(cnt[2] >= 4){
                          
                           answer += 2*cnt[2];
                          explodeCnt++;
                          int len = cnt[2];
                          int pos = j-1;
                           
                          while(len!=0){
                               len--; 
                               explode[pos--] = true; 
                           
                          }
                          
                          
                          
                      }
                      
                      cnt[1] = 0;
                      cnt[2] = 0;  
                  }
                  
                  
                  
              }
              
              if(explodeCnt == 0){
                  break; 
              }
              
              tmpMarbles = new ArrayList<>();
              for(int j=0; j<marbles.size(); j++){
                  if(explode[j] == false){
                      tmpMarbles.add(marbles.get(j));
                  }
              }
              
              marbles.clear();
              System.out.println("중간 결과:");
              for(int j=0; j<tmpMarbles.size(); j++){
                  System.out.print(tmpMarbles.get(j)+ " ");
                  marbles.add(tmpMarbles.get(j)); 
              }
              System.out.println(); 
              
          }
          
          System.out.println("최종 결과:");
          for(int j=0; j<marbles.size(); j++){
              System.out.print(marbles.get(j)+ " ");
          }
          System.out.println(); 
          
          finalMarbles = new ArrayList<>(); 
          
          int num = marbles.get(0);
          int cnt = 1;
          
          for(int j=1; j<marbles.size(); j++){
              if(marbles.get(j-1) == marbles.get(j)){
                  cnt++;
              }else{
                  num = marbles.get(j);
                  finalMarbles.add(cnt);
                  finalMarbles.add(marbles.get(j-1));
                  cnt = 1; 
              }
          }
          finalMarbles.add(cnt);
          finalMarbles.add(marbles.get(marbles.size()-1));
          
           System.out.println("진짜 최종 결과:");
          for(int j=0; j<finalMarbles.size(); j++){
              System.out.print(finalMarbles.get(j)+ " ");
          }
          
      }
      
      
      
      
      
      
      
      
      
      
      
    }
}
