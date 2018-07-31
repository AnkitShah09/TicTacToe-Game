#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int i,j,flag=0;
void check(int a[][3],int p)
{
	if(a[0][0]==p && a[1][1]==p && a[2][2]==p)
	{
		flag=1;
	}
	else if(a[0][2]==p && a[1][1]==p && a[2][0]==p)
	{
		flag=1;
	}
	else if(a[0][0]==p && a[0][1]==p && a[0][2]==p)
	{
		flag=1;
	}
	else if(a[0][0]==p && a[1][0]==p && a[2][0]==p)
	{
		flag=1;
	}
	else if(a[2][0]==p && a[2][1]==p && a[2][2]==p)
	{
		flag=1;
	}
	else if(a[0][2]==p && a[1][2]==p && a[2][2]==p)
	{
		flag=1;
	}
}
void main()
{
	int a[3][3]={0},cn[2]={0},x,y,num,n=1,c=20,r=5,p;
	char ch;
	clrscr();
	textcolor(RED);
	printf("\n\t\t\tWelcome to Game");
	randomize();
	p=random(2)+1;

	do
	{
		gotoxy(50,10);
		printf("                                   ");
		gotoxy(50,3);
		printf("Now Player-%d chance:",p);
		gotoxy(50,4);
		printf("Enter the Position:");
		gotoxy(50,5);
		printf("Row:");
		scanf("%d",&x);
		gotoxy(50,6);
		printf("Column:");
		scanf("%d",&y);
		if(a[x-1][y-1]==0)
		{
			for(i=x-1;i<x;i++)
			{
				for(j=y-1;j<y;j++)
				{
					a[i][j]=p;
					cn[p-1]++;
				}
			}
			r=5,c=10;
			for(i=0;i<3;i++)
			{
				r++;
				gotoxy(c,r++);
				printf("-------------");
				gotoxy(c,r);
				printf("%c",179);
				for(j=0;j<3;j++)
				{
					gotoxy(c+j*4,r);
					printf("%c %d %c",179,a[i][j],179);
				}
			}
			gotoxy(c,++r);
			printf("-------------");
		}
		else
		{
			gotoxy(50,10);
			printf("Entered place is already filled");
		}
		check(a,p);
		if(flag==1)
		{
			gotoxy(25,15);
			printf("%d is won",p);
			getch();
			return;
		}
		gotoxy(50,8);
		printf("Enter n for exit:");
		ch=getch();
		gotoxy(54,5);printf("  ");
		gotoxy(57,6);printf("  ");
		p=p==1?2:1;
		n++;
		if(n>9)
		{
			break;
		}
	}while(ch!='n');
	gotoxy(25,15);
	check(a,p);
	if(flag==0)
	{
		printf("Draw:");
		getch();
	}
}