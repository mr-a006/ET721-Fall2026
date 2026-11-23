// load all tasks
function loadTasks() {
    fetch("/get_tasks")
        .then(response => response.json())
        .then(tasks => {
            const list = document.querySelector("#taskList");
            list.innerHTML = "";

            tasks.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.task;
                li.classList.add("task_item");
                list.appendChild(li);

                // create delete button for each task
                const btn = document.createElement("button");
                btn.innerHTML = "&#10060;"; // unicode for a cross mark
                btn.classList.add("btndeletetask");
                btn.onclick = () => {
                    fetch("/delete_task", {
                        method: "POST",
                        headers: {"Content-Type" : "application/json"},
                        body: JSON.stringify({id : task.id})
                    })
                    .then(() => loadTasks());
                };
                li.appendChild(btn);
            });
        });
}
// load all tasks when the page loads
window.onload = loadTasks

function addtask(){
    const inputtask = document.querySelector("#taskInput")
    const task = inputtask.value.trim()

    if (task === "") return;

    fetch("/add_task",{
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({task : task})
    })
    .then(()=>{
        inputtask.value = ""
        loadTasks()
    })
}