#include "lists.h"

/**
 * sum_dlistint - main function
 * @head: param 1
 * Return: NULL
 */
int sum_dlistint(dlistint_t *head)
{
	int a = 0;

	if (head != NULL)
	{
		while (head->prev != NULL)
			head = head->prev;

		while (head != NULL)
		{
			a += head->n;
			head = head->next;
		}
	}
	return (a);
}
