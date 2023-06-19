#include <iostream>

using namespace std;

int T[17];
int P[17];
int sum[17];

int main(void)
{
	int n;
	int maximum = 0;

	cin >> n;

	for (int i = 1; i <= n; i++)
		cin >> T[i] >> P[i];

	for (int i = 1; i <= n + 1; i++)
	{
		int nd = i + T[i];

		if (sum[i + 1] < sum[i])
			sum[i + 1] = sum[i];

		if (sum[nd] < sum[i] + P[i])
			sum[nd] = sum[i] + P[i];
	}

	for (int i = 1; i <= n + 1; i++)
	{
		//cout << sum[i] << " ";
		if (maximum < sum[i])
			maximum = sum[i];
	}
	//cout << endl;

	cout << maximum << "\n";

	return 0;
}