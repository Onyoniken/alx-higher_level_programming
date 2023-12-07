#include "lists.h"

/**
 * add_dnodeint_end - main function
 * @head: param 1
 * @n: param 2
 * Return: address
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *b;
	dlistint_t *a;

	a = malloc(sizeof(dlistint_t));
	if (a == NULL)
		return (NULL);

	a->n = n;
	a->next = NULL;

	b = *head;

	if (b != NULL)
	{
		while (b->next != NULL)
			b = b->next;
		b->next = a;

	}
	else
	{
		*head = a;
	}

	a->prev = b;

	return (a);
}
