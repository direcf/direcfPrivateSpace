#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int map[21][21];
int n;
int mini = 987654321;

int cal(vector<int> team)
{
	int ret = 0;

	for (int i = 0; i < team.size(); i++)
	{
		int player1 = team[i];

		for (int j = 0; j < team.size(); j++)
		{
			int player2 = team[j];

			if (player1 == player2)
				continue;

			ret += map[player1][player2];
		}
	}

	return ret;
}

void find(int idx, vector<int> team_a, bool check_a[21])
{
	if (team_a.size() == n / 2)
	{
		vector<int> team_b;

		for (int i = 1; i <= n; i++)
		{
			if (!check_a[i])
				team_b.push_back(i);
		}

		int sum_a = cal(team_a);
		int sum_b = cal(team_b);

		int diff = abs(sum_a - sum_b);

		if (diff < mini)
			mini = diff;

		return;
	}
	else
	{
		for (int i = idx; i <= n; i++)
		{
			team_a.push_back(i);
			check_a[i] = true;

			find(i + 1, team_a, check_a);
			
			team_a.pop_back();
			check_a[i] = false;
		}
	}

	return;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	bool check_a[21];
	memset(check_a, 0, sizeof(check_a));

	vector<int> team_a;
	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= n; j++)
		{
			cin >> map[i][j];
		}
	}
	
	find(1, team_a, check_a);

	cout << mini << "\n";

	return 0;
}