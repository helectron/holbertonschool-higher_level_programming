#include "lists.h"

/**
 * check_cycle - check if there is a cycle in the linked list 
 * @One: go through the linked list one by one
 * @Two: go through the linked list two by two
 * Return: 1 if there is a cycle, 0 if there is not
*/

int check_cycle(listint_t *list)
{
    listint_t *One = list;
    listint_t *Two = list;

    while (One && Two && Two->next)
    {
	One = One->next;
	Two = Two->next->next;
	if (One == Two)
	{
	    return (1);
	}
	return (0);
    }
}
