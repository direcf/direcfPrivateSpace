import java.util.*; 


public class Main {
    
    public static int N;
    public static int M;
    public static int maxSum; 
    public static int[][] map;
    public static boolean[][] visited; 
    
    
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {1, 0, -1, 0};
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=N && 1<=y && y<=M){
            return true;
        }else{
            return false; 
        }
    }
    
    
    
    
    
    public void type1And3And4(int x, int y, int cnt, ArrayList<Integer> arr, int sum){
        
        
        
            if(cnt == 3){
                
                StringBuilder sb = new StringBuilder();
                
                for(int i=0; i<arr.size(); i++){
                    sb.append(arr.get(i).toString());
                }
                
                String str = sb.toString();
                
                if(str.equals("000") || str.equals("111") || str.equals("222") || str.equals("333")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                if(str.equals("232") || str.equals("323") || str.equals("030") || str.equals("303") || str.equals("010") || str.equals("101") || str.equals("121") || str.equals("212")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                if(str.equals("011") || str.equals("001") || str.equals("100") || str.equals("110")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                if(str.equals("211") || str.equals("112") || str.equals("221") || str.equals("122")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                if(str.equals("300") || str.equals("003") || str.equals("033") || str.equals("330")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                
                if(str.equals("233") || str.equals("223") || str.equals("332") || str.equals("322")){
                    maxSum = Math.max(maxSum, sum);
                }
                
                
                
                return; 
                
            }    
                
        
            
            
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(isInside(nx,ny) && visited[nx][ny] == false){
                    visited[nx][ny] = true;
                    arr.add(i);
                    type1And3And4(nx, ny, cnt+1, arr, sum+map[nx][ny]);
                    arr.remove(arr.size()-1);
                    visited[nx][ny] = false;
                    
                }
            }
        
        
        
        
    }
    
    
    public void type2(int x, int y){
        
        int sum = 0;
        
        
        if(isInside(x+1,y) && isInside(x, y+1) && isInside(x+1, y+1)){
            sum = map[x][y] + map[x+1][y] + map[x][y+1] + map[x+1][y+1];
        }
        
        
        maxSum = Math.max(maxSum, sum);
        
        
    }
    
    
    public void type5(int x, int y){
        
        int sum1 = 0;
        int sum2 = 0;
        int sum3 = 0;
        int sum4 = 0;
        
        
        if(isInside(x+1,y) && isInside(x, y+1) && isInside(x-1, y)){
            sum1 = map[x][y] + map[x+1][y] + map[x][y+1] + map[x-1][y];
        }
        
        if(isInside(x+1,y) && isInside(x, y+1) && isInside(x, y-1)){
            sum2 = map[x][y] + map[x+1][y] + map[x][y+1] + map[x][y-1];
        }
        
        
        if(isInside(x+1,y) && isInside(x, y-1) && isInside(x-1, y)){
            sum3 = map[x][y] + map[x+1][y] + map[x][y-1] + map[x-1][y];
        }
        
        
        if(isInside(x,y+1) && isInside(x, y-1) && isInside(x-1, y)){
            sum4 = map[x][y] + map[x][y+1] + map[x][y-1] + map[x-1][y];
        }
        
        
        
        
        
        
        maxSum = Math.max(maxSum, sum1);
        maxSum = Math.max(maxSum, sum2);
        maxSum = Math.max(maxSum, sum3);
        maxSum = Math.max(maxSum, sum4);
        
    }
    
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      
      N = sc.nextInt();
      M = sc.nextInt();
      
      map = new int[N+10][M+10];
      visited = new boolean[N+10][M+10];
      
      maxSum = Integer.MIN_VALUE; 
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              map[i][j] = sc.nextInt();
          }
      }
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=M; j++){
              
              ArrayList<Integer> arr1 = new ArrayList<>();
              T.type1And3And4(i,j, 0, arr1, map[i][j]);
              T.type2(i,j);
              T.type5(i,j); 
              
              
          }
      }
      
      
      System.out.println(maxSum);
      
      
      
      
    }
}
