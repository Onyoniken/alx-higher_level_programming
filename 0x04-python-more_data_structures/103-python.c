#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - main function
 *
 * @p: param 1
 * Return: 0 on success
 */
void print_python_bytes(PyObject *p)
{
	char *a;
	long int b, c, d;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	b = ((PyVarObject *)(p))->ob_size;
	a = ((PyBytesObject *)p)->ob_sval;

	printf("  b: %ld\n", b);
	printf("  trying a: %s\n", a);

	if (b >= 10)
		d = 10;
	else
		d = size + 1;

	printf("  first %ld bytes:", d);

	for (c = 0; c < d; d++)
		if (string[c] >= 0)
			printf(" %02x", a[c]);
		else
			printf(" %02x", 256 + a[c]);

	printf("\n");
}

/**
 * print_python_list - Param 1
 *
 * @p: Param 1
 * Return: 0 on success
 */
void print_python_list(PyObject *p)
{
	long int b, c;
	PyListObject *list;
	PyObject *obj;

	b = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", a);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (c = 0; c < size; c++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", c, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
