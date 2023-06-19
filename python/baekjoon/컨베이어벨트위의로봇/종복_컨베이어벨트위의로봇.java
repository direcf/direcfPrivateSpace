import java.util.*; 


class Robot{
    
    int x;
    int y;
    
    public Robot(int x, int y){
        this.x = x;
        this.y = y; 
    }
    
}


public class Main {
    
    public static int N;
    public static int K;
    public static int[][] arr;
    public static ArrayList<Robot> robots; 
    
    
    
    
    
    
    public static boolean checkDurability(){
        int cnt = 0; 
        
        for(int i=0; i<=1; i++){
            for(int j=1; j<=N; j++){
                if(arr[i][j] == 0){
                    cnt++;
                }
            }
        }
        // System.out.println("cnt는?" + cnt);
        
        if(cnt >= K){
            return true;
        }else{
            return false; 
        }
        
    }
    /*
    public static void print(){
        
        System.out.println("출력");
        for(int i=0; i<=1; i++){
            for(int j=1; j<=N; j++){
                System.out.print(arr[i][j]+ " ");
            }
            System.out.println(); 
        }
    }
    
    public static void printRobots(){
        
        System.out.println("로봇 출력");
        for(int i=0; i<robots.size(); i++){
            System.out.print(robots.get(i).x + " " + robots.get(i).y);
        }
        System.out.println(); 
    }
    */
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      N = sc.nextInt();
      K = sc.nextInt();
      arr = new int[2][N+10];
      robots = new ArrayList<>(); 
      
      for(int i=1; i<=N; i++){
          arr[0][i] = sc.nextInt();
      }
      
      
      for(int i=N; i>=1; i--){
          arr[1][i] = sc.nextInt();
      }
      
      
      int stage = 1; 
      
      
      
      while(true){
          
          // 윗 줄 컨베이어 벨트를 이동시키는 것
          for(int i=N; i>=1; i--){
              arr[0][i+1] = arr[0][i];
          }
          
          // 아랫줄 컨베이어 벨트를 이동시키는 것
          for(int i=1; i<=N; i++){
              arr[1][i-1] = arr[1][i];
          }
          
          
          arr[0][1] = arr[1][0];
          arr[1][N] = arr[0][N+1];
          
          arr[1][0] = 0;
          arr[0][N+1] = 0;
          
          
          
          
          int deadPos = -1; 
          
          // 로봇들을 컨베이어벨트에 따라 이동시키는 것
          // 이 때, 중요한 것은 내리는 지점에 도달하면, 바로 내리게 해야 한다 
          // 이 조건을 잘 적용해야 한다 
          for(int i=0; i<robots.size(); i++){
              Robot curr = robots.get(i); 
              
              int x = curr.x;
              int y = curr.y;
              
              if(x == 0 && y == N){
                  x = 1;
                  y = N;
              }else if(x == 0 && y != N){
                  x = 0;
                  y = y+1;
              }else if(x == 1 && y == 1){
                  x = 0;
                  y = 1;
              }else if(x ==1 && y != 1){
                  x = 1; 
                  y = y-1;
              }
              
              if(x == 0 && y == N){
                  deadPos = i; 
              }
              
              robots.get(i).x = x;
              robots.get(i).y = y; 
          }
          
          // 내리는 로봇이 있다면, robots 배열에서 제거해준다. 
          if(deadPos != -1){
            robots.remove(deadPos);
          }
          
          
          deadPos = -1; 
          
          // 로봇들을 다음 칸으로 이동시킨다. 
          // 이 때는, 다음 칸에 로봇이 존재하지 않아야 한다는 조건과 내구도가 1이상이어야 한다는 조건이 중요하다.
          // 두 조건을 만족할 때만, 이동시킨다. 
          // 마찬가지로 내리는 지점에 도달한 것이 있다면 제거해준다. 
          for(int i=0; i<robots.size(); i++){
              Robot curr = robots.get(i); 
              
              int x = curr.x;
              int y = curr.y;
              int nx = 0;
              int ny = 0; 
              
              if(x == 0 && y == N){
                  nx = 1;
                  ny = N;
              }else if(x == 0 && y != N){
                  nx = 0;
                  ny = y+1;
              }else if(x == 1 && y == 1){
                  nx = 0;
                  ny = 1;
              }else if(x ==1 && y != 1){
                  nx = 1; 
                  ny = y-1;
              }
              
              boolean robotExist = false;  
              
              
              for(int j=0; j<robots.size(); j++){
                  if(i != j){
                      
                        Robot cmp = robots.get(j);
                  
                        if(cmp.x == nx && cmp.y == ny){
                            robotExist = true;
                            break;
                        }
                  }
              }
              
              
              if(robotExist == false && arr[nx][ny] >= 1){
                  arr[nx][ny] -= 1;
                  robots.get(i).x = nx;
                  robots.get(i).y = ny; 
                  if(nx == 0 && ny == N){
                      deadPos = i;
                  }
                  
              }

          }
          
          
          if(deadPos != -1){
            robots.remove(deadPos);
          }
          
          // 올리는 위치에 내구도가 1이상이면
          // 새로운 로봇을 추가하고, 내구도를 1 감소시킨다. 
          if(arr[0][1] >= 1){
              arr[0][1] -= 1;
              robots.add(new Robot(0, 1));
          }
          
          // 전체 배열의 내구도를 확인한다. 
          boolean result = checkDurability(); 
          
          // print(); 
          // printRobots(); 
          
          // 내구도가 0인 것이 K개 이상이면 while문을 탈출한다. 
          if(result){
              break;
          }
          
          stage++;
          
          
          
          
          
          
      }
      
      
      // 몇 stage까지 도달했는지 출력한다. 
      System.out.println(stage);
      
      
      
      
      
      
    }
}
