#include "lists.h"

/**
 * check_cycle - main function
 * @list: param 1
 *
 * Return: 1 on success , 0 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
		return (0);

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
		return (1);
	}
	return (0);
}
