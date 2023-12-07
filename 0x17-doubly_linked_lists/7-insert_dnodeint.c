#include "lists.h"

/**
 * insert_dnodeint_at_index - main function
 * @h: param 1
 * @idx: param 2
 * @n: param 3
 * Return: address
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *a;
	dlistint_t *b;
	unsigned int k;

	a = NULL;
	if (idx == 0)
		a = add_dnodeint(h, n);
	else
	{
		b = *h;
		k = 1;
		if (b != NULL)
			while (b->prev != NULL)
				b = b->prev;
		while (b != NULL)
		{
			if (k == idx)
			{
				if (b->next == NULL)
					a = add_dnodeint_end(h, n);
				else
				{
					a = malloc(sizeof(dlistint_t));
					if (a != NULL)
					{
						a->n = n;
						a->next = b->next;
						a->prev = b;
						b->next->prev = a;
						b->next = a;
					}
				}
				break;
			}
			b = b->next;
			k++;
		}
	}

	return (a);
}
