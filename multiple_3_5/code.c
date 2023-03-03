#include <stdio.h>
int main(void)
{
	int temp=0;

	for (int i=0; i<1000; i++)
	{
		if ((i%3==0) || (i%5==0))
			temp+=i;
	}
	printf("Value %d",temp);
	
	return 0;
}
