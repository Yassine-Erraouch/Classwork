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
        `<div class="row d-flex align-items-center">
            <div class="col">
                <input type="checkbox" name="" id="" class="form-check-input"  onclick="changeState" id="c${task.id}>
            </div>

            <div class="col" id="t${task.id}">
                ${task.name}
            </div>

            <div class="col">
                ${task.date}
            </div>


            <div class="col text-end">
                <button class="btn btn-secondary" onclick="editTask('${task.name}')"><i class="fa-solid fa-pen-to-square"></i></button>
                <button class="btn btn-danger" onclick="deleteTask('${task.name}')"><i class="fa-solid fa-trash-can"></i></i></button>
            </div>
        </div>`
    };
};

let clearAndFocus = () => {
    let taskInput = document.querySelector("#taskName");
    taskInput.value = '';
    taskInput.focus();
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
        clearAndFocus();
    }
    tasks.push({id: tasks.length?tasks.length +1: 1, name: taskName, done: false, date: new Date()});
    localStorage.setItem('tasks', JSON.stringify(tasks));
    displayTasks();

    clearAndFocus();
   
};

let deleteTask = (taskName) => {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }
    tasks = tasks.filter(task => task.name !== taskName);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    // displaying the tasks after all the operations are performed
    displayTasks();
};

// defining the buttons
let saveBtn = document.querySelector('#saveBtn');
let cancelBtn = document.querySelector('#cancelBtn');
let addBtn = document.querySelector('#addBtn');

// fucntion to show btns
let ShowBtns = () => {
    saveBtn.classList.remove('d-none');
    cancelBtn.classList.remove('d-none');
    addBtn.classList.add('d-none');   
}

// function to hide btns
let hideBtns = () => {
    addBtn.classList.remove('d-none');
    saveBtn.classList.add('d-none');
    cancelBtn.classList.add('d-none');
}

// let toggleBtns = () => {
    
//     //toggling the buttons
//     if(addBtn.classList.contains('d-none')) {
//         addBtn.classList.remove('d-none');
//         saveBtn.classList.add('d-none');
//         cancelBtn.classList.add('d-none');
//     } else {
//         saveBtn.classList.remove('d-none');
//         cancelBtn.classList.remove('d-none');
//         addBtn.classList.add('d-none');
//     }
   
// }


let editTask = (taskName) => {
    let taskInput = document.querySelector('#taskName');
    let saveBtn = document.querySelector('#saveBtn');
    let cancelBtn = document.querySelector('#cancelBtn');
    let addBtn = document.querySelector('#addBtn');
    // // showing the save and cancel buttons and hiding the add button
    // saveBtn.classList.remove('d-none');
    // cancelBtn.classList.remove('d-none');
    // addBtn.classList.add('d-none');


    ShowBtns();
    
    let task = tasks.find(task => task.name === taskName);
    taskInput.value = task.name;

    // adding an event listener to the save button;
    saveBtn.addEventListener('click', ()=> {
        task.name = taskInput.value;
        task.date = (new Date()).toLocaleString();
        localStorage.setItem('tasks', JSON.stringify(tasks));
        clearAndFocus();
        displayTasks();
    });

    cancelBtn.addEventListener('click', ()=> {
        hideBtns();
        clearAndFocus();
        displayTasks();
    })


};






displayTasks();





