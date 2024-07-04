bool isPalindrome(int x) 
{
    int a,i;
    int b[10];
    a=x;
    i=0;
    if(a>=0)
    {
        while(a>0)
    {
        b[i]=a%10;
        a= a/10;
        i++;
    }
    int count=i,key=0;
    for(i=0;i<count;i++)
    {
        if(b[i]!=b[count-i-1])
        {
            key = 1;
            break;
        }
        key=0;
    }
    if(key==1)
    {
        return false;
    }
    else
    {
        return true;
    }
    }
    else
    {
        return false;
    }
}