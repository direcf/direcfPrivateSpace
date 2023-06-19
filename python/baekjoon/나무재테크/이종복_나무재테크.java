import java.util.*; 

public class Main {
    
    public static int N;
    public static int M;
    public static int K;
    public static int[][] A; 
    public static int[][] nutritions;
    public static int[][] addedNutritions; 
    public static ArrayList<Integer> [][] trees;
    public static int answer; 
    
    
    public static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    public static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1}; 
    
    public boolean isInside(int x, int y){
        
        if(1<=x && x<=N && 1<=y && y<=N){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public void winter(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                nutritions[i][j] += A[i][j]; 
            }
        }
          
    }
    
    
    
    
    public void fall(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                int len = trees[i][j].size();
                
                for(int k=0; k<len; k++){
                    if(trees[i][j].get(k) % 5 == 0){
                        breed(i,j);
                    }
                }
            }
        }
        
    }
    
    public void breed(int x, int y){
        
        
        for(int i=0; i<8; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(isInside(nx,ny)){
                trees[nx][ny].add(1);
            }
        }
    }
    
    
    
    public void summer(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                nutritions[i][j] += addedNutritions[i][j];
            }
        }
        
    }
    
    
    
    
    public void spring(){
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                
                if(trees[i][j].size() != 0){
                    
                    int addedNutrition = 0;
                    int isDead = -1;
                    int len = trees[i][j].size();
                    ArrayList<Integer> tmp = new ArrayList<>();
                    
                    for(int k=0; k<len; k++){
                        
                        int age = trees[i][j].get(k);
                        
                        if(nutritions[i][j] - age >= 0){
                            nutritions[i][j] -= age;
                            trees[i][j].set(k, age+1);
                        }else{
                            isDead = k;
                            break;
                        }
                    }
                    
                    for(int k=0; k<isDead; k++){
                        tmp.add(trees[i][j].get(k));
                    }
                    
                    if(isDead != -1){
                        for(int k=isDead; k<len; k++){
                            addedNutrition += (trees[i][j].get(k)/2);
                        }
                    }
                    
                    addedNutritions[i][j] = addedNutrition;
                    
                    if(isDead != -1){
                        trees[i][j].clear();
                        for(int k=0; k<isDead; k++){
                            trees[i][j].add(tmp.get(k));
                        }
                    }
                }
                
                
            }
        }
        
        
        
        
    }
    
    
    
    
    
    
    public void sort(){
        
        
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              Collections.sort(trees[i][j]);
          }
      }
        
        
    }
    
    
    
    
    public void treeFinance(){
        
        int year = 0; 
        
        
        while(true){
            
            if(year == K){
                break; 
            }
            
            addedNutritions = new int[N+10][N+10];
            
            spring();
            
            summer();
            
            fall();
            
            sort(); 
            
            
            winter();
            
            year++;
            
        }
        
        
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                answer += trees[i][j].size(); 
            }
        }
        
        
    }
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      
      Scanner sc = new Scanner(System.in);
      answer = 0; 
      
      N = sc.nextInt();
      M = sc.nextInt();
      K = sc.nextInt();
      
      A = new int[N+10][N+10];
     
      trees = new ArrayList[N+10][N+10];
      nutritions = new int[N+10][N+10];
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              trees[i][j] = new ArrayList<>();
          }
      }
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              A[i][j] = sc.nextInt(); 
          }
      }
      
      
      for(int i=1; i<=N; i++){
          for(int j=1; j<=N; j++){
              nutritions[i][j] = 5;
          }
      }
      
      for(int i=1; i<=M; i++){
          int x = sc.nextInt();
          int y = sc.nextInt();
          int age = sc.nextInt();
          trees[x][y].add(age);
      }
      
      T.sort(); 
      
      T.treeFinance();
      
      
      System.out.println(answer); 
      
      
      
      
      
      
      
    }
}
