
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>


#include <python3.8/Python.h>


#define PY_SSIZE_T_CLEAN


int main(int argc, char **argv)
{
	printf("this is start........\n");
	Py_Initialize();
	PyObject *tuple, *list;

	tuple=Py_BuildValue("(iss)",1,2,"three");
	list=Py_BuildValue("[iss]",1,2,"three");


	Py_Finalize();
	printf("end ........\n");
	return 0;
	
}




