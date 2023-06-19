import java.util.*; 


class Info{
    
    int x;
    int y;
    int d;
    
    public Info(int x, int y, int d){
        this.x = x;
        this.y = y;
        this.d = d; 
    }
    
    
}

class Shark{
    
    int x;
    int y; 
    
    public Shark(int x, int y){
        this.x = x;
        this.y = y;
    }
    
}


class Pair{
    
    int x;
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y; 
    }
    
    
}






public class Main {
    
    public static int M;
    public static int S;
    public static ArrayList<Info> fishes; 
    public static ArrayList<Info> liveFishes;
    public static ArrayList<Info> deadFishes; 
    public static Shark shark;
    public static boolean[][] visited;
    
    public static ArrayList<Integer>[][] fishSmells; 
    
    public static int[] dx = {0, -1, -1, -1, 0, 1, 1, 1};
    public static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    
    public static int[] dx2 = {-1, 0, 1, 0};
    public static int[] dy2 = {0, -1, 0, 1};
    
    
    public static ArrayList<Integer> selectedPositions;
    public static ArrayList<Integer> positions; 
    
    public static ArrayList<Info> tmp; 
    
    public boolean isInside(int x, int y){
        if(1<=x && x<=4 && 1<=y && y<=4){
            return true;
        }else{
            return false; 
        }
    }
    
    
    
    
    
    
    public void moveFish(int i, int x, int y, int d){
        
        int cnt = 0;
        
        
        while(true){
            
            if(cnt == 8){
                break; 
            }
            
            int nx = x + dx[d-1];
            int ny = y + dy[d-1];
            
            if(isInside(nx,ny) && fishSmell[nx][ny] == 0 && ((nx!=shark.x) || (ny != shark.y))){
                fishes.get(i).x = nx;
                fishes.get(i).y = ny;
                fishes.get(i).d = d;
                break; 
            }else{
                cnt++;
                
                if(d == 1){
                    d == 8;
                }else{
                    d -= 1;
                }
            }
            
            
        }
        
        
        
        
    }
    
    
    
    public void moveFishes(){
        
        
        for(int i=0; i<fishes.size(); i++){
            
            int x = fishes.get(i).x;
            int y = fishes.get(i).y;
            int d = fished.get(i).d;
            
            moveFish(i, x, y, d);
            
            
        }
        
    }
    
    
    public int calculate(ArrayList<Integer> positions){
        
            int cnt = 0; 
            
            for(int i=0; i<positions.size(); i++){
                
                    int x = positions.get(i).x;
                    int y = positions.get(i).y;
                
                for(int j=0; j<fishes.size(); j++){
                    if( (x == fishes.get(j).x) && (y == fishes.get(j).y)){
                        cnt++;
                    }
                    
                }
                
            }
            
            
            return cnt; 
        
        
        
    }
    
    
    
    public int compare(ArrayList<Integer> selectedPositions, ArrayList<Integer> positions){
        
            int sum1 = 0;
            int sum2 = 0; 
            
            int curr1 = 2;
            int curr2 = 2; 
            
            for(int i=0; i<selectedPositions.size(); i++){
                sum1 += (selectedPositions.get(i)*Math.pow(10, curr1--));
            }
            
            
            for(int i=0; i<positions.size(); i++){
                sum2 += (positions.get(i)*Math.pow(10, curr2--));
            }
            
            if(sum1 < sum2){
                return 1;
            }else{
                return -1; 
            }
             
        
        
    }
    
    
    public void dfs(int x, int y, ArrayList<Pair> positions, ArrayList<Integer> directions, int cnt){
        
        if(cnt == 3){
            
            int deadFishes = calculate(positions);
            
            if(maxDeadFishes <= deadFishes){
                maxDeadFishes = deadFishes; 
                
                if(selectedPositions.size() == 0){
                    for(int i=0; i<positions.size(); i++){
                        selectedPositions.add(positions.get(i));
                    }
                }else{
                    
                    int result = comparePositions(selectedPositions, positions);
                    
                    if(result == -1){
                        selectedPositions.clear();
                        
                        for(int i=0; i<positions.size(); i++){
                            selectedPositions.add(positions.get(i));
                        }
                    }
                    
                }
                
                
                
            }
            
            return; 
            
            
        }
        
        
        
        for(int i=0; i<4; i++){
            
            int nx = x + dx2[i];
            int ny = y + dy2[i];
            
            if(isInside(nx,ny) && visited[nx][ny] == false){
                visited[nx][ny] = true;
                positions.add(new Pair(nx, ny));
                directions.add(i+1);
                
                dfs(nx, ny, positions, directions, cnt+1);
                
                visited[nx][ny] = false;
                positions.remove(positions.size()-1);
                directions.remove(directions.size()-1);
                
                
            }
            
            
        }
        
        
        
        
        
    }
    
    
    
    
    
