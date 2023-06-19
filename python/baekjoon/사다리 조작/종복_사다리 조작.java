import java.util.*; 

public class Main {
    
    
    public static int N;
    public static int M;
    public static int H;
    public static boolean[][][][] ladder; 
    public static int arrive; 
    public static int minCnt; 
    
    
    
    public static void move(int x, int y){
        
           // System.out.println("x, y는?" + x + " " + y);
        
        
          if(x == H+1){
              arrive = y;
              return; 
          }
        
        
          int ny1 = y+1;
          int ny2 = y-1;
          
          if( ((1<=ny1 && ny1<=N) && ladder[x][y][x][ny1] == true) || ((1<=ny2 && ny2<=N) && ladder[x][ny2][x][y] == true) ){
               
               if(1<=ny1 && ny1<= N && ladder[x][y][x][ny1] == true){
                        move(x+1, ny1);
                }
        
        
               if(1<=ny2 && ny2 <=N && ladder[x][ny2][x][y] == true ){
                    move(x+1, ny2);
               }
          }else{
              
              move(x+1, y); 
          } 
          
         
        
          
        
        
    }
    
    
    public static boolean checkAllMatching(){
          
          boolean result = true;
    
          for(int i=1; i<=N; i++){
               arrive = 0; 
               move(1, i); 
               // System.out.println("i, arrive는?" + i + " " + arrive);
               
               if(i != arrive){
                   result = false;
                   break; 
               }
          }
          
          return result; 
          
        
    }
    
    
    public static void print(){
        
        
        for(int i=1; i<=H; i++){
            for(int j=1; j<=N-1; j++){
                System.out.print(ladder[i][j][i][j+1]+ " ");
            }
            System.out.println(); 
        }
        
        
        
        
        
    }
    
    
    
    
    public static void DFS(int cnt){
        
          
          /*
          System.out.println("사다리 출력");
          print();
          */     
          boolean allMatching = true;
        
          allMatching = checkAllMatching();
          // System.out.println("결과는?" + allMatching);
          // System.out.println("cnt는?" + cnt); 
        
        
          if(allMatching){
              minCnt = Math.min(minCnt, cnt);
              return; 
          }else{
              
              if(cnt == 3){
                  return; 
              }
              
              for(int i=1; i<=H; i++){
                  for(int j=1; j<=N-1; j++){
                      
                      if(j == 1){
                          
                          if(N == 2){
                          
                              if(ladder[i][j][i][j+1] == false){
                                  ladder[i][j][i][j+1] = true;
                                  DFS(cnt+1);
                                  ladder[i][j][i][j+1] = false;
                              }
                              
                          }else{
                              
                               if(ladder[i][j][i][j+1] == false && ladder[i][j+1][i][j+2] == false){
                                  ladder[i][j][i][j+1] = true;
                                  DFS(cnt+1);
                                  ladder[i][j][i][j+1] = false;
                              }
                              
                          }
                          
                          
                      }else if(j == N){
                          
                          if(N == 2){ 
                              if(ladder[i][j-1][i][j] == false){
                                  ladder[i][j-1][i][j] = true;
                                  DFS(cnt+1);
                                  ladder[i][j-1][i][j] = false;
                              }
                          
                          }else{
                              
                              if(ladder[i][j-1][i][j] == false && ladder[i][j-2][i][j-1] == false){
                                  ladder[i][j-1][i][j] = true;
                                  DFS(cnt+1);
                                  ladder[i][j-1][i][j] = false;
                              }
                              
                          }
                          
                      }else{
                          
                           if(N == 2){
                               
                               
                              if(ladder[i][j][i][j+1] == false){
                                  ladder[i][j][i][j+1] = true;
                                  DFS(cnt+1);
                                  ladder[i][j][i][j+1] = false;
                              }
                               
                               
                              if(ladder[i][j-1][i][j] == false){
                                  ladder[i][j-1][i][j] = true;
                                  DFS(cnt+1);
                                  ladder[i][j-1][i][j] = false;
                              }
                               
                               
                           }else{
                               
                               
                               if(ladder[i][j][i][j+1] == false && ladder[i][j+1][i][j+2] == false){
                                  ladder[i][j][i][j+1] = true;
                                  DFS(cnt+1);
                                  ladder[i][j][i][j+1] = false;
                               }
                              
                               
                               
                              if(ladder[i][j-1][i][j] == false && ladder[i][j-2][i][j-1] == false){
                                  ladder[i][j-1][i][j] = true;
                                  DFS(cnt+1);
                                  ladder[i][j-1][i][j] = false;
                              }
                               
                           }
                      }
                      
                      
                      
                  }
              }
              
              
              
              
          }
        
        
        
        
        
        
        
    }
    
    
    
    
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      ladder = new boolean[H+10][N+10][H+10][N+10];
      minCnt = 987654321;
      
      N = sc.nextInt();
      M = sc.nextInt();
      H = sc.nextInt();
      
      
      for(int i=1; i<=M; i++){
          int x = sc.nextInt();
          int y = sc.nextInt();
          ladder[x][y][x][y+1] = true;
      }
      
      
      DFS(0); 
      
      
      if(minCnt == 987654321){
          minCnt = -1;
      }
      System.out.println(minCnt); 
      
      
      
      
      
      
      
      
    }
}
