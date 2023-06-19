#include<iostream>

using namespace std;
int N;
int townpop[21][21];
int townarea[21][21];

void showarea()
{
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cout << townarea[i][j]<<' ';
		}
		cout << endl;
	}
	cout << "\n\n";
}

void areadivide(int x, int y, int d1, int d2)	//구역 나누기 1차함수
{
	for (int r = 1; r <= N; r++)
	{
		for (int c = 1; c <= N; c++)
		{
			if (r+c>=x+y && r+c<=x+y+2*d2 && r-c>=x-y && r-c<=x-y+2*d1)
				townarea[r][c] = 5;
			else if ((r < x + d1) && (c <= y))
				townarea[r][c] = 1;
			else if ((r <= x + d2) && (y < c))
				townarea[r][c] = 2;
			else if ((x + d1 <= r) && (c < y - d1 + d2))
				townarea[r][c] = 3;
			else if ((x + d2 < r) && (y - d1 + d2 <= c))
				townarea[r][c] = 4;
			
		}
	}
}

int getpopdiff()	//각 구역별 최대최소인구값 구해서 차이 구하기
{
	int areapop[5] = { 0, };
	for (int r = 1; r <= N; r++)
	{
		for (int c = 1; c <= N; c++)
		{
			areapop[townarea[r][c] - 1] += townpop[r][c];
		}
	}
	int minn = 21e8;
	int maxx = 0;
	for (int i = 0; i < 5; i++)
	{
		if (areapop[i] > maxx)
			maxx = areapop[i];
		if (areapop[i] < minn)
			minn = areapop[i];
	}
	return maxx - minn;
}

int main()
{
	freopen("input.txt", "r", stdin);

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			cin >> townpop[i][j];
		}
	}

	int ans = 21e8;
	for (int x = 1; x <= N; x++)	//모둔 경우에 대해 조건이 맞으면 값 구하고 아니면패스
	{
		for (int y = 1; y <= N; y++)
		{
			for (int d1 = 1; d1 <= N; d1++)
			{
				for (int d2 = 1; d2 <= N; d2++)
				{
					if (x + d1 + d2 > N) continue;
					if (y - d1 < 1) continue;
					if (y + d2 > N) continue;
					areadivide(x, y, d1, d2);
					int popdiff = getpopdiff();
					//cout << popdiff << endl;
					if (popdiff < ans)
						ans = popdiff;

				}
			}
		}
	}

	cout << ans;

	return 0;
}