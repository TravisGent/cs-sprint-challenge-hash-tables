Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

    Hashing functions
    Collision resolution
    Performance of basic hash table operations
    Load factor
    Automatic resizing
    Various use cases for hash tables

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

Hashing functions are functions that take a string and put it into a list of items in a way that is organized for the hashing function to know how to find it very very quickly. It involves turning it into a number and the modulusing it by the length of the list and putting it into that list with the index being the remainder from the modulus. It can really speed up computing time because hashing functions have a O(1) lookup time.

However, sometimes there can be whata are called collisions because the remainder we get from two numbers can be the same therefore putting two items at the same index in our hash list. Whenever this happens, a common way of solving it is by making those items at that index position a singly linked list. This can increase runtime complexity, but overall seems to handle things pretty well.

That is where autimatic resizing comes into play. There are some hashing functions that people have made that automatically determine if there are too many items in our hash list, or too many items in the singly linked lists in our hashing list and will then resize our hash list to better fit everything. Because every item in our list is basically a number, we get way less collisions if the number we are doing our modulus operation on is based on a larger length of the list.

Hash tables can be used to look up items in a list way quicker, simply but turning a list into a hash list, and giving it a key to lookup it finds the item almost instantly.