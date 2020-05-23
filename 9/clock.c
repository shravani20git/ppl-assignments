#include <stdio.h> 
#include <stdlib.h>
#include <pthread.h> 
#include <semaphore.h> 
#include <unistd.h> 
  
sem_t mutex; 

int hrs;
int min;
int sec;
int hflag = 0;
int mflag = 0;
void* thread(void* arg) 
{ 
    //wait
    
    if(!mflag){
	    sem_wait(&mutex);
    }
    else{
    	sleep(1);
	++min;
	printf("%02d : %02d : %02d\n ",hrs,min,sec);
       

	if(min==5){
	min = 0;
	mflag = 0;
	hflag = 1;
	
	}
	mflag=0;
    	
    }  
  
    //critical section 
    //signal  
 
    sem_post(&mutex); 
    return 0;
}
void* thread2(void* arg)
{
    //wait
    
    if(hflag==1 ||  mflag ==1 ){
            sem_wait(&mutex);
    }
    else{
        sleep(1);
	++sec;
      printf("%02d : %02d : %02d \n",hrs,min,sec);
      
        if(sec==5){
        sec = 0;
        mflag = 1;

        }

    }

    //critical section
    //signal
    sem_post(&mutex);
    return 0;
}

void* thread3(void* arg)
{
    //wait
  
    if(!hflag){
            sem_wait(&mutex);
    }
    else{
        sleep(1);
	hrs= hrs + 1;
         printf("%02d : %02d : %02d \n",hrs,min,sec);
        mflag = 0;
	hflag = 0;

    }

    //critical section
    //signal

    sem_post(&mutex);
    return 0;
}



  
  
int main() 
{ 
    hrs=min=sec=0;
    sem_init(&mutex, 0, 1);
   while(1){ 
     	   
    pthread_t t1,t2,t3; 
    int cnt =0;
     
   	 pthread_create(&t1,NULL,thread,NULL); 
    
   	 pthread_create(&t2,NULL,thread2,NULL);
	 pthread_create(&t3,NULL,thread3,NULL);


	 
		 pthread_join(t2,NULL);
       		 pthread_join(t1,NULL);
		 pthread_join(t3,NULL);
        
     		   cnt++;
	system("clear"); 
   } 
    sem_destroy(&mutex); 
    return 0; 
} 
