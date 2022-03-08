#include <unistd.h>
#include <string.h>
#include <dirent.h>
#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>

void printdir(const char *dir, int depth)
{
    DIR *dp;
    struct dirent *entry;
    struct stat statbuf;
    dp=opendir(dir);

    if (dp==NULL) {
        fprintf(stderr,"not open directory: %s\n",dir);
        return;
    }
    chdir(dir);
    while((entry=readdir(dp))!=NULL) {
        lstat (entry->d_name,&statbuf);
        if (S_ISDIR (statbuf.st_mode)) {
            if (strcmp(".",entry->d_name)  ==0 ||
                    strcmp("..",entry->d_name) ==0 )
                continue;
            printf("%*s%s /\n",depth, " ",entry->d_name);
            printdir(entry->d_name,depth+4);
        }
        else 
            printf("%*s%s\n",depth," ",entry->d_name);
    }
    chdir("..");
    closedir(dp);
}

int main()
{
    printf("Directory san of /home:\n*");
    printdir("/home/wzp/git/",0);
    printf("Done.\n");
    exit(0);
}

    
