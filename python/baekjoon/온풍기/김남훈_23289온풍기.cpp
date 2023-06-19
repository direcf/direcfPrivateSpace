#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int R, C,K;
int house[21][21];
int onpung[400][3];
int tocheck[400][2];
int W;
int wallinfo0[21][21];
int wallinfo1[21][21];
int tocheckidx = 0;
int onpungidx = 0;

int dir[5][2] = { 0,0,0,1,0,-1,-1,0,1,0 };
int isout(int x, int y)
{
	if (x <= 0 || x > R || y <= 0 || y > C)
		return 1;
	else
		return 0;
}

void showhouse()
{
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			cout << house[i][j] << ' ';
		}
		cout << endl;
	}
	cout << "\n\n";
}


void onblow()
{
	for (int oidx = 0; oidx < onpungidx; oidx++)
	{
		int ox = onpung[oidx][0];
		int oy = onpung[oidx][1];
		int od = onpung[oidx][2];
		int isdone[21][21] = { 0, };
		if (od == 1)	//오른쪽
		{
			if (wallinfo1[ox][oy] == 1)
				continue;
			int x = ox + dir[od][0];
			int y = oy + dir[od][1];
			if (isout(x, y) == 1)
				continue;
			isdone[x][y] = 1;
			house[x][y] += 5;
			for (int i = 0; i < 4; i++)
			{
				for (int j = -i; j <= i; j++)
				{
					int cy = y + i * dir[od][1];
					int cx = x + j;
					//cout << cx << ' ' << cy << endl;
					if (isout(cx, cy) == 1)
						continue;
					if (isdone[cx][cy] == 0)
						continue;
					for (int k = -1; k <= 1; k++)
					{
						int ny = cy + dir[od][1];
						int nx = cx + k;
						if (isout(nx, ny) == 1)
							continue;
						if (k == -1)
						{
							if (wallinfo0[nx+1][ny-1] || wallinfo1[nx][ny - 1])
								continue;
						}
						else if (k == 1)
						{
							if (wallinfo0[nx][ny-1 ] || wallinfo1[nx][ny - 1])
								continue;
						}
						else if (k == 0)
						{
							if (wallinfo1[nx][ny - 1])
								continue;
						}


						if (isdone[nx][ny] == 1)
							continue;
						house[nx][ny] += (4 - i);
						isdone[nx][ny] = 1;
					}
				}
			}
		}
		else if (od == 2)	//left
		{
			if (oy > 0 && wallinfo1[ox][oy - 1] == 1)
				continue;
			int x = ox + dir[od][0];
			int y = oy + dir[od][1];
			if (isout(x, y) == 1)
				continue;
			isdone[x][y] = 1;
			house[x][y] += 5;
			for (int i = 0; i < 4; i++)
			{
				for (int j = -i; j <= i; j++)
				{
					int cy = y + i * dir[od][1];
					int cx = x + j;
					//cout << cx << ' ' << cy << endl;
					if (isout(cx, cy) == 1)
						continue;
					if (isdone[cx][cy] == 0)
						continue;
					for (int k = -1; k <= 1; k++)
					{
						int ny = cy + dir[od][1];
						int nx = cx + k;
						if (isout(nx, ny) == 1)
							continue;
						if (k == -1)
						{
							if (wallinfo0[nx+1][ny] || wallinfo1[nx][ny])
								continue;
						}
						else if (k == 1)
						{
							if (wallinfo0[nx][ny] || wallinfo1[nx][ny])
								continue;
						}
						else if (k == 0)
						{
							if (wallinfo1[nx][ny])
								continue;
						}


						if (isdone[nx][ny] == 1)
							continue;
						house[nx][ny] += (4 - i);
						isdone[nx][ny] = 1;
					}
				}
			}
		}
		else if (od == 3)	//up
		{
			if (wallinfo0[ox][oy] == 1)
				continue;
			int x = ox + dir[od][0];
			int y = oy + dir[od][1];
			if (isout(x, y) == 1)
				continue;
			isdone[x][y] = 1;
			house[x][y] += 5;
			for (int i = 0; i < 4; i++)
			{
				for (int j = -i; j <= i; j++)
				{
					int cy = y + j;
					int cx = x + i * dir[od][0];
					//cout << cx << ' ' << cy << endl;
					if (isout(cx, cy) == 1)
						continue;
					if (isdone[cx][cy] == 0)
						continue;
					for (int k = -1; k <= 1; k++)
					{
						int ny = cy + k;
						int nx = cx + dir[od][0];
						if (isout(nx, ny) == 1)
							continue;
						if (k == -1)
						{
							if (wallinfo0[nx+1][ny] || wallinfo1[nx][ny])
								continue;
						}
						else if (k == 1)
						{
							if (wallinfo0[nx+1][ny] || wallinfo1[nx][ny + 1])
								continue;
						}
						else if (k == 0)
						{
							if (wallinfo0[nx+1][ny])
								continue;
						}


						if (isdone[nx][ny] == 1)
							continue;
						house[nx][ny] += (4 - i);
						isdone[nx][ny] = 1;
					}
				}
			}
		}
		else if (od == 4)	//down
		{
			if (ox<R && wallinfo1[ox+1][oy] == 1)
				continue;
			int x = ox + dir[od][0];
			int y = oy + dir[od][1];
			if (isout(x, y) == 1)
				continue;
			isdone[x][y] = 1;
			house[x][y] += 5;
			for (int i = 0; i < 4; i++)
			{
				for (int j = -i; j <= i; j++)
				{
					int cy = y + j;
					int cx = x + i * dir[od][0];
					//cout << cx << ' ' << cy << endl;
					if (isout(cx, cy) == 1)
						continue;
					if (isdone[cx][cy] == 0)
						continue;
					for (int k = -1; k <= 1; k++)
					{
						int ny = cy + k;
						int nx = cx + dir[od][0];
						if (isout(nx, ny) == 1)
							continue;
						if (k == -1)
						{
							if (wallinfo0[nx ][ny] || wallinfo1[nx-1][ny])
								continue;
						}
						else if (k == 1)
						{
							if (wallinfo0[nx][ny] || wallinfo1[nx-1][ny - 1])
								continue;
						}
						else if (k == 0)
						{
							if (wallinfo0[nx][ny])
								continue;
						}


						if (isdone[nx][ny] == 1)
							continue;
						house[nx][ny] += (4 - i);
						isdone[nx][ny] = 1;
					}
				}
			}
		}
		//showhouse();
		int de = -1;
	}


	

}

