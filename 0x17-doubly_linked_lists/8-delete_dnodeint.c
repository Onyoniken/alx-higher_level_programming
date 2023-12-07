#include "lists.h"

/**
 * delete_dnodeint_at_index - main function
 * @head: param 1
 * @index: param 2
 * Return: 1 on success, 0 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *a;
	dlistint_t *b;
	unsigned int k;

	a = *head;

	if (a != NULL)
		while (a->prev != NULL)
			a = a->prev;

	k = 0;

	while (a != NULL)
	{
		if (k == index)
		{
			if (k == 0)
			{
				*head = a->next;
				if (*head != NULL)
					(*head)->prev = NULL;
			}
			else
			{
				b->next = a->next;

				if (a->next != NULL)
					a->next->prev = b;
			}

			free(a);
			return (1);
		}
		b = a;
		a = a->next;
		k++;
	}

	return (-1);
}
