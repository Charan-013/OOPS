class STask:
    def __init__(self, taskID, Title, desp, dueDate, priority):
        self.taskID = taskID
        self.title = Title
        self.description = desp
        self.dueDate = dueDate
        self.priority = priority
        self.isCompleted = False

    def mark_Completed(self):
        self.isCompleted = True

    def update_Task(self, taskID, Title, desp, dueDate, priority):
        self.taskID = taskID
        self.title = Title
        self.description = desp
        self.dueDate = dueDate
        self.priority = priority

    def get_task_details(self):
        if self.isCompleted == True:
            status = "Completed"
        else:
            status = "Pending"
        return f"{self.taskID}. [{status}] {self.title} - Due: {self.dueDate}, Priority: {self.priority}"
        


class toDoList:
    def __init__(self):
        self.tasks = []

    def addTask(self, Task):
        taskID, Title, desp, dueDate, priority = map(str, Task)
        self.tasks.append(STask(taskID, Title, desp, dueDate, priority))

    def removeTask(self, taskID):
        new = []
        for ele in self.tasks:
            if int(ele.taskID) != int(taskID):
                # print(ele.taskID)
                new.append(ele)
        self.tasks = new
        # print(ele.get_task_details for ele in new)


    def get_AllTask(self):
        allTasks = []
        for ele in self.tasks:
            allTasks.append(ele.get_task_details())
        return allTasks

    def get_PendingTasks(self):
        pending = []
        for ele in self.tasks:
            if ele.isCompleted == False:
                pending.append(ele.get_task_details())
        return pending

    def get_CompletedTasks(self):
        completed = []
        for ele in self.tasks:
            if ele.isCompleted == True:
                completed.append(ele.get_task_details())
        return completed

    def sort_Task(self, condition):
        if condition == "due_date":
            self.tasks.sort(key=lambda x: x.dueDate)
        elif condition == "priority":
            self.tasks.sort(key=lambda x: x.priority)
            
        

    def searchTask(self, s):
        lower = s.lower()
        found = []
        for ele in self.tasks:
            if lower in ele.title.lower() or lower in ele.description.lower():
                found.append(ele.get_task_details())
        return found

def todolist():
    tdl = toDoList()

    while True:
        try:
            inp = input().strip()

            if not inp:
                break

            if inp.startswith("add_task"):
                inp = inp.split("add_task")
                inp = eval(inp[1])
                a = tdl.addTask(inp)

            elif inp.startswith("update_task"):
                inp = inp.split("update_task")
                inp = eval(inp[1])

                for ele in tdl.tasks:
                    if int(ele.taskID) == int(inp[0]):
                        ele.update_Task(inp[0],inp[1],inp[2],inp[3],inp[4])

            elif inp.startswith("get_all_tasks"):
                all = tdl.get_AllTask()
                print("All Tasks:")
                for ele in all:
                    print(ele)
                print()

            elif inp.startswith("get_completed_tasks()"):
                completed = tdl.get_CompletedTasks()
                print("Completed Tasks:")
                for ele in completed:
                    print(ele)
                print()

            elif inp.startswith("get_pending_tasks()"):
                pending = tdl.get_PendingTasks()
                print("Pending Tasks:")
                for ele in pending:
                    print(ele)
                print()

            elif inp.startswith("mark"):
                inp = inp.split("mark_completed")
                inp = int(eval(inp[1]))
                for ele in tdl.tasks:
                    # print(ele.taskID)
                    if int(ele.taskID) == inp:
                        ele.mark_Completed()
                        # print("changed")
                # m = STask.mark_Completed(inp)

            elif inp.startswith("remove_task"):
                inp = inp.split("remove_task")
                inp = eval(inp[1])
                tdl.removeTask(inp)

            elif inp.startswith("sort_tasks"):
                inp = inp.split("sort_tasks")
                inp = eval(inp[1])
                tdl.sort_Task(inp)
                all = tdl.get_AllTask()
                print("All Tasks:")
                for ele in all:
                    print(ele)
                print()

            elif inp.startswith("search_tasks"):
                inp = inp.split("search_tasks")
                inp = eval(inp[1])
                print(f"Search Results for: {inp}")
                l = tdl.searchTask(inp)
                for ele in l:
                    print(ele)
                print()

        except EOFError:
            break


if __name__ == "__main__":
    todolist()
