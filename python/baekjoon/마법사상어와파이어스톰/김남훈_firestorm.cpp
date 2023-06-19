#include<iostream>
#include<queue>
#include<cmath>
#include<cstring>
using namespace std;

int N;
int L;
int A[64][64];
int Q;

int tN;

int dir[4][2] = { 0,1,1,0,0,-1,-1,0 };

void showA()
{
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			cout << A[i][j] << ' ';
		}
		cout << endl;
	}
	cout << "\n\n";
}
void rotate(int yy, int xx, int L)	//각 구역별 갯수에 맞춰 rotate하는함수
{
	int temp[64][64];
	int tL;
	tL = pow(2, L);
	for (int i = 0; i < tL; i++)
	{
		for(int j = 0; j < tL; j++)
		{
			temp[i][j] = A[tL-j-1+yy][i+xx];
		}
	}
	for (int i = 0; i < tL; i++)
	{
		for (int j = 0; j < tL; j++)
		{
			//temp[i][j] = A[tL - j - 1 + yy][i + xx];
			A[i+yy][j+xx] = temp[i][j];
		}
	}
}

void rotateAll(int L)	//모든 구역에 대해 rotate
{
	int tL = pow(2, L);
	int grid = tN / tL;
	for (int i = 0; i < grid; i++)
	{
		for (int j = 0; j < grid; j++)
		{
			rotate(i*tL, j*tL, L);
		}
	}

}

void icemelt()	//얼음녹이는 함수 
{
	int temp[64][64] = { 0, };	//초기화하기
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			if (A[i][j] == 0) continue;
			int icecount = 0;
			for (int d = 0; d < 4; d++)
			{
				int ny = i + dir[d][0];
				int nx = j + dir[d][1];
				if (ny < 0 || ny >= tN || nx < 0 || nx >= tN) continue;
				if (A[ny][nx] > 0) icecount++;

			}
			if (icecount < 3)
			{
				//A[i][j]--;
				temp[i][j] = A[i][j] - 1;

			}
			else
				temp[i][j] = A[i][j];
		}
	}
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			A[i][j] = temp[i][j];
		}
	}
}

int dungury()	//덩어리 크기 구하기 플러드필사용
{
	int visited[64][64] = { 0, };
	int maxx = 0;	//이거 -1로하면안됨
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			if (A[i][j] == 0) continue;
			if (visited[i][j] == 1) continue;

			queue<pair<int, int>> q;
			q.push({ i,j });
			visited[i][j] = 1;
			int dungsize = 1;
			while (!q.empty())
			{
				int y = q.front().first;
				int x = q.front().second;
				q.pop();
				for (int d = 0; d < 4; d++)
				{
					int ny = y + dir[d][0];
					int nx = x + dir[d][1];
					if (ny < 0 || ny >= tN || nx < 0 || nx >= tN) continue;
					if (A[ny][nx] == 0) continue;
					if (visited[ny][nx]==1) continue;
					visited[ny][nx] = 1;
					dungsize++;
					q.push({ ny,nx });
				}
			}
			//cout << dungsize << endl;
			
			if (maxx < dungsize) maxx = dungsize;
		}
	}
	return maxx;
}

int main()
{
	freopen("input.txt", "r", stdin);
	cin >> N >> Q;
	tN = pow(2, N);
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			cin >> A[i][j];
		}
	}
	//showA();
	//cout << dungury() << endl;
	for (int i = 0; i < Q; i++)
	{
		int L;
		cin >> L;
		rotateAll(L);
		cout << "cycle: " << i << endl << endl;
		showA();
		icemelt();
		showA();
		//cout << dungury() << endl;

		
	}
	int cnt = 0;
	int maxx = -1;
	for (int i = 0; i < tN; i++)
	{
		for (int j = 0; j < tN; j++)
		{
			cnt += A[i][j];
		}
	}
	cout << cnt << endl << dungury();

	return 0;
}