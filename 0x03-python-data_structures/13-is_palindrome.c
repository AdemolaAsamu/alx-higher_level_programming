#include "lists.h"
/**
 * is_palindrome - Checks if a list is a palindrome
 * @head: double pointer to head list
 * Return: returns 0 for true instances and 0 for otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int holder[2000];
	int idx, av, ar;

	current = *head;
	idx = 0;
	av = 0;
	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		holder[idx] = current->n;
		idx += 1;
		current = current->next;
	}
	if (idx == 1)
		return (1);
	ar = idx - 1;
	while (av < (idx / 2))
	{
		if (holder[av] != holder[ar])
			return (0);
		ar -= 1;
		av += 1;
	}
	return (1);
}
