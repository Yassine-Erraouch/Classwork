let taskInput = document.querySelector('#taskInput');





// initiating tasks array
let tasks = localStorage.getItem('tasks')? JSON.parse( localStorage.getItem('tasks')): [];





// localStorage.clear()




console.log(tasks);
// displayTasks(): fucntion to display tasks
let displayTasks = () => {
    let taskContainer = document.querySelector('#taskContainer');

    let tasksToDisplay = tasks.map((task)=> 
    `<div class="border border-primary border-1 rounded d-flex flex-row justify-content-between align-items-center p-3 ">
        <p  class="fs-5" id='${task.id}'>${task.name}</p>
        <div class="">
            <button class="btn" id="" onclick="complete(${task.id})">
                <i class="fa-solid fa-check text-success fs-4"></i>
            </button>

            <button class="btn btn-" id="" onclick="remove(${task.id})">
                <i class="fa-solid fa-xmark text-danger fs-4"></i>
            </button>
        </div>
    </div>`).join('');

    taskContainer.innerHTML = tasksToDisplay;
}



// addTask(): fucntion to add tasks
let addTask = () => {
    let taskName = taskInput.value;
    if(taskName == "") {
        alert('Please enter a task.')
        return;
    };
    
    let task = {id:tasks.length > 0? tasks.lenght +1 : 0, name: taskName , complete: false};
    
    // updating tasks the array and local storage
    tasks.push(task);
    localStorage.setItem('tasks', JSON.stringify(tasks));

    displayTasks(); 
}


// complete(task.id): function to mark a task as complete
let complete = (id) => {
    let task = tasks.find((task) => task.id == id);
    if (task) {
        task.complete = !task.complete;
        let taskElement = document.getElementById(id);
        if (taskElement) {
            taskElement.style.textDecoration = task.complete ? 'line-through' : 'none';
        }
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };
};

let remove = (id) => {
    let task = tasks.find((task) => task.id == id);
    if (confirm('Are you sure you want to remove this task?')) {
        tasks.pop(task);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        alert('Task deleted successfully!')
    }
}








// Displaying tasks on load
displayTasks();
