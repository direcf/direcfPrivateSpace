#include <iostream>

using namespace std;

int num[20];
int n;
int maxi = -1e9;
int mini = 1e9;

void find(int idx, int cal[4], long long sum)
{
	if (idx == n + 1)
	{
		if (sum > maxi)
			maxi = sum;

		if (sum < mini)
			mini = sum;

		return;
	}
	else
	{
		for (int i = 0; i < 4; i++)
		{
			if (cal[i] != 0)
			{
				cal[i]--;

				if (i == 0)
					find(idx + 1, cal, sum + num[idx]);
				else if (i == 1)
					find(idx + 1, cal, sum - num[idx]);
				else if (i == 2)
					find(idx + 1, cal, sum * num[idx]);
				else if (i == 3)
					find(idx + 1, cal, sum / num[idx]);

				cal[i]++;
			}
		}
	}

	return;
}

int main(void)
{
	int cal[4];
	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> num[i];

	for (int i = 0; i < 4; i++)
		cin >> cal[i];

	find(2, cal, num[1]);

	cout << maxi << "\n";
	cout << mini << "\n";

	return 0;
}