import argparse
import re

TASKS_FILE = "day-40/project/tasks.txt"


def load_tasks(path):
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            done_flag, text = line.split("|", 1)
            yield {"done": done_flag == "1", "text": text}


def save_tasks(path, tasks):
    with open(path, "w") as file:
        for task in tasks:
            done_flag = "1" if task["done"] else "0"
            file.write(f"{done_flag}|{task['text']}\n")


def format_task(index, task):
    status = "x" if task["done"] else " "
    return f"[{status}] {index}: {task['text']}"


def cmd_add(args):
    tasks = list(load_tasks(TASKS_FILE))
    text = " ".join(args.text)
    tasks.append({"done": False, "text": text})
    save_tasks(TASKS_FILE, tasks)
    print(f"Added: {text}")


def cmd_list(args):
    tasks = list(load_tasks(TASKS_FILE))
    if not tasks:
        print("No tasks yet.")
        return

    shown = 0
    for index, task in enumerate(tasks):
        if args.pending and task["done"]:
            continue
        if args.done and not task["done"]:
            continue
        print(format_task(index, task))
        shown += 1

    if shown == 0:
        print("No tasks match that filter.")


def cmd_done(args):
    tasks = list(load_tasks(TASKS_FILE))
    if args.index < 0 or args.index >= len(tasks):
        print(f"No task at index {args.index}")
        return

    tasks[args.index]["done"] = True
    save_tasks(TASKS_FILE, tasks)
    print(f"Marked done: {tasks[args.index]['text']}")


def cmd_search(args):
    tasks = list(load_tasks(TASKS_FILE))
    pattern = re.compile(args.pattern, re.IGNORECASE)
    found = False
    for index, task in enumerate(tasks):
        if pattern.search(task["text"]):
            print(format_task(index, task))
            found = True

    if not found:
        print("No matching tasks.")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple command-line task manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", nargs="+", help="The task description")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--pending", action="store_true", help="Show only pending tasks")
    list_parser.add_argument("--done", action="store_true", help="Show only completed tasks")
    list_parser.set_defaults(func=cmd_list)

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("index", type=int, help="The task's index, from 'list'")
    done_parser.set_defaults(func=cmd_done)

    search_parser = subparsers.add_parser("search", help="Search tasks with a regex pattern")
    search_parser.add_argument("pattern", help="A regular expression to search task text")
    search_parser.set_defaults(func=cmd_search)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
