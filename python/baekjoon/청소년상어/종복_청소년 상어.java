import java.util.*; 

class Fish implements Comparable<Fish>{
    
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
    
    @Override
    public int compareTo(Fish cmp){
        return this.num - cmp.num;
    }
}

class Shark{
    
    int x;
    int y;
    int dir;
    
    public Shark(int x, int y, int dir){
        this.x = x;
        this.y = y;
        this.dir = dir; 
    }
}







public class Main {
    
    
    public static ArrayList<Fish> fishes; 
    public static ArrayList<Fish> sharkTargets; 
    public static ArrayList<Integer> sharkTargetsPos;
    public static Shark shark; 
    public static int[] dx = {0, -1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dy = {0, 0, -1, -1, -1, 0, 1, 1, 1};
    
    public static int answer; 
    
    public static boolean isInside(int x, int y){
        if(1<=x && x<=4 && 1<=y && y<=4){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public static void startShark(){
        
        
         for(int i=0; i<fishes.size(); i++){
             if(fishes.get(i).x == 1 && fishes.get(i).y == 1){
                 shark = new Shark(1, 1, fishes.get(i).dir);
                 fishes.get(i).isDead = true; 
                 break;
             }
         }
        
        
    }
    
    
    public static void dfs(int x, int y, int dir){
        
        
          int nx = x + dx[dir];
          int ny = y + dy[dir];
          
          if(!isInside(nx, ny)){
              return; 
          }
          
          
          for(int i=0; i<fishes.size(); i++){
              if(fishes.get(i).isDead == false){
                  if(nx == fishes.get(i).x && ny == fishes.get(i).y){
                      sharkTargets.add(fishes.get(i));
                      sharkTargetsPos.add(i);
                      break;
                  }
              }
          }
           
          dfs(nx, ny, dir);       
        
    }
    
    
    
    public static void moveShark(){
        
        
        sharkTargets = new ArrayList<>(); 
        sharkTargetsPos = new ArrayList<>();
        
        int x = shark.x;
        int y = shark.y;
        int dir = shark.dir;
        
        dfs(x, y, dir);
        
        System.out.println("상어 타겟 출력:");
        if(sharkTargets.size() != 0){
            
            System.out.println("상어 위치 및 방향" + shark.x + " " + shark.y + " " + shark.dir);
            
            for(int i=0; i<sharkTargets.size(); i++){
                
                
            System.out.println(sharkTargets.get(i).x + " " + sharkTargets.get(i).y + " " + sharkTargets.get(i).num + " " + sharkTargets.get(i).dir + " " + sharkTargets.get(i).isDead);
                
            }
        }
        
    }
    
    
    
    
    public static void moveFish(){
        
           
          for(int i=0; i<fishes.size(); i++){
              if(fishes.get(i).isDead == false){
                  
                  int x = fishes.get(i).x;
                  int y = fishes.get(i).y;
                  int num = fishes.get(i).num; 
                  int dir = fishes.get(i).dir;
                  int initDir = dir;
                  
                  while(true){
                      
                      int nx = x + dx[dir];
                      int ny = y + dy[dir];
                      
                      boolean fishExist = false;
                      
                      for(int j=0; j<fishes.size(); j++){
                          if( (i!=j) && (nx == fishes.get(j).x) && (ny == fishes.get(j).y) && fishes.get(j).isDead == false){
                              fishes.get(i).x = nx;
                              fishes.get(i).y = ny;
                              fishes.get(i).dir = dir; 
                              
                              fishes.get(j).x = x;
                              fishes.get(j).y = y;
                              fishExist = true;
                              break;
                          }
                      }
                      
                      if(fishExist == true){
                          break;
                      }
                      
                      if(isInside(nx,ny) && ((nx!=shark.x) || (ny!=shark.y))){
                          fishes.get(i).x = nx;
                          fishes.get(i).y = ny;
                          fishes.get(i).dir = dir; 
                          break; 
                      }
                      
                      dir += 1;
                      if(dir == 9){
                          dir = 1; 
                      }
                      
                      if(dir == initDir){
                          break; 
                      }
                      
                  }
                  
                  
                  
              }
              
              
              
          }
        
        
        
        
    }
    
    public static void print(){
        
        
        
        System.out.println("물고기는?");
        for(int i=0; i<fishes.size(); i++){
            System.out.println(fishes.get(i).x + " " + fishes.get(i).y + " " + fishes.get(i).num + " " + fishes.get(i).dir + " " + fishes.get(i).isDead);
        }
        
        
        
    }
    
    
    
    
    public static void stage(int sum, int cnt){
        
        
        moveFish();
        moveShark(); 
        
        print(); 
        
        
        System.out.println("sum은?" + sum);
        
        if(sharkTargets.size() == 0){
           System.out.println("sharkTarget.size()==0일 때, sum은?" + sum);
           answer = Math.max(answer, sum);
           return; 
        }else{
            
          int len = sharkTargets.size();    
          ArrayList<Fish> tmpSharkTargets = new ArrayList<>();
          ArrayList<Integer> tmpSharkTargetsPos = new ArrayList<>(); 
          
          for(int i=0; i<len; i++){
              tmpSharkTargets.add(sharkTargets.get(i));
              tmpSharkTargetsPos.add(sharkTargetsPos.get(i));
          }
          
          for(int i=0; i<tmpSharkTargets.size(); i++){
              Fish fish = tmpSharkTargets.get(i);
              int pos = tmpSharkTargetsPos.get(i);
              
              fishes.get(pos).isDead = true;
              
              sum += fishes.get(pos).num;
              shark.x = fishes.get(pos).x;
              shark.y = fishes.get(pos).y;
              shark.dir = fishes.get(pos).dir;
              
              stage(sum, cnt+1);
              
              
              fishes.get(pos).isDead = false;
              sum -= fishes.get(pos).num; 
              
          }
       }
        
        
    }
    
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      fishes = new ArrayList<>(); 
      
      
      for(int i=1; i<=4; i++){
          
          for(int j=1; j<=1; j++){
              
              int a1 = sc.nextInt();
              int b1 = sc.nextInt();
              int a2 = sc.nextInt();
              int b2 = sc.nextInt();
              int a3 = sc.nextInt();
              int b3 = sc.nextInt();
              int a4 = sc.nextInt();
              int b4 = sc.nextInt();
              System.out.println(a1 + " " + b1 + " " + a2 + " " + b2 + " " + a3 + " " + b3 + " " + a4 + " " + b4);
              
              fishes.add(new Fish(i, 1, a1, b1, false));
              fishes.add(new Fish(i, 2, a2, b2, false));
              fishes.add(new Fish(i, 3, a3, b3, false));
              fishes.add(new Fish(i, 4, a4, b4, false));
          }
      }
      
      
      startShark(); 
      
      Collections.sort(fishes);
      
      answer = Integer.MIN_VALUE; 
      
      stage(0, 0);
      
    

      System.out.println(answer);
    }
}
