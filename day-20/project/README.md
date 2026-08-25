# Contact Book — Day 20 mini-project

A command-line contact book: add, list, search, and delete contacts, persisted
to a plain text file between runs.

## Setup

Nothing beyond the repo's root setup (see the [root README](../../README.md)) —
this project uses only the Python standard library, no extra packages.

## Run it

From the **repository root**:

```bash
python day-20/project/contact_book.py
```

Contacts are stored one per line in [`contacts.txt`](contacts.txt) as
`name,phone,email`, and the app ships with two sample contacts already in
there. Every time you choose **Quit**, the current in-memory list of contacts
is written back to that file, so changes persist across runs.

## Sample session

```
1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit
Choose an option: 2
Ada Lovelace | 555-0100 | ada@example.com
Grace Hopper | 555-0200 | grace@example.com

1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit
Choose an option: 1
Name: Alan Turing
Phone: 555-0300
Email: alan@example.com
Added Alan Turing.

1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit
Choose an option: 3
Search for: grace
Grace Hopper | 555-0200 | grace@example.com

1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit
Choose an option: 5
Contacts saved. Goodbye!
```

## How it's built

- `load_contacts()` / `save_contacts()` — read and write `contacts.txt`, one
  contact per line, using `with` (Day 18).
- `add_contact()`, `list_contacts()`, `search_contacts()`, `delete_contact()` —
  each takes the in-memory `contacts` list (Day 11) of dicts (Day 13) and does
  one job.
- `main()` — a menu loop (Day 7's `while True:` + Day 6's `if`/`elif`) that
  dispatches to the right function based on user input (Day 5).

This is deliberately a flat, single-file script with plain functions — no
classes yet. You'll rebuild something in this shape with proper OOP starting
[Day 21](../../day-21/README.md).

## Stretch goal

Pick one (or more) to extend the project once the core works:

- **Duplicate prevention**: refuse to add a contact whose name already exists
  (case-insensitive), and tell the user instead.
- **Edit in place**: add a menu option to update an existing contact's phone or
  email without deleting and re-adding it.
- **Sorted listing**: make `list_contacts()` print contacts alphabetically by
  name using `sorted()` (Day 11) instead of file order.
- **Multiple search fields**: extend `search_contacts()` to also match against
  phone and email, not just name.
