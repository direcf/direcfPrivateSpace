import java.util.*; 


class Pair{
    
    int x;
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y; 
    }
    
    
}


public class Main {
 
       
    public static int N;
    public static int M; 
    public static ArrayList<Pair> rainCloud;
    
    public static int[][] A;
    public static boolean[][] before; 
    public static int[][] moves; 
    
    public static int[] dx = {0, -1, -1, -1, 0, 1, 1, 1};
    public static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=M){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public static void print(){
        
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                System.out.print(A[i][j]+ " ");
            }
            System.out.println(); 
        }
    }
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      int answer = 0; 

      
      N = sc.nextInt();
      M = sc.nextInt();
      
      A = new int[N+10][M+10];
      moves = new int[110][10];
      
      rainCloud = new ArrayList<>();
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              A[i][j] = sc.nextInt(); 
          }
      }
      
      
      
      for(int i=0; i<M; i++){
          moves[i][0] = sc.nextInt();
          moves[i][1] = sc.nextInt();
      }
      
      
      rainCloud.add(new Pair(N, 1));
      rainCloud.add(new Pair(N, 2));
      rainCloud.add(new Pair(N-1, 1));
      rainCloud.add(new Pair(N-1, 2));
      
      
      
      
      
      
      for(int i=0; i<M; i++){
          
          int direction = moves[i][0];
          int speed = moves[i][1];
          
          int len = rainCloud.size(); 
          
          for(int j=0; j<len; j++){
              
              System.out.println(j + "번째");
              System.out.println("이전");
              System.out.println(rainCloud.get(j).x + " " + rainCloud.get(j).y);
              rainCloud.get(j).x += (speed)*(dx[direction-1]);
              rainCloud.get(j).y += (speed)*(dy[direction-1]);
              System.out.println("이후");
              System.out.println(rainCloud.get(j).x + " " + rainCloud.get(j).y);
              
              for(int k=0; k<speed; k++){
                  rainCloud.get(j).x += dx[direction-1];
                  rainCloud.get(j).y += dy[direction-1];
                  
                  if(rainCloud.get(j).x == 0){
                      rainCloud.get(j).x = N;
                  }else if(rainCloud.get(j).x == N+1){
                      rainCloud.get(j).x = 1; 
                  }
                  
                  if(rainCloud.get(j).y == 0){
                      rainCloud.get(j).y = N;
                  }else if(rainCloud.get(j).y == N+1){
                      rainCloud.get(j).y = 1; 
                  }
              }
              
              
              
              System.out.println("교정");
              System.out.println(rainCloud.get(j).x + " " + rainCloud.get(j).y);
              
              
          }
          
          
          before = new boolean[N+10][M+10];
          
          
          for(int j=0; j<len; j++){
              
              int x = rainCloud.get(j).x;
              int y = rainCloud.get(j).y;
              System.out.println("구름 x, y 좌표" + x + " " + y);
              
              A[x][y] += 1;
              before[x][y] = true;
              
              for(int dir=1; dir<=8; dir++){
                  if(dir % 2 == 0){
                      int nx = x + dx[dir-1];
                      int ny = y + dy[dir-1];
                      
                      if(T.isInside(nx,ny) && A[nx][ny] >= 1){
                         A[x][y] += 1;   
                      }
                  }
              }
          }
          
          System.out.println("구름 사라지기 전");
          print();
          
          
          rainCloud.clear();
          
          for(int j=1; j<=N; j++){
              for(int k=1; k<=N; k++){
                  if(A[j][k] >= 2 && before[j][k] == false){
                    A[j][k] -= 2;
                    rainCloud.add(new Pair(j,k));
                  }
              }
          }
          
          System.out.println("최종");
          print(); 

      }
      
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              answer += A[i][j]; 
          }
      }
      
      
      System.out.println(answer); 
      
      
      
      
      
      
      
    }
}
