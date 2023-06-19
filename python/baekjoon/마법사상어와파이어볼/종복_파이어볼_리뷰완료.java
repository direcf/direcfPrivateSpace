import java.util.*; 

class Info{
    
    int r;
    int c;
    int m;
    int s;
    int d;
    
    public Info(int r, int c, int m, int s, int d){
        this.r = r;
        this.c = c;
        this.m = m;
        this.s = s;
        this.d = d; 
    }
    
    
}



public class Main {
    
    public static int N;
    public static int M;
    public static int K; 
    public static ArrayList<Info>[][] map;
    public static ArrayList<Info> fireballs;
    public static ArrayList<Info> newFireballs;
    public static int arriveR;
    public static int arriveC; 
    
    // 8방향을 dx, dy로 나타낸다. 
    public static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    public static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1}; 
    
    
    public static void DFS(int r, int c, int d, int s){
        
           // 속도가 0이 되면, 즉 도착하면
           // 도착지점을 기록해준다. 
           if(s == 0){
               arriveR = r;
               arriveC = c;
               return; 
           }
        
             
           int nr = r + dx[d];
           int nc = c + dy[d];
           
           if(1<=nr && nr<=N && 1<=nc && nc<=N){
               DFS(nr, nc, d, s-1);
           }else{
               
               
               // r이 1이상 N이하를 벗어나면 값을 업데이트한다. 
               if(nr == 0){
                   nr = N;
               }else if(nr == N+1){
                   nr = 1; 
               }
               
               // c가 1이상 N이하를 벗어나면 값을 업데이트한다. 
               if(nc == 0){
                   nc = N;
               }else if(nc == N+1){
                   nc = 1;
               }
               
               // DFS에서 속도를 1 감소시킨다. 
               DFS(nr, nc, d, s-1);
               
           }
          
        
        
    }
    
    
    public static void main(String args[]) {
      Main T = new Main(); 
      Scanner sc = new Scanner(System.in);
      int answer = 0; 
      
      N = sc.nextInt(); 
      M = sc.nextInt();
      K = sc.nextInt();
      
      map = new ArrayList[N+10][N+10];
      
      
      
      fireballs = new ArrayList<>();
      
      // 첫 조건의 fireball들을 배열에 넣어준다.    
      // 이 때, Info라는 클래스를 만들어서 정보를 관리한다. 
      for(int i=1; i<=M; i++){
          int r = sc.nextInt();
          int c = sc.nextInt();
          int m = sc.nextInt();
          int s = sc.nextInt();
          int d = sc.nextInt();
          
          fireballs.add(new Info(r, c, m, s, d));
      }
      
      
      // 마법사 상어는 K번 이동을 명령한다. 
      while(K != 0){
          
          // 파이어볼들을 담을 map 배열을 만든다. 
         for(int i=1; i<=N; i++){
           for(int j=1; j<=N; j++){
              map[i][j] = new ArrayList<>();
           }
         }
          
          // 파이어볼들을 각 정보에 따라 이동시킨다.
          // 이 때, 방향은 8개가 있고,
          // 맵에 대한 정보에 유의해서 이동한다. 
          // 그리고 도착한 지점에 파이어볼을 넣어준다. 
          for(int i=0; i<fireballs.size(); i++){
              Info curr = fireballs.get(i);
              arriveR = 0;
              arriveC = 0; 
              
              DFS(curr.r, curr.c, curr.d, curr.s);
              
              // 도착한 지점에 fireball을 넣어준다. 
              map[arriveR][arriveC].add(new Info(arriveR, arriveC, curr.m, curr.s, curr.d));
              
          }
          
          newFireballs = new ArrayList<>();
          
          
          for(int i=1; i<=N; i++){
              for(int j=1; j<=N; j++){
                  ArrayList<Info> arr = map[i][j];
                  
                  // i,j에 파이어볼이 하나도 없다면, 그냥 continue 한다. 
                  if(arr.size() == 0){
                      continue; 
                  }
                  // i,j에 파이어볼이 하나라면, 그냥 넣어준다. 
                  else if(arr.size() == 1){
                      newFireballs.add(arr.get(0));
                      continue;
                  }
                  
                  // i,j에 파이어볼이 2개 이상이라면
                  // 파이어볼과 관련한 연산을 수행한다. 
                  int mSum = 0;
                  int sSum = 0; 
                  int oddCnt = 0;
                  int evenCnt = 0; 
                  
                  // 파이어볼들의 질량의 합을 구하고,
                  // 파이어볼들의 속도의 합을 구한다. 
                  for(int k=0; k<arr.size(); k++){
                      mSum += arr.get(k).m;
                      sSum += arr.get(k).s;
                      
                      if(arr.get(k).d % 2 == 0){
                          evenCnt++;
                      }else{
                          oddCnt++;
                      }
                  }
                  /*
                  System.out.println("mSum은?" + mSum);
                  System.out.println("sSum은?" + sSum); 
                  System.out.println("arr.size()는?" + arr.size()); 
                  System.out.println("sSum/arr.size()는?" + sSum/arr.size());
                  */
                  
                  // 새로운 파이어볼이 질량이 0이라면 소멸된다. 
                  if(mSum / 5 == 0){
                      continue;
                  }else{
                      
                      // 새로운 파이어볼이 질량이 0이 아니라면
                      // 합쳐지는 파이어볼들의 방향에 따라
                      // 정보를 업데이트 한다. 
                      for(int k=0; k<4; k++){
                          if(oddCnt == arr.size() || evenCnt == arr.size()){
                            newFireballs.add(new Info(i, j, mSum/5, sSum/arr.size(), 2*k));
                          }else{
                            newFireballs.add(new Info(i, j, mSum/5, sSum/arr.size(), 2*k+1));
                          }
                      }
                      
                  }
                  
                  
                  
              }
          }
          
          // 기존의 파이어볼들을 없애고, 
          fireballs.clear();
          // System.out.println("새 정보");
          
          // 새로운 파이어볼로 기존의 파이어볼 정보를 교체한다. 
          for(int i=0; i<newFireballs.size(); i++){
              // System.out.println(newFireballs.get(i).r + " " + newFireballs.get(i).c + " " + newFireballs.get(i).m + " " + newFireballs.get(i).s + " " + newFireballs.get(i).d);
              fireballs.add(newFireballs.get(i));
          };  
          
          K--; 
        
      }
      
      
      
      for(int i=0; i<fireballs.size(); i++){
          answer += fireballs.get(i).m;
      }
      
      
      System.out.println(answer); 
      
      
      
      
    }
}
