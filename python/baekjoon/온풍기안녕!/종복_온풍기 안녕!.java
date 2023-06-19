import java.util.*;


class Route{
    
    int x1;
    int y1; 
    int x2;
    int y2;
    
    public Route(int x1, int y1, int x2, int y2){
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2; 
    }

    
    
}






class Wall{
    
    int x1;
    int y1;
    int x2;
    int y2;
    
    public Wall(int x1, int y1, int x2, int y2){
        this.x1 = x1;
        this.y1 = y2;
        this.x2 = x2;
        this.y2 = y2; 
    }
    
}

class Info{
    
    int x;
    int y;
    int time; 
    
    public Info(int x, int y, int time){
        this.x = x;
        this.y = y; 
        this.time = time; 
    }
}


public class Main {
    
    public static int R;
    public static int C;
    public static int K; 
    public static int W; 
    public static int[][] map;
    public static int[][] tmpMap; 
    public static int[][] info; 
    public static boolean[][] check; 
    public static ArrayList<Wall> walls; 
    
    public static int[] dx ={0, -1, -1, -1, 0, 1, 1, 1};
    public static int[] dy ={1, 1, 0, -1, -1, -1, 0, 1};
    
    
    
    public static boolean isInside(int x, int y){
        if(1<=x && x<=R && 1<=y && y<=C){
            return true;
        }else{
            return false; 
        }
    }
    
    
    
