# Storing functions in Python
This is a proof of concept for persistent storage of functions that are created while a program is running,
for example by user input.

I originally had this idea when working on a chat bot, and it was meant to store commands that are created by users
via "!addcom command ...", although I have admittedly not found an actual use-case where storing an entire function
is the solution.

I created this mostly for learning purposes, but go and have fun with it!

The `on_` notation stems from that original idea of using it in a chat bot. The bot I was workign on used that notation
for functions that were to be called when certain events happen. It just stuck with me.
