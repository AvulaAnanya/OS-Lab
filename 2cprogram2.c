#include<stdio.h>

#include<unistd.h>



int main()

{

    int i;



    printf("I am EXEC.c called by execv() ");

    printf("\n");

    return 0;

}





//execDemo.c



#include<stdio.h>

#include<stdlib.h>

#include<unistd.h>

int main()

{

        //A null terminated array of character

        //pointers

        char *args[]={"./EXEC",NULL};

        execv(args[0],args);



        /*All statements are ignored after execvp() call as this whole

        process(execDemo.c) is replaced by another process (EXEC.c)

        */

        printf("Ending-----");



    return 0;

}