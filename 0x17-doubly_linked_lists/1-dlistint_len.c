#include "lists.h"

/**
 * dlistint_len - main function
 * @h: param 1
 * return: node numbers
 */
size_t dlistint_len(const dlistint_t *h)
{
	int a = 0;

	if (h == NULL)
		return (a);
	while (h->prev != NULL)
		h = h->prev;
	while (h != NULL)
	{
		a++;
		h = h->next;

	}
	return (a);
}
