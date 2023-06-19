import java.util.*; 

public class Main {
    
    public static int[][] wheels;
    public static int[][] tmpWheels; 
    public static boolean[] visited; 
    
    
    public void moveClockWard(int num){
           
         int tmp = tmpWheels[num][8];
         
         for(int i=7; i>=1; i--){
             tmpWheels[num][i+1] = tmpWheels[num][i];
         }
         
         tmpWheels[num][1] = tmp;
        
    }
    
    
    public void moveUnClockWard(int num){
    
         int tmp = tmpWheels[num][1];
         
         for(int i=2; i<=8; i++){
             tmpWheels[num][i-1] = tmpWheels[num][i];
         }
         
         tmpWheels[num][8] = tmp;
        
        
    }
    
    
    public void DFS(int num, int direction){
        
        
        visited[num] = true; 
        
        for(int i=1; i<=8; i++){
            int tmpNum = tmpWheels[num][i];
            wheels[num][i] = tmpNum;
        }
        
        if(direction == 1){
            moveClockWard(num);
        }else{
            moveUnClockWard(num); 
        }
        
        
        
        if(num >= 2 && wheels[num-1][3] != wheels[num][7] && visited[num-1] == false){
              if(direction == 1){
                DFS(num-1, -1);
            }else{
                DFS(num-1, 1);
            }
        }
        
        if(num <= 3 && wheels[num][3] != wheels[num+1][7] && visited[num+1] == false){
            if(direction == 1){
                DFS(num+1, -1);
            }else{
                DFS(num+1, 1);
            }
        }
        
        
    }

    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      
      int answer = 0; 
      
      wheels = new int[10][10];
      tmpWheels = new int[10][10];
      
      for(int i=1; i<=4; i++){
          String str = sc.next();
          for(int j=0; j<str.length(); j++){
              wheels[i][j+1] = str.charAt(j)-'0';
          }
      }
      
      int K = sc.nextInt(); 
      
      
      for(int i=1; i<=K; i++){
          visited = new boolean[10];
          int num = sc.nextInt();
          int direction = sc.nextInt();
          for(int j=1; j<=4; j++){
              for(int k=1; k<=8; k++){
                tmpWheels[j][k] = wheels[j][k];   
              }
          }
          
          T.DFS(num, direction); 
          for(int j=1; j<=4; j++){
              for(int k=1; k<=8; k++){
                wheels[j][k] = tmpWheels[j][k];   
              }
          }
      }
      
      
      for(int i=1; i<=4; i++){
         if(wheels[i][1] == 0){
             continue;
         }else{
             answer += Math.pow(2, i-1);
         }
      }
      
      
      System.out.println(answer); 
      
      
      
    }
}
