#include "lists.h"
/**
 *check_cycle - checks if there is a loop
 *@list: head of list
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *quick = NULL;
	listint_t *slow = NULL;

	if (list == NULL)
		return (0);
	quick = list->next;
	slow = list;
	while (quick && quick->next != NULL)
	{
		if (quick == slow)
			return (1);
		quick = quick->next->next;

		slow = slow->next;
	}
	return (0);
}
