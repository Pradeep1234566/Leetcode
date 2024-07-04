int romanToInt(char* s) 
{
   int i=0,result = 0;
   while(s[i]!='\0')
   {
       if(s[i]=='I')
       {
           if(s[i+1]=='V')
           {
               result=result+4;
               i=i+2;
           }
           else if(s[i+1]=='X')
           {
               result = result +9;
               i=i+2;
           }
           else
           {
               result = result +1;
               i=i+1;
           }
       }
       else if(s[i]=='X')
       {    
           if(s[i+1]=='L')
           {
               result = result + 40;
               i = i + 2;
           }
           else if(s[i+1]=='C')
           {
               result = result + 90;
               i = i +2;
           }
           else
           {
               result = result+10;
               i = i +1;
           }
       }
       else if(s[i]=='C')
       {
           if(s[i+1]=='D')
           {
               result = result + 400;
               i= i +2;
           }
           else if(s[i+1]=='M')
           {
               result = result + 900;
               i = i + 2;
           }
           else
           {
               result = result+100;
               i = i +1;
           }
       }
       else if(s[i]=='V')
       {
           result = result + 5;
           i = i+1;
       }
       else if(s[i]=='L')
       {
           result = result + 50;
           i = i+1;
       }
       else if (s[i]=='D')
       {
           result = result + 500;
           i = i+1;
       }
       else if(s[i]=='M')
       {
           result = result + 1000;
           i = i + 1;

       }
   }
   return result;
}