#include "lists.h"

/**
 * free_dlistint - main function
 * @head: param 1
 * Return: 0
 */
void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
	return;

	while (head->next)
	{
		head = head->next;
		free(head->prev);
	}
	free(head);
}
