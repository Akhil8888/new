#include<stdio.h>
#include<stdlib.h>
int a[20];
int main()
{
	int ch,i,del,sch,pos,val;
	int num;
	setbuf(stdout,NULL);
	do{
	printf("Enter the task to perform \n0)Create\n1)insertion\n2)deletion\n3)searching\n4)display\n5)exit");
	scanf("%d",&ch);

	switch (ch) {
		case 0:
			printf("enter the number of elements in array");
			scanf("%d",&num);
			printf("enter the array elements");
			for(i=0;i<num;i++)
			{
				scanf("%d",&a[i]);

			}
			break;
		case 1:
			printf("Enter the position of element to be inserted");
			scanf("%d",&pos);
			pos=pos-1;
			printf("Enter the value");
			scanf("%d",&val);
			for(i=num;i==pos;i++)
			{
				a[i+1]=a[i];

			}
			a[pos]=val;
			break;
		case 4:
			printf("Elements in array are");
			for (i=0;i<num;i++)
			{
				printf("%d",a[i]);

			}

			break;
		case 3:
			printf("enter the element to search");
			scanf("%d",&sch);
			for(i=0;i<num;i++)
			{
				if(a[i]==sch)
				{
					printf("element found at %d  position",i);
				}
			}
			break;
		case 2:
			printf("enter the position of number to be deleted");
			scanf("%d",&del);

			for(i=del-1;i<=num;i++)
			{

				a[i]=a[i+1];

			}
			printf("Numbers after deletion are");
			for(i=0;i<num-1;i++)
			{
				printf("%d \n",a[i]);
			}
                  break;
		default:
			printf("element not found");
			break;
	}}while(ch!=5);




	return 0;
}
