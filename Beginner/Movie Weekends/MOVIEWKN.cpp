#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n],brr[n];
	    int product=0,rating=0,index=0;
	    for(int i=0;i<n;i++)
	    {
	        cin>>arr[i];

	    }
	    for(int i=0;i<n;i++)
	    {
	        cin>>brr[i];
	    }
	     for(int i=0;i<n;i++)
	     {
	         if(arr[i]*brr[i]>=product && brr[i] > rating )
	         {
	             product=arr[i]*brr[i];
	             rating = brr[i];
	             index=i;


	         }
	    }
	     cout<<index+1<<endl;





	}
	return 0;
}
