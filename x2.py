# -*- coding: utf-8 -*-
import os
import sys
import fileinput
import linecache
import pdb
 
class Insert_line(object):
 
    def __init__(self, file, keyword, newline):
        self.__file = file
        self.__key = keyword
        self.__newline = newline
 
    def _get_specify_lineno(self):   #get line num of gBS->allocate
        i = 1
        arr=[]
        try:
            f = open("%s" % self.__file)
        except IOError,e:
            print e[1] + ' "%s"' % e.filename
            sys.exit(1)
        while True:
            line = f.readline()
            if not line: break
            if "%s" % self.__key in line:
                arr.append(i)        #store line num to list
            i += 1
        f.close()
        print(arr)
        return arr
 
    def _inserted_newline_list(self):

       # if self._get_specify_lineno():
           
            ls = os.linesep   # 换行符
            f = open("%s" % self.__file)
            li = f.readlines() # get all content in f , seems like store it to mem
            f.close()
            cup = self._get_specify_lineno()
            j=0
            for i in cup:
               # line = getline("%s" % self.__file,i)
                print (li[i-1+j]+ "|")
                #pdb.set_trace()
                if "\\" not in li[i-1+j]:
                    li.insert(i+cup.index(i), self.__newline + ls )
                    j+=1
                    print ("no mark!")
                else:
                    li.insert(i+cup.index(i)+1, self.__newline + ls ) # 加入一行后，往下一匹配行插入debug 时 ，插入位置要加一
                    j+=1
                    print ("has mark")
            return li
 
    def inserted_new_file(self):
        if self._inserted_newline_list():
            lines = self._inserted_newline_list()
            #os.system("cp %s %s.bak" % (self.__file, self.__file))
            f = open("%s" % self.__file, 'w')
            f.writelines(lines)
            f.close()
        else:
            print 'No such keyword "%s"' % self.__key

def checktype(f):             #筛选c文件  
    return f.endswith('.c')
'''
def getline(the_file_path, line_number):
    f = open(the_file_path, 'rU')
    if line_number < 1:
        return ''
    for cur_line_number, line in enumerate(f):
        if cur_line_number == line_number-1:
          #pdb.set_trace()
          f.close()
          return line
    return ''
'''
def _main():
    #os.chdir("D:\\Project\\AMD\\ReferenceBuildRome_origin\\LenovoCorePkg")
    path = os.getcwd()
    print (os.listdir(path))
    for dir,folder,files in os.walk(path):
        for i in files:
            f=(os.path.join(dir,i))
            if (checktype(f)== False):
                continue
 
            file = Insert_line(f, "gBS->AllocatePool", '''\tDEBUG((EFI_D_ERROR,"%a:%d\\n",__FUNCTION__,__LINE__));''')
            file.inserted_new_file()
if __name__ == "__main__":
    _main()
