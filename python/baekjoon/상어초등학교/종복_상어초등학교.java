import java.util.*; 


class Pair implements Comparable<Pair>{
    
    int x;
    int y;
    int empty;
    
    public Pair(int x, int y, int empty){
        this.x = x;
        this.y = y;
        this.empty = empty; 
    }
    
    @Override
    public int compareTo(Pair p){
        if(this.x == p.x){
            return this.y - p.y;
        }
        
        return this.x-p.x; 
    }
    
}


public class Main {
    
    public static int N;
    public static int[][] map;
    public static ArrayList<Integer> order;
    public static int[][] likeCnt;
    public static int[][] likes; 
    public static ArrayList<Pair> first; 
    public static ArrayList<Pair> second; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1}; 
    
    public boolean isInside(int x, int y){
        if(0<=x && x<N && 0<=y && y<N){
            return true;
        }else{
            return false; 
        }
    }
    
    
    
    
    public int getLikeFriends(int x, int y, int studentNum){
        
        
            int cnt = 0; 
            int a = likes[studentNum][0];
            int b = likes[studentNum][1];
            int c = likes[studentNum][2];
            int d = likes[studentNum][3];
            
            
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(isInside(nx,ny) && (map[nx][ny] == a || map[nx][ny] == b || map[nx][ny] == c || map[nx][ny] == d)){
                    cnt++;
                }
            }
        
        
            return cnt;         
        
    }
    
    
    
    
    
    public void firstCheck(int studentNum){
        
          likeCnt = new int[N+10][N+10];
          int maxCnt = Integer.MIN_VALUE;
          
          
          for(int i=0; i<N; i++){
              for(int j=0; j<N; j++){
                  if(map[i][j] != 0){
                      continue; 
                  }
                  int cnt = getLikeFriends(i,j, studentNum);
                  likeCnt[i][j] = cnt;
                  maxCnt = Math.max(maxCnt, cnt); 
              }
          }
          
          for(int i=0; i<N; i++){
              for(int j=0; j<N; j++){
                  if(maxCnt == likeCnt[i][j]){
                      first.add(new Pair(i,j,0));
                  }
              }
          }
          
        
    }
    
    
    
    public int getEmpty(int x, int y){
        
        int cnt = 0; 
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(isInside(nx,ny) && map[nx][ny] == 0){
                cnt++;
            }
        }
        
        return cnt; 
        
    }
    
    
    public void secondCheck(int studentNum){
        
        int maxCnt = Integer.MIN_VALUE; 
        
        for(int i=0; i<first.size(); i++){
            
            Pair curr = first.get(i);
            
            int cnt = getEmpty(curr.x, curr.y);
            
            first.get(i).empty = cnt; 
            
            maxCnt = Math.max(maxCnt, cnt);
        }
        
        
        for(int i=0; i<first.size(); i++){
            
            Pair curr = first.get(i);
            
            if(curr.empty == maxCnt){
                second.add(curr); 
            }
            
            
        }
    
        
    }
    
    
    public void thirdCheck(){
        
        
        Collections.sort(second);
        
        
        
    }
    
    public int getPoint(int x, int y, int studentNum){
        
        int cnt = 0; 
        
        int a = likes[studentNum][0];
        int b = likes[studentNum][1];
        int c = likes[studentNum][2];
        int d = likes[studentNum][3];
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(isInside(nx, ny) && ((map[nx][ny] == a) || (map[nx][ny] == b) || (map[nx][ny] == c) || (map[nx][ny] == d))){
                cnt++; 
            }
        }
        
        return cnt; 
        
        
    }
    
    
    public int getPoints(){
        
        int total = 0; 
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                int studentNum = map[i][j];
                
                int cnt = getPoint(i,j, studentNum); 
                
                if(cnt == 1){
                    total += 1;
                }else if(cnt == 2){
                    total += 10;
                }else if(cnt == 3){
                    total += 100;
                }else if(cnt == 4){
                    total += 1000; 
                }
                
            }
        }
        
        
        return total;  
    }
  
    
    public static void main(String args[]) {
      Main T = new Main();
      
      int answer = 0; 
      
      Scanner sc = new Scanner(System.in); 
      
      N = sc.nextInt();
      
      map = new int[N+10][N+10];
      order = new ArrayList<>(); 
      
      likes = new int[30][10];
      
      for(int i=1; i<=N*N; i++){
        int num = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        
        likes[num][0] = a;
        likes[num][1] = b;
        likes[num][2] = c;
        likes[num][3] = d;
        
        order.add(num);
      }
      
      
      for(int i=1; i<=N*N; i++){
          
          int studentNum = order.get(i-1);
          
          first = new ArrayList<>(); 
          
          T.firstCheck(studentNum);
          
       
          if(first.size() == 1){
              int x = first.get(0).x;
              int y = first.get(0).y;
              
              map[x][y] = studentNum;
              continue;
          }
          
          second = new ArrayList<>(); 
          
          T.secondCheck(studentNum);
          
        
          if(second.size() == 1){
              int x = second.get(0).x;
              int y = second.get(0).y;
              
              map[x][y] = studentNum; 
              continue;
          }
          
          T.thirdCheck();
          
          if(second.size() == 1){
              int x  = second.get(0).x;
              int y  = second.get(0).y;
              map[x][y] = studentNum;
              continue;
          }
         
      }
      
      
      answer = T.getPoints(); 
          
      
      System.out.println(answer); 
      
      
      
      
      
      
      
      
    }
}
