import sys
import os
import time
from multiprocessing import Process

def make_branch(dir_l0,n):
    total=0
    ldir='long_directory_name_long_directory_name_long_directory_name_long_directory_name_long_directory_name'
    dir_start_str='C:/tmp/dir10m/'+dir_l0+str(n)+'/'
    os.mkdir(dir_start_str)

    for i in range(10):
        dir_l1='dir'+str(i)+'/'
        os.mkdir(dir_start_str+dir_l1)
        print('directory',i,':', total)
        for j in range(10):
            dir_l2=ldir+str(j)+'/'
            os.mkdir(dir_start_str+dir_l1+dir_l2)
            #time.sleep(0.2)
            for k in range(10):
                dir_l3=ldir+str(k)+'/'
                os.mkdir(dir_start_str+dir_l1+dir_l2+dir_l3)
                for l in range(10):
                    dir_l4=ldir+str(l)+'/'
                    os.mkdir(dir_start_str+dir_l1+dir_l2+dir_l3+dir_l4)
                    for m in range(100):
                        total+=1
                        fname='long_file_name_long_file_name_long_file_name_long_file_name_long_file_name_long_file_name_long_file_name.'+str(m)
                        #os.system('touch '+dir_start_str+dir_l1+dir_l2+dir_l3+dir_l                                                                                                                                                             4+fname3#
                        f=open(dir_start_str+dir_l1+dir_l2+dir_l3+dir_l4+fname,"w")
                        f.close()
                        
    return total

start=time.time()
#print(make_branch('dir',2),'files created.')
#print(round(time.time()-start),2)
#print('The end.')
#exit()
print(__name__)
if __name__ == '__main__':
    procs=[]
    branches=int(sys.argv[1])
    #branches=10
    for n in range(branches):
        proc = Process(target=make_branch, args=('dir',n))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()