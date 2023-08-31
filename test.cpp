#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define print(a) for(auto x : a) cout << x <<" ";cout <<"\n"
#define printm(a) for(const auto& e : a) cout<<e.first<<" "<<e.second<<"\n"
#define nxtl "\n"

ll calc(int item,int a[],vector<pair<int,int>> &v,ll num=0){
	if(v[item].first==-1 and v[item].second==-1) return num+a[item];
	num+=a[item];
	num*=10;
	ll ans=0;
	if(v[item].first!=-1) ans+=calc(v[item].first,a,v,num);
	if(v[item].second!=-1) ans+=calc(v[item].second,a,v,num);
	return ans; 
}
void solve() {
	int n;
	cin>>n;
	int a[n];
	vector<pair<int,int>> v;
	for(auto &it:a) cin>>it;
	for(int i=0;i<n;i++){
		int x,y;
		cin>>x>>y;
		v.push_back(make_pair(x,y));
	}
	ll ans=calc(0,a,v);
	cout<<ans;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t = 1;
	// cin >> t;
	while (t--) solve();
	return 0;
}