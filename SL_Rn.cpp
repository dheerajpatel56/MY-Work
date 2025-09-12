#include<iostream>
#include<cstdlib>
#include<ctime>
# define SIZE 10
int A[SIZE];
int c;
void init()
{
	for( int i=0;i<SIZE;i++)
	 A[i]=0;
}
int k=sizeof(A[0]);
int lad_i[7]={6,10,36,68,73,51,85};
int lad_e[7]={31,90,45,82,91,65,92};
int snake_m[8]={13,47,58,72,94,99};
int snake_t[8]={5,21,30,60,41,3};
int dice()
{
	return((rand()%6)+1);
}
void path_pro(int *x )
{
for(int i=0;i<6;i++)
{
	if(*x==lad_i[i])
	{   std::cout<<"LADDER!!"<<'\n';
	    std::cout<<*x<<"--------"<<lad_e[i]<<'\n';  
		*x=lad_e[i];
		return ;
	}
	if(*x==snake_m[i])
	{   
	    std::cout<<"ALAS SNAKE"<<'\n';
	    std::cout<<*x<<"--------"<<snake_t[i]<<'\n';
		*x=snake_t[i];
		return ;
	}
}
	return;
}
int main() {
    srand(time(0));
    std::cout<<"****************************************\n";
    std::cout<<"             SNAKE AND LADDER          \n";
    std::cout<<"****************************************\n\n";
    int n,l;
    char playAgain,changePlayers='y';
    do 
	{
        if(changePlayers=='y'||changePlayers=='Y') 
		{
            std::cout<<"Enter number of players (max 10): \n to play with computer press 1\n";
            std::cin>>n;
            while(n<=0||n>SIZE){
                std::cout<<"Invalid number! Enter again (1 to 10): ";
                std::cin>>n;
        }
        }
        init();
        if(n>1)
        {
        do{
        for(int i = 0; i < n; i++){
            std::cout << "\nPlayer "<<i+1<<"-Press 'r' to roll: ";
            char ch;
            std::cin>>ch;
            while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
            int roll = dice();
            std::cout << "Player " << i + 1 << " rolled: " << roll << "\n";
            if (A[i] + roll > 100) 
			{
                std::cout << "Can't move. Need exact roll.\n";
                continue;
            }
            l=A[i];
            A[i]+=roll;
            path_pro(&A[i]);
            while((A[i]-l)>6)
            {
                std::cout<<"Player"<<i+1<<"Has Got up A ladder!! Extra turn.\n";
                std::cout << "\nPlayer "<<i+1<<"-Press 'r' to roll: ";
            char ch;
            std::cin>>ch;
            while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(A[i]+roll<=100)
				{   l=A[i];
                    A[i]+=roll;
                    path_pro(&A[i]);
                }
			}
            while (roll==6)
		   {
                std::cout<<"Player"<<i+1<<"rolled a 6! Extra turn.\n";
                std::cout << "\nPlayer "<<i+1<<"-Press 'r' to roll: ";
            char ch;
            std::cin>>ch;
            while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(A[i]+roll<=100)
				{
                    A[i]+=roll;
                    path_pro(&A[i]);
                }
            }
            if(A[i]==100)
			{
                std::cout<<"?? Player "<<i+1<<" wins! ??\n";
                k=1;
                break;
            } 
			else
			{
                std::cout<<"Player"<<i+1<<"is at position: "<<A[i]<<"\n"<<'\n';
            }
        }
        for(int i=0;i<n;i++)
        {
        	std::cout<<"Player "<<i+1<<"is at -- "<<A[i]<<'\n'; 
		}
    }while(k!=1);
    }
    else
    {
     std::cout<<"PLAYER VS COMPUTER\n";
     int k=0;
     do
     {
     char ch='o';
       while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
            int roll = dice();
            std::cout << "Player rolled: " << roll << "\n";
            if (A[0] + roll > 100) 
			{
                std::cout << "Can't move. Need exact roll.\n";
                continue;
            }
            l=A[0];
            A[0]+=roll;
            path_pro(&A[0]);
            while((A[0]-l)>6)
            {
                std::cout<<"Player Has Got up A ladder!! Extra turn.\n";
                std::cout << "\nPlayer Press 'r' to roll: ";
            char ch;
            std::cin>>ch;
            while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(A[0]+roll<=100)
				{   l=A[0];
                    A[0]+=roll;
                    path_pro(&A[0]);
                }
			}
            while (roll==6)
		   {
                std::cout<<"Player rolled a 6! Extra turn.\n";
                std::cout << "\nPlayer Press 'r' to roll: ";
            char ch;
            std::cin>>ch;
            while (ch!='r')
			{
                std::cout << "Press 'r' to roll: ";
                std::cin >> ch;
            }
                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(A[0]+roll<=100)
				{
                    A[0]+=roll;
                    path_pro(&A[0]);
                }
            }
            // computer
            std::cout<<" Computer's Chance\n";
             roll = dice();
            std::cout << "Computer rolled: " << roll << "\n";
            if (c + roll > 100) 
			{
                std::cout << "Can't move. Need exact roll.\n";
                continue;
            }
            l=c;
            c+=roll;
            path_pro(&c);
            while((c-l)>6)
            {
                std::cout<<"Computer Has Got up A ladder!! Extra turn.\n";

                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(c+roll<=100)
				{   l=c;
                    c+=roll;
                    path_pro(&c);
                }
			}
            while (roll==6)
		   {
                std::cout<<"Computer rolled a 6! Extra turn.\n";

                roll=dice();
                std::cout<<"Extra roll: "<<roll<<"\n";
                if(c+roll<=100)
				{
                    c+=roll;
                    path_pro(&c);
                }
            }
            if(A[0]==100)
			{
                std::cout<<"Player  wins! \n";
                k=1; 
            }
            else if(c==100)
            {
            	std::cout<<"Computer Won\n";
            	k=1;
			}
			else
			{
                std::cout<<"Player is at position: "<<A[0]<<"\n";
                std::cout<<"Computer is at position: "<<c<<"\n";
            }	
	 }while(k!=1);
	}
        std::cout<<"\nGame Over! Play again? (y/n): ";
        std::cin>>playAgain;
        std::cout<<"Change number of players? press y: ";
        std::cin>>changePlayers;

    }while(playAgain == 'y' || playAgain == 'Y');
    return 0;
}
