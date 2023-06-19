import java.util.*;

class Fish{
    
    int x;
    int y;
    int num;
    int dir;
    boolean isDead;
    
    public Fish(int x, int y, int num, int dir, boolean isDead){
        this.x = x;
        this.y = y;
        this.num = num; 
        this.dir = dir;
        this.isDead = isDead;
    }
    
    
    
    
}


public class Main {
    
    public static Fish[] fish;
    public static int[][] map;
    public static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    public static int answer;
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      answer = 0; 
      fish = new Fish[20];
      map = new int[4][4];
      
      for(int i=0; i<4; i++){
          for(int j=0; j<4; j++){
              int num = sc.nextInt();
              int dir = sc.nextInt()-1; 
              
              fish[num] = new Fish(i, j, num, dir, false);
              map[i][j] = num;
          }
      }
      
      
      int sx = 0;
      int sy = 0; 
      int sd = fish[map[0][0]].dir;
      int eat = map[0][0];
      fish[map[0][0]].isDead = true;
      
      dfs(sx, sy, sd, eat);
     
      System.out.println(answer); 
     
    }
    
    
    
    public static void dfs(int sx, int sy, int sd, int eat){
        
        System.out.println("eat은? " + eat); 
        answer = Math.max(answer, eat); 
        
        
        int[][] tempMap = new int[map.length][map.length];
		for(int i = 0; i < map.length; i++) {
			System.arraycopy(map[i], 0, tempMap[i], 0, map.length);
		}

		//fish 배열 복사 
		Fish[] tempFish = new Fish[fish.length];
		for(int i = 1; i <= 16; i++) 
			tempFish[i] = new Fish(fish[i].x, fish[i].y, fish[i].num, fish[i].dir, fish[i].isDead);
        
        
        
        moveFish(); 
        
        
        for(int i=1; i<=3; i++){
            int nx = sx + dx[sd]*i;
            int ny = sy + dy[sd]*i;
            
            if(0<=nx && nx<4 && 0<=ny && ny<4 && map[nx][ny] != 0){
                
                int eatFish = map[nx][ny];
                int nd = fish[eatFish].dir;
                fish[map[nx][ny]].isDead = true; 
                map[sx][sy] = 0; 
                map[nx][ny] = -1;
                
                dfs(nx, ny, nd, eat+eatFish);
                
                map[sx][sy] = -1; 
                map[nx][ny] = eatFish;
                fish[map[nx][ny]].isDead = false; 
                
                
                
                
            }
        }
        
        
        for(int j = 0; j < map.length; j++) 
			System.arraycopy(tempMap[j], 0, map[j], 0, map.length);

		for(int i=1; i<=16; i++)
			fish[i] = new Fish(tempFish[i].x, tempFish[i].y, tempFish[i].num, tempFish[i].dir, tempFish[i].isDead);
	
        
        
        
        
    }
    
    
    public static void moveFish(){
        
        
        
        for(int i=1; i<=16; i++){
            if(fish[i].isDead == true){
                continue;
            }
            
            int x = fish[i].x;
            int y = fish[i].y;
            int num = fish[i].num;
            int dir = fish[i].dir;
            
            int cnt = 0;
            
            
            while(cnt != 8){
                
                dir %= 8;
                
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                fish[i].dir = dir;
                
                if(0<=nx && nx<4 && 0<=ny && ny < 4 && map[nx][ny] != -1){
                    
                    if(map[nx][ny] == 0){
                        map[x][y] = 0; 
                        map[nx][ny] = num;
                        fish[i].x = nx;
                        fish[i].y = ny; 
                    }else if(map[nx][ny] == 1){
                        
                        int changeFishNum = map[nx][ny];
                        fish[changeFishNum].x = x;
                        fish[changeFishNum].y = y; 
                        map[x][y] = changeFishNum;
                        
                        fish[i].x = nx;
                        fish[i].y = ny;
                        map[nx][ny] = num;
                    }
                    break;
                }else{
                    dir++;
                    cnt++; 
                }
                
            }
            
            
            
        }
        
        
        
        
        
        
        
        
        
        
        
    }
    
    
    
}