void adjust()
{
	int temp[21][21] = {0, };
	for (int x = 1; x < R; x++)
	{
		for (int y = 1;y < C; y++)
		{
			int nx, ny, d;
			if (!wallinfo0[x+1][y]) {
				nx = x + 1;
				ny = y;
			
				if (house[x][y] > house[nx][ny])
				{
					d = (house[x][y] - house[nx][ny])/4;

					temp[x][y] -= d;
					temp[nx][ny] += d;
				}
				else
				{
					d = (house[nx][ny] - house[x][y]) / 4;
					temp[x][y] += d;
					temp[nx][ny] -= d;
				}
				
			}
			if (!wallinfo1[x][y]) {
				nx = x;
				ny = y + 1;
				if (house[x][y] > house[nx][ny])
				{
					d = (house[x][y] - house[nx][ny]) / 4;
					temp[x][y] -= d;
					temp[nx][ny] += d;
				}
				else
				{
					d = (house[nx][ny] - house[x][y]) / 4;
					temp[x][y] += d;
					temp[nx][ny] -= d;
				}
			}
		}
	}

	for (int x = 1; x <= R; x++)
	{
		for (int y = 1; y <= C; y++)
		{
			house[x][y] += temp[x][y];
		}
	}

}

void droptemp() {
	for (int i = 1; i <= R; i++)
	{
		if (house[i][1] > 0)
			house[i][1]--;
		if (house[i][C] > 0)
			house[i][C]--;
	}

	for (int i = 2; i < C; i++)
	{
		if (house[1][i] > 0)
			house[1][i]--;
		if (house[R][i] > 0)
			house[R][i]--;
	}
}

int isvalidh()
{
	int ans = 1;
	for (int i = 0; i < tocheckidx; i++)
	{
		if (house[tocheck[i][0]][tocheck[i][1]] < K)
		{
			return 0;
		}
	}
	return 1;
}

int main(int argc, char** argv)
{
	freopen("input.txt", "r", stdin);
	cin >> R >> C>>K;
	

	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			int n;
			cin >> n;
			if (n != 0 && n!=5)
			{
				onpung[onpungidx][0] = i;
				onpung[onpungidx][1] = j;
				onpung[onpungidx][2] = n;
				onpungidx++;
			}
			else if (n == 5)
			{
				tocheck[tocheckidx][0] = i;
				tocheck[tocheckidx][1] = j;
				tocheckidx++;
			}
		}
	}

	cin >> W;
	int wallinfoidx1 = 0;
	int wallinfoidx2 = 0;
	for (int i = 0; i < W; i++)
	{
		int y, x, d;
		cin >> y >> x >> d;
		if (d == 0)
		{
			wallinfo0[y][x] = 1;

		}
		else if (d == 1)
		{
			wallinfo1[y][x] = 1;
		}
	}
	//showhouse();
	for (int i = 1; i <= 100; i++)
	{
		onblow();
		//showhouse();
		adjust();
		//showhouse();
		droptemp();
		//showhouse();
		int isdone = isvalidh();
		//cout << isdone << endl;
		if (isdone)
		{
			cout << i;
			return 0;
		}
	}
	//showhouse();
	//onblow();
	//showhouse();
	//adjust();
	//showhouse();


	cout << 101;
	return 0;//정상종료시 반드시 0을 리턴해야합니다.

}