    public boolean wallCheck(int x1, int y1, int x2, int y2){
        
        
        
          for(int i=0; i<walls.size(); i++){
              int a = walls.get(i).x1;
              int b = walls.get(i).y1;
              int c = walls.get(i).x2;
              int d = walls.get(i).y2;
              
              if( (x1 == a) && (y1 == b) && (x2 == c) && (y2 == d)){
                  return true;
              }else if( (x1 == c) && (y1 == d) && (x2 == a) && (y2 == b)){
                  return true;
              }
          }
        
        
          return false;     
        
    }
    
    
    public boolean crossWallCheck(int x1, int y1, int x2, int y2, int dir){
        
        
    
        if(dir == 1){
            
            
            Route route21 = new Route(x1, y1, x1+dx[2], y1+dy[2]);
            Route route22 = new Route(x1+dx[2], y1+dy[2], x2, y2);
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            
            
            
        }else if(dir == 3){
            
            Route route11 = new Route(x1, y1, x1+dx[2], y1+dy[2]);
            Route route12 = new Route(x1+dx[2], y1+dy[2], x2, y2);
            
            boolean able11 = wallCheck(route11.x1, route11.y1, route11.x2, route11.y2);
            boolean able12 = wallCheck(route12.x1, route12.y1, route12.x2, route12.y2);
            
            if(able11 == false && able12 == false){
                return false; 
            }
            
            /*
            Route route21 = new Route(x1, y1, x1+dx[4], y1+dy[4]);
            Route route22 = new Route(x1+dx[4], y1+dy[4], x2, y2);
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            */
            
            
            
        }else if(dir == 5){
            
            Route route11 = new Route(x1, y1, x1+dx[4], y1+dy[4]);
            Route route12 = new Route(x1+dx[4], y1+dy[4], x2, y2);
            
            boolean able11 = wallCheck(route11.x1, route11.y1, route11.x2, route11.y2);
            boolean able12 = wallCheck(route12.x1, route12.y1, route12.x2, route12.y2);
            
            if(able11 == false && able12 == false){
                return false; 
            }
            
            /*
            Route route21 = new Route(x1, y1, x1+dx[6], y1+dy[6]);
            Route route22 = new Route(x1+dx[6], y1+dy[6], x2, y2);
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            */
            
            
            
        }else if(dir == 7){
            
            
            Route route21 = new Route(x1, y1, x1+dx[0], y1+dy[0]);
            Route route22 = new Route(x1+dx[0], y1+dy[0], x2, y2);
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            
            
            
            
            
            
        }
        
        
        
        
        return true; 
        
        
        
        
        
    }
    
    
    public void print(){
        
        
        System.out.println("출력");
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                System.out.print(map[i][j]+ " ");
            }
            System.out.println();
        }
        
        
        System.out.println();
        
        
    }
    
    
    
    
    
    
    public void BFS(int sx, int sy, int direction){
        
        
        
        Queue<Info> q = new LinkedList<>();
        
        
        check = new boolean[R+10][C+10];
        
        
        if(direction == 1){
            int nx = sx;
            int ny = sy+1;
            q.add(new Info(nx, ny, 5));
        }else if(direction == 2){
            int nx = sx;
            int ny = sy-1;
            q.add(new Info(nx, ny, 5));
        }else if(direction == 3){
            int nx = sx-1;
            int ny = sy;
            q.add(new Info(nx, ny, 5));
        }else if(direction == 4){
            int nx = sx+1;
            int ny = sy;
            q.add(new Info(nx, ny, 5));
        }
        
        
        
        
        while(!q.isEmpty()){
            
            
            Info curr = q.poll();
            
            int x = curr.x;
            int y = curr.y;
            int time = curr.time; 
            if(check[x][y] == false){
                check[x][y] = true;
                map[x][y] += time; 
            }
            
            
            if(time == 0){
                break; 
            }
            
            if(direction == 1){
                
                for(int i=0; i<3; i++){
                    
                    int dir = (i+7)%8;
                    
                    int nx = x+dx[dir];
                    int ny = y+dy[dir];
                    
                    if(!isInside(nx, ny)){
                        continue; 
                    }
                    
                    if(dir == 0 || dir == 2 || dir == 4 || dir == 6){
                        
                        boolean result = wallCheck(x, y, nx, ny); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                    
                    }else{
                        
                        boolean result = crossWallCheck(x, y, nx, ny, dir); 
                        
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                    }
                    
                    
                }
                
                
                
            }else if(direction == 2){
                
                for(int i=0; i<3; i++){
                    
                    int dir = i+3;
                    
                    int nx = x+dx[dir];
                    int ny = y+dy[dir];
                    
                    if(!isInside(nx, ny)){
                        continue; 
                    }
                    
                    if(dir == 0 || dir == 2 || dir == 4 || dir == 6){
                        
                        boolean result = wallCheck(x, y, nx, ny); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                    
                    }else{
                        
                        boolean result = crossWallCheck(x, y, nx, ny, dir); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                        
                    }
                    
                    
                }
                
                
                
                
                
                
            }else if(direction == 3){
                
                for(int i=0; i<3; i++){
                    
                    int dir = i+1;
                    
                    int nx = x+dx[dir];
                    int ny = y+dy[dir];
                    
                    if(!isInside(nx, ny)){
                        continue; 
                    }
                    
                    if(dir == 0 || dir == 2 || dir == 4 || dir == 6){
                        
                        boolean result = wallCheck(x, y, nx, ny); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                    
                    }else{
                        
                        boolean result = crossWallCheck(x, y, nx, ny, dir); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                        
                    }
                    
                    
                }
                
                
            }else if(direction == 4){
                
                for(int i=0; i<3; i++){
                    
                    int dir = i+5;
                    
                    int nx = x+dx[dir];
                    int ny = y+dy[dir];
                    
                    if(!isInside(nx, ny)){
                        continue; 
                    }
                    
                    if(dir == 0 || dir == 2 || dir == 4 || dir == 6){
                        
                        boolean result = wallCheck(x, y, nx, ny); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                    
                    }else{
                        
                        boolean result = crossWallCheck(x, y, nx, ny, dir); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                        
                    }
                    
                }
                
                
            }
            
            
            
            
            
            
            
            
            
            
            
        }
        
        
        
        
        
        
        
    }
    
    
    
    public void temperateCheck(int x, int y){
        
        
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!isInside(nx,ny)){
                continue;
            }
            
            
            
            boolean result = wallCheck(x, y, nx, ny);
            
            if(result == false){
                int a = map[x][y];
                int b = map[nx][ny];
                
                if(a > b){
                    int value = (a-b)/4;
                    tmpMap[x][y] -= value;
                    tmpMap[nx][ny] += value; 
                }
            }
        }
        
        
        
        
        
        
        
        
        
    }
    
    
    
    
    
    
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      R = sc.nextInt();
      C = sc.nextInt();
      K = sc.nextInt(); 
      
      int total = 0; 
      
      map = new int[R+10][C+10];
      info = new int[R+10][C+10];
      walls = new ArrayList<>(); 
      
      for(int i=1; i<=R; i++){
          for(int j=1; j<=C; j++){
              info[i][j] = sc.nextInt();
              if(info[i][j] == 5){
                total++;    
              }
          }
      }
      
      
      
      W = sc.nextInt(); 
      
      
      for(int i=1; i<=W; i++){
          int x = sc.nextInt();
          int y = sc.nextInt();
          int t = sc.nextInt();
          
          if(t == 0){
              walls.add(new Wall(x, y, x-1, y));
          }else if(t == 1){
              walls.add(new Wall(x, y, x, y+1));
          }
          
      }
      
      
      int chocolate = 0; 
      
      
      
      while(true){
          
          if(chocolate == 101){
              break; 
          }
          
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  if(info[i][j] == 1 || info[i][j] == 2 || info[i][j] == 3 || info[i][j] == 4){
                      T.BFS(i, j, info[i][j]);
                  }
                  
              }
          }
          
          
          tmpMap = new int[R+10][C+10];
          
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  T.temperateCheck(i, j); 
              }
          }
          
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  map[i][j] += tmpMap[i][j]; 
              }
          }
          
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  if(i == 1 || i == R || j == 1 || j == C){
                      if(map[i][j] >= 1){
                          map[i][j] -= 1; 
                      }
                  }
              }
          }
          
          int cnt = 0; 
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  if(info[i][j] == 5 && map[i][j] >= K){
                      cnt++; 
                  }
              }
          }
          
          
          chocolate++; 
          
          
          T.print(); 
          
          if(cnt == total){
              break; 
          }
          
          
          
          
          
          
          
          
      }
      
      
      
      
      
      
      
      
      
      
      
      System.out.println(chocolate);
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    }
}
