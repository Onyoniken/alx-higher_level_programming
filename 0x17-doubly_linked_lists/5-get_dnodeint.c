#include "lists.h"

/**
 * get_dnodeint_at_index - main function
 * @head: param 1
 * @index: param 2
 * @index: param 3
 * Return: 0
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int a;
	dlistint_t *b;

	a = 0;
	if (head == NULL)
		return (NULL);

	b = head;
	while (b)
	{
		if (index == a)
		return (b);
		a++;
		b = b->next;
	}
	return (NULL);
}
