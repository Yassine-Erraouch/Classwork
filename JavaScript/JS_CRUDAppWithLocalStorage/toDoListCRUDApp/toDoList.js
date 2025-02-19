// creating an array to contain the tasks
let tasks = localStorage.getItem('tasks')? JSON.parse(localStorage.getItem('tasks')) : [];


// function to display the tasks
let displayTasks = () => {
    let taskList = document.querySelector('#taskList');
    if (!tasks.length) {
        taskList.classList.add('d-none');
        return;
    }
    taskList.classList.remove('d-none');

    taskList.innerHTML = '';
    for (let task of tasks) {
        taskList.innerHTML += 
        `<div class="row">
            <div class="col-auto">
                <input type="checkbox" name="" id="" class="form-check-input" ${task.done? 'checked' : ''}>
            </div>

            <div class="col">
                ${task.name}
            </div>

            <div class="col">
                <button class="btn btn-secondary" onclick="editTask('${task.name}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button class="btn btn-danger" onclick="deleteTask('${task.name}')"><i class="fa-solid fa-trash-can"></i></i></button>
            </div>
        </div>`
    };
};



let addTask = () => {
    let taskName = document.querySelector('#taskName').value;
    let taskList = document.querySelector('#taskList');

    if (!taskName) {
        return;
    }
    if (tasks.find(task => task.name === taskName)) {
        alert('Task already exists');
        return;
    }
    tasks.push({name: taskName, done: false, date: new Date()});
    localStorage.setItem('tasks', JSON.stringify(tasks));
    taskName.value = '';
    displayTasks();
}

let deleteTask = (taskName) => {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }
    tasks = tasks.filter(task => task.name !== taskName);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    displayTasks();
}

let editTask = (taskName) => {
    let task = tasks.find(task => task.name === taskName);
    let taskNameInput = document.querySelector('#taskName');
    taskNameInput.value = task.name;
    taskNameInput.focus();
    
}


displayTasks();





