#include <bits/stdc++.h>
//#include<ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

#define ll              long long
#define ld              long double
#define get(a)          int a; cin>>a;
#define getl(a)         long long a; cin>>a;
#define put(a)          cout<<a<<" ";
#define putn(a)         cout<<a<<"\n";
#define rep(i,a,b)      for(int i=a; i<=b; i++)
#define repr(i,a,b)     for(int i=a; i>=b; i--)
#define vi              vector<long long>
#define vs              vector<string>
#define ump             unordered_map
#define mp              map
#define pq_max          priority_queue<long long>
#define pq_min          priority_queue< long long , vi , greater<long long> >
#define init(a,n)       vector<long long> a(n+1); for(int i=1; i<=n; i++) { cin>>a[i]; }
#define logarr(a)       for(auto i:a) { cout<<i<<" "; } cout<<"\n"; 
#define log(args...)    { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
#define token(str,ch)   (std::istringstream var((str)); vs v; string t; while(getline((var), t, (ch))) {v.pb(t);} return v;)
#define all(x)          x.begin(), x.end()
#define mid(l,r)        (l+(r-l)/2)
#define pii             pair<ll,ll>
#define mod             1000000007
#define N               100001
#define pb              emplace_back
#define pf              first
#define ps              second
#define bpc             __builtin_popcountll
#define ctz             __builtin_ctzll
#define clz             __builtin_clzll
#define precise(n)      cout<<fixed<<setprecision(n)

// #define ordered_set tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>;
//using namespace __gnu_pbds;
using namespace std;

vs tokenizer(string str,char ch) {std::istringstream var((str)); vs v; string t; while(getline((var), t, (ch))) {v.pb(t);} return v;}

void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args)
{
    cout << *it << " = " << a << "\n";
    err(++it, args...);
}

void file_i_o()
{
    freopen("./tests/test01.txt", "r", stdin);
    freopen("./tests/output01.txt", "w", stdout);
}
vi memo;

ll solve(int n, vi heights) {
    if(memo[n] == -1) {
        ll ans = 0;
        if(n == 1)  ans = 0;
        if(n == 2) ans = abs (heights[2] - heights[1]);
        if (n > 2) ans = min(solve(n - 1,heights) + abs(heights[n]-heights[n-1]), solve(n-2,heights) + abs(heights[n] - heights[n-2]));
        memo[n] = ans;
    }
    return memo[n];
    }

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    memo.assign(12+1,-1);
    vi heights = {0,10,27,11,25,26,11,38,15,30,41,27,38};
    cout << solve(12, heights);
}