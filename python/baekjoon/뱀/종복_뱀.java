import java.util.*; 

class Pair{
    int x; 
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Info{
    
    int time;
    char direction;
    
    public Info(int time, char direction){
        this.time = time;
        this.direction = direction; 
    }
    
    
}


public class Main {
    
    public static int N;
    public static int K;
    public static int L;
    public static int direction; 
    public static int[][] map;
    
    public static ArrayList<Pair> apples;
    public static ArrayList<Pair> snake;
    public static ArrayList<Info> changeDirections;
    
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {1, 0, -1, 0};
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=N){
            return true;
        }else{
            return false; 
        }
    }
    
    public boolean touch(int x, int y){
        
        int len = snake.size();
        
        for(int i=1; i<len; i++){
            int sx = snake.get(i).x;
            int sy = snake.get(i).y;
            if(x == sx && y == sy){
                return true;
            }
        }
        
        return false; 
        
    }
    
    public boolean eatApple(int x, int y){
        
        for(int i=0; i<apples.size(); i++){
            Pair curr = apples.get(i);
            if(x == curr.x && y == curr.y){
                apples.remove(i); 
                return true;
            }
        }
        
        return false;
        
        
    }
    
    public void changeNow(char changeDirection){
        
            if(changeDirection == 'L'){
                  if(direction == 0){
                          direction = 3;
                  }else{
                          direction -= 1; 
                  }
            }else{
                  if(direction == 3){
                          direction = 0;
                  }else{
                          direction += 1; 
                  }
            }
            
            changeDirections.remove(0); 
        
    }
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      snake = new ArrayList<>();
      apples = new ArrayList<>();
      changeDirections = new ArrayList<>();
      
      N = sc.nextInt();
      K = sc.nextInt(); 
      
      map = new int[N+1][N+1];
      
      for(int i=1; i<=K; i++){
          int x = sc.nextInt();
          int y = sc.nextInt();
          apples.add(new Pair(x,y));
      }
      
      L = sc.nextInt();
      
      
      for(int i=1; i<=L; i++){
        int time = sc.nextInt();
        String str = sc.next();
        changeDirections.add(new Info(time, str.charAt(0)));
      }
     
      direction = 0;
      int time = 0; 
      
      snake.add(new Pair(1, 1));
      
      while(true){
          
          time++;
          
          Pair curr = snake.get(0);
          
          int x = curr.x;
          int y = curr.y;
          
          int nx = x + dx[direction];
          int ny = y + dy[direction];
          
          if(!T.isInside(nx, ny)){
              break;
          }
          
          if(T.touch(nx, ny)){
              break;
          }
          
          
          if(T.eatApple(nx, ny)){
              snake.add(0, new Pair(nx, ny));
          }else{
              snake.add(0, new Pair(nx, ny));
              snake.remove(snake.size()-1);
          }
          
          if(changeDirections.size() != 0){
              Info change = changeDirections.get(0);
              if(time == change.time){
                  T.changeNow(change.direction);
              }
          }
          
      }
      
      
      System.out.println(time); 
      
      
      
    }
}
