class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# Quicksort na listach
# Można między innymi zrobić to tak
# Kod ma raka, bo nie miałem czasu tego zrobić ładnie
# Jest to opcja która nie wykonuje żadnych nadmiarowych przejść po listach, ale przez to przekazuje dużo wskaźników
def partition_list(head, tail): # Partition będzie zwracało 3 listy 
    pivot=head #Bierzemy pierwszy element jako pivot
    head=head.nextval
    pivot.next=None #Ważne! Ustawiamy jego następny element jako
    head_left=Node() # Tworzymy wartowników
    head_right=Node()
    tail_left, tail_right=head_left,head_right #Wskaźniki na końce list
    while(head):
        p,head=head,head.nextval
        if(p.dataval<=pivot.dataval): #Jeśli element jest mniejszy bądź równy leci do lewej listy (na koniec)
            tail_left.nextval=p
            tail_left=p
        else: #inaczej leci do prawej listy (na koniec)
            tail_right.nextval=p
            tail_right=p
    tail_left.nextval,tail_right.nextval=None,None # Usuwamy wskazania ostatnich elementów list
    head_left,head_right=head_left.nextval,head_right.nextval # Usuwamy wartowników
    return head_left,tail_left,pivot,head_right,tail_right
#     Tutaj chodzi o to, że zwracamy listę elementów mniejszych, pivot i listę większych elementów


        
def quick_sort_list(head, tail):
    if(head and not tail==head):
        head_left,tail_left,pivot,head_right,tail_right=partition_list(head, tail) #Wywołujemy partition
        head_left,tail_left=quick_sort_list(head_left,tail_left) #wywołujemy quicksort na lewej części
        head_right,tail_right=quick_sort_list(head_right,tail_right) #wywołujemy quicksort na prawej części
        if(head_left): #Jeśli lewa część nie jest pusta to je łączymy
            tail_left.nextval=pivot
            head=head_left
        if(head_right): #Jeśli prawa część nie jest pusta to je łączymy
            pivot.nextval=head_right
            tail=tail_right
            tail.nextval=None
    return head, tail #quick_sort zwraca początek i koniec listy