    public void moveShark(){
        
        int x = shark.x;
        int y = shark.y;
        
        ArrayList<Pair> positions = new ArrayList<>();
        ArrayList<Integer> directions = new ArrayList<>();
        visited = new boolean[10][10];
        
        visited[x][y] = true; 
        
        selectedPositions = new ArrayList<>(); 
        positions = new ArrayList<>(); 
        
        dfs(x, y, positions, directions, 0); 
        
        
        
    }
    
    
    public void eatFishes(){
        
        liveFishes = new ArrayList<>(); 
        deadFishes = new ArrayList<>(); 
        
        for(int i=0; i<fishes.size(); i++){
            
            int x = fishes.get(i).x;
            int y = fishes.get(i).y;
            boolean isDead = false;
            
            for(int j=0; j<selectedPositions.size(); j++){
                int posX = selectedPositions.get(j).x;
                int posY = selectedPositions.get(j).y;
                
                if(x == posX && y == posY){
                    isDead = true;
                    break; 
                }
            }
            
            if(isDead == true){
                deadFishes.add(fishes.get(i)); 
            }else{
                liveFishes.add(fishes.get(i));
            }
            
            
            
        }
        
    
        fishes.clear();
        
        for(int i=0; i<liveFishes.size(); i++){
            fishes.add(liveFishes.get(i)); 
        }
        
        
        
        
        
    }
    
    
    
    public void removeSmells(){
        
        
            for(int i=1; i<=4; i++){
                for(int j=1; j<=4; j++){
                    ArrayList<Integer> arr = fishSmells[i][j];
                    
                    
                }
            }
        
        
        
        
        
    }
    
    
    public void change(){
        
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                ArrayList<Integer> arr = fishSmells[i][j];
                
                for(int k=0; k<arr.size(); k++){
                    fishSmells[i][j].get(k) -= 1; 
                }
            }
        }
        
        
        
    }
    
    
    public void addSmells(){
        
        for(int i=0; i<deadFishes.size(); i++){
               int x = deadFishes.get(i).x;
               int y = deadFishes.get(i).y;
               
               fishSmells[x][y].add(2); 
            
        }
        
        
        
        
    }
    
    
    public void duplicate(){
        
        tmp = new ArrayList<>(); 
        
        for(int i=0; i<fishes.size(); i++){
            tmp.add(fishes.get(i)); 
        }
        
        
    }
    
    public void duplicateEnd(){
        
        for(int i=0; i<tmp.size(); i++){
            fishes.add(tmp.get(i)); 
        }
    }
    
    
    
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      
      M = sc.nextInt();
      S = sc.nextInt();
      
      for(int i=1; i<=M; i++){
          int x = sc.nextInt();
          int y = sc.nextInt();
          int d = sc.nextInt();
          
          fishes.add(new Info(x,y,d));
          
      }
      
      
      int x = sc.nextInt()
      int y = sc.nextInt();
      
      shark = new Shark(x, y);
      
      
      int practice = 0; 
      
      fishSmells = new ArrayList[10][10]; 
      
      for(int i=1; i<=4; i++){
          for(int j=1; j<=4; j++){
              fishSmells[i][j] = new ArrayList<>(); 
          }
      }
      
      
      while(true){
          
          
          duplicate();
          
          moveFishes(); 
          
          moveShark();
          
          eatFishes(); 
          
          removeSmells(); 
          
          
          practice++;
          
          change(); 
          
          addSmells(); 
          
          duplicateEnd(); 
      }
      
      
    }
}
