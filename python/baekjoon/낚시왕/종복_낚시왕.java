import java.util.*;


// 상어의 정보를 클래스로 관리합니다. 
class Shark{
    
    int r;
    int c;
    int s;
    int d;
    int z;
    boolean isDead;
    
    public Shark(int r, int c, int s, int d, int z, boolean isDead){
        this.r = r;
        this.c = c;
        this.s = s;
        this.d = d;
        this.z = z;
        this.isDead = isDead;
    }
    
}




public class Main {
    
    public static int R;
    public static int C; 
    public static int M; 
    public static ArrayList<Shark> arr;
    public static int column;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, 1, -1}; 
    public static int[][] size;
    public static int[][] idx;
    public static int answer; 
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=R && 1<=y && y<=C){
            return true;
        }else{
            return false; 
        }
    }
    
    
    // 상어를 사냥합니다.
    // 열에 해당하는 상어 중에서 
    // 가장 행이 작은 것을 사냥합니다. 
    // 상어를 잡으면, 해당 상어는 죽었다고 처리하고, 
    // 정답에 해당 상어의 크기를 더합니다. 
    public void catchShark(int col){
        
        
        int selectedRow = 1000;
        int selectedPos = 10010;
        
        for(int i=0; i<arr.size(); i++){
            if(arr.get(i).isDead == false && arr.get(i).c == col){
                if(selectedRow > arr.get(i).r){
                    selectedRow = arr.get(i).r;
                    selectedPos = i;
                }
            }
        }
        
        if(selectedPos != 10010){
            arr.get(selectedPos).isDead = true;
            answer += arr.get(selectedPos).z;
        }
        
    }
    
    
    // 상어가 이동합니다. 
    // 이동하다 벽에 부딪치면 방향을 전환합니다. 
    // time이 s가될때까지 이동합니다. 
    public void move(int i, int x, int y, int s, int d){
        
        int nx;
        int ny;
        int time = 0; 
        
        
        while(true){
            
            if(time == s){
                break;
            }
            
            nx = x + dx[d-1];
            ny = y + dy[d-1];
            
            if(!isInside(nx,ny)){
                
                if(d == 1){
                    d = 2;
                }else if(d == 2){
                    d = 1;
                }else if(d == 3){
                    d = 4;
                }else if(d == 4){
                    d = 3;
                }
                
                nx = x + dx[d-1];
                ny = y + dy[d-1];
                
            }
            
            
            x = nx;
            y = ny;
            time++; 
            
        }
        
        
        arr.get(i).r = x;
        arr.get(i).c = y;
        arr.get(i).d = d; 
        
        
        
        
        
    }
    
    
    
    // 전체 상어의 이동을 시작하는 함수입니다. 
    public void moveShark(){
        
        
        
        for(int i=0; i<arr.size(); i++){
            Shark shark = arr.get(i);
            if(shark.isDead == true){
                continue; 
            }
            
            int x = shark.r;
            int y = shark.c;
            int s = shark.s;
            int d = shark.d;
            
            move(i, x, y, s, d);
        }
        
        
        
        
    }
    
    
    // 상어가 상어를 잡아 먹습니다.
    // 이 때, 가장 큰 상어의 사이즈를 기록하고,
    // 가장 큰 것이 아닌 상어는 모두 잡아 먹히는 것을 처리해줍니다. 
    public void eatShark(){
        
        
        size = new int[R+1][C+1];
        
        for(int i=0; i<arr.size(); i++){
            Shark shark = arr.get(i);
            if(shark.isDead == true){
                continue; 
            }
            
            int x = shark.r;
            int y = shark.c;
            int z = shark.z;
            
            if(size[x][y] < z){
                size[x][y] = z;
            }
            
        }
        
        
          
        for(int i=0; i<arr.size(); i++){
            Shark shark = arr.get(i);
            if(shark.isDead == true){
                continue; 
            }
            
            int x = shark.r;
            int y = shark.c;
            int z = shark.z;
            
            if(size[x][y] != z){
                arr.get(i).isDead = true;
            }
            
        }
        
        
        
        
        
        
    }
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      arr = new ArrayList<>(); 
      
      R = sc.nextInt();
      C = sc.nextInt(); 
      M = sc.nextInt();
      
      // 상어의 초기값을 배열에 저장합니다. 
      for(int i=1; i<=M; i++){
          int r = sc.nextInt();
          int c = sc.nextInt();
          int s = sc.nextInt();
          int d = sc.nextInt();
          int z = sc.nextInt();
          
          arr.add(new Shark(r, c, s, d, z, false));
          
      }
      
      
      column = 1; 
      
      // 열을 하나씩 이동하면서 상어를 잡고,
      // 상어가 이동하고,
      // 특정 지점에서 가장 큰 상어가 나머지 상어들을 잡아 먹는 것을 반복합니다. 
      while(true){
          
          if(column == C+1){
              break; 
          }
          
          T.catchShark(column);
         
          
          T.moveShark(); 
          
          
          T.eatShark(); 
          
         
          column++;
          
          
      }
      
      
      System.out.println(answer); 
      
      
      
      
      
      
    }
}
