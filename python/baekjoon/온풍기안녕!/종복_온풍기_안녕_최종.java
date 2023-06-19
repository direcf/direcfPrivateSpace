import java.util.*;



// 라우트를 저장하는 클래스 
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





// 벽을 저장하는 클래스 
class Wall{
    
    int x1;
    int y1;
    int x2;
    int y2;
    
    public Wall(int x1, int y1, int x2, int y2){
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2; 
    }
    
}


// Info를 저장하는 클래스 
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
    public static int chocolate; 
    public static boolean[][] check; 
    public static ArrayList<Wall> walls; 
    
    public static int[] dx ={0, -1, -1, -1, 0, 1, 1, 1};
    public static int[] dy ={1, 1, 0, -1, -1, -1, 0, 1};
    
    public static int[] dx2={-1, 1, 0, 0};
    public static int[] dy2={0, 0, -1, 1};
    
    
    // 맵의 내부인지를 검사하는 함수 
    public static boolean isInside(int x, int y){
        if(1<=x && x<=R && 1<=y && y<=C){
            return true;
        }else{
            return false; 
        }
    }
    
    
    // 벽이 있는지를 검사하는 함수 
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
    
    
    // 대각선 방향에 벽이 있는지 체크하는 함수 
    public boolean crossWallCheck(int x1, int y1, int x2, int y2, int direction, int dir){
        
        
    
        if(dir == 1){
            
            
            Route route21 = new Route(0, 0, 0, 0);;
            Route route22 = new Route(0, 0, 0, 0);;
            
            if(direction == 1){
                route21 = new Route(x1, y1, x1+dx[2], y1+dy[2]);
                route22 = new Route(x1+dx[2], y1+dy[2], x2, y2);
            }else if(direction == 3){
                route21 = new Route(x1, y1, x1+dx[0], y1+dy[0]);
                route22 = new Route(x1+dx[0], y1+dy[0], x2, y2);
            }
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            
            
            
        }else if(dir == 3){
            
            Route route11 = new Route(0, 0, 0, 0);;
            Route route12 = new Route(0, 0, 0, 0);;
            
            if(direction == 2){
                route11 = new Route(x1, y1, x1+dx[2], y1+dy[2]);
                route12 = new Route(x1+dx[2], y1+dy[2], x2, y2);
            }else if(direction == 3){
                route11 = new Route(x1, y1, x1+dx[4], y1+dy[4]);
                route12 = new Route(x1+dx[4], y1+dy[4], x2, y2);
            }
            
            
            
            
            boolean able11 = wallCheck(route11.x1, route11.y1, route11.x2, route11.y2);
            boolean able12 = wallCheck(route12.x1, route12.y1, route12.x2, route12.y2);
            
            if(able11 == false && able12 == false){
                return false; 
            }
            
     
            
            
            
        }else if(dir == 5){
            
            Route route11 = new Route(0, 0, 0, 0);;
            Route route12 = new Route(0, 0, 0, 0);;
            
            if(direction == 2){
                route11 = new Route(x1, y1, x1+dx[6], y1+dy[6]);
                route12 = new Route(x1+dx[6], y1+dy[6], x2, y2);
            }else if(direction == 4){
                route11 = new Route(x1, y1, x1+dx[4], y1+dy[4]);
                route12 = new Route(x1+dx[4], y1+dy[4], x2, y2);
            }
            
            
            boolean able11 = wallCheck(route11.x1, route11.y1, route11.x2, route11.y2);
            boolean able12 = wallCheck(route12.x1, route12.y1, route12.x2, route12.y2);
            
            if(able11 == false && able12 == false){
                return false; 
            }
    
            
            
        }else if(dir == 7){
            
            
            Route route21 = new Route(0, 0, 0, 0);
            Route route22 = new Route(0, 0, 0, 0);
            
            
            if(direction == 1){
                route21 = new Route(x1, y1, x1+dx[6], y1+dy[6]);
                route22 = new Route(x1+dx[6], y1+dy[6], x2, y2);
            }else if(direction == 4){
                route21 = new Route(x1, y1, x1+dx[0], y1+dy[0]);
                route22 = new Route(x1+dx[0], y1+dy[0], x2, y2);
            }
            
            
            
            boolean able21 = wallCheck(route21.x1, route21.y1, route21.x2, route21.y2);
            boolean able22 = wallCheck(route22.x1, route22.y1, route22.x2, route22.y2);
            
            if(able21 == false && able22 == false){
                return false; 
            }
            
            
            
            
            
            
        }
        
        
        
        
        return true; 
        
        
        
        
        
    }
    


    
    
    
    // BFS 함수 
    public void BFS(int sx, int sy, int direction){
        
        
        
        Queue<Info> q = new LinkedList<>();
        
        
        check = new boolean[R+10][C+10];
        tmpMap = new int[R+10][C+10];
        
        
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
            
            // 이걸 왜 하는가?
            // 이걸 하는 이유가 무엇인가?
            // time을 왜 더 하는가?
            // time을 더한다는 것이 무엇인가?
            // 
            if(check[x][y] == false){
                check[x][y] = true;
                tmpMap[x][y] += time; 
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
                        
                        boolean result = crossWallCheck(x, y, nx, ny, direction, dir); 
                        
                        
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
                        
                        boolean result = crossWallCheck(x, y, nx, ny, direction, dir); 
                        
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
                        
                        boolean result = crossWallCheck(x, y, nx, ny, direction, dir); 
                        
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
                        
                        boolean result = crossWallCheck(x, y, nx, ny, direction, dir); 
                        
                        if(result == false){
                            q.add(new Info(nx, ny, time-1));
                        }
                        
                    }
                    
                }
                
                
            }
            
            
            
            
            
            
            
            
            
            
            
        }
        
        
        
        
        
        
        
    }
    
    
    // 온도 조절을 함
    public void temperateCheck(int x, int y){
        
        
        
        for(int i=0; i<4; i++){
            int nx = x + dx2[i];
            int ny = y + dy2[i];
            
            if(!isInside(nx,ny)){
                continue;
            }
            
            
            
            boolean result = wallCheck(x, y, nx, ny);
            
            if(result == false){
                int a = map[x][y];
                int b = map[nx][ny];
                
                if(a > b){
                    int value = (int)((a-b)/4);
                    tmpMap[x][y] -= value;
                    tmpMap[nx][ny] += value; 
                }
            }
        }

        
        
        
    }
    
    
    public static void tmpToOrigin(){
        
        
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                map[i][j] += tmpMap[i][j]; 
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
      
      

      
      chocolate = 0; 
      
      
      
      while(true){
          
          if(chocolate == 101){
              break; 
          }
          
          
          // 온풍기가 존재한다면 
          // 온풍기를 돌림 
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  if(info[i][j] == 1 || info[i][j] == 2 || info[i][j] == 3 || info[i][j] == 4){
                      T.BFS(i, j, info[i][j]);
                      T.tmpToOrigin(); 
                  }
                  
              }
          }
          
          
          
          
          tmpMap = new int[R+10][C+10];
          
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  T.temperateCheck(i, j); 
              }
          }
          
          T.tmpToOrigin(); 
         
        
          
          
          // 온도가 1 이상인 가장 바깥쪽의 온도가 1씩 감소
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
          
          
          // 온도를 조사해야 하는 칸이면서
          // K보다 크거나 같으면 카운트를 해줌 
          for(int i=1; i<=R; i++){
              for(int j=1; j<=C; j++){
                  if(info[i][j] == 5 && map[i][j] >= K){
                      cnt++; 
                  }
              }
          }
          
          
          chocolate++; 
          
          
          // 카운트가 전체 온도를 조사해야 하는 칸의 수와 같으면
          // while문을 break함 
          if(cnt == total){
              break; 
          }
          
          
          
          
          
          
          
          
      }
      
      
      
      
      
     
      
      System.out.println(chocolate);
      
      
      
      
      
      
      
    }
}
