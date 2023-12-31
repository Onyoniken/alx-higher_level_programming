#include <stdio.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - main function
 * @p: param 1
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s, alloc, k;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", alloc);

	for (k = 0; k < size; k++)
	{
		type = list->ob_item[k]->ob_type->tp_name;
		printf("Element %ld: %s\n", k, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[k]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[k]);
	}
}

/**
 * print_python_bytes - main function
 * @p: param 1
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s, k;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", s);
	for (k = 0; k < s; k++)
	{
		printf("%02hhx", bytes->ob_sval[k]);
		if (k == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - main function
 * @p: param 1
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
