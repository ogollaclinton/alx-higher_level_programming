#include <object.h>
#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int a;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;


	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
