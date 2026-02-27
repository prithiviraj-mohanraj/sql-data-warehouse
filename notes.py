Python List & Tuple Study Notes
1. Adding Multiple Values to a List
There are three main ways to add more than one item at a time.
extend(iterable): Unpacks an iterable (like a list or tuple) and adds each item to the end of the original list.
Example: my_list.extend([4, 5]) 
 [1, 2, 3, 4, 5]
Slice Assignment [i:i]: Inserts items into a specific "gap" without replacing anything.
Example: my_list[1:1] = [10, 20] (Inserts 10 and 20 at index 1).
Concatenation +: Creates a brand new list.
Example: new_list = list1 + list2
2. The "None" Trap (In-Place Methods)
Methods that change the list directly (in-place) do not return the list; they return None.
⚠️ Danger: my_list = my_list.append(4) will wipe out your list and make it None.
✅ Correct: Just write my_list.append(4).
3. CSV Strings to Lists
To add values from a string like "apple,banana,cherry":
Split it: my_str.split(",") creates a list.
Extend it: my_list.extend(my_str.split(",")).
4. Lists vs. Tuples (Mutability)
Feature	List []	Tuple ()
Type	Mutable (Changeable)	Immutable (Fixed)
Methods	append, extend, insert, pop	None (Only count and index)
Changing	Modify the "same box."	Must create a "new box" using +.
5. The "Comma" Rule for Tuples
Because () is used for math, Python needs a comma to recognize a single-item tuple.
(5) 
 Integer
(5,) 
 Tuple
[] 
 List (No comma needed because [] has only one meaning).
6. Slice Assignment Secrets
To Insert: my_list[2:2] = ["new"] (Inserts "new" at index 2).
To Replace: my_list[1:4] = ["Bonus"] (Deletes items at 1, 2, 3 and puts "Bonus" there).
To Delete: del my_list[1:3] (Removes a range of items).
7. Removing Items
.pop(index): Removes item by position and "hands it to you" (returns it).
.remove(value): Removes item by name (finds the first "Apple" and deletes it).
del list[index]: A keyword that deletes by position but returns nothing.
Comparison Summary
Task	Use This	Example
Add 1 item to end	append()	l.append(5)
Add many items to end	extend()	l.extend([5, 6])
Add 1 item in middle	insert()	l.insert(1, "Hi")
Add many in middle	Slice [i:i]	l[1:1] = [1, 2]
Combine two lists	+ operator	l3 = l1 + l2
