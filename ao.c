#include<stdio.h>
int main()
{
 int a,b,c;
  printf("please enter a,b");
  scanf("%d%d\n",&a,&b);
  c=a+b;
  printf("\n%d+%d=%d",a,b,c);
  c=a-b;
  printf("\n%d-%d=%d",a,b,c);
  c=a*b;
  printf("\n%d*%d=%d",a,b,c);
  c=(a/b);
  printf("\n%d/%d=%d",a,b,c);
  return 0

}
