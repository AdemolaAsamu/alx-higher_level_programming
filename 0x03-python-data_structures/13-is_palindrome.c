#include "list.h"
/**
 * is_palindrome - Checks if a list is a palindrome
 * @head: double pointer to head list
 * Return: returns 0 for true instances and 0 for otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *lists;
	int holder, idx, av, ar;

	lists = *head;
	idx = 0;
	av = 0;
	if (*head == NULL)
		return (1);
	while (lists != NULL)
	{
		holder[idx] = holder->n;
		idx += 1;
		holder = holder->next;
	}
	if (idx == 1)
		return (1);
	ar = idx - 1;
	while (av < idx / 2)
	{
		if (holder[av] != holder[ar])
			return (0);
		ar -= 1;
		av += 1;
	}
	return (1);
}
