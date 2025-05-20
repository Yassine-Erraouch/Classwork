async function fetchData() {
  let data;
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos');
    data = await response.json();
    
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
}

let data = fetchData();

// stocking the first 20 todos in a new array;
let todos;
data.then(data =>{
    todos = data.slice(0, 20);
    loadTasks();

});

// displaying the todos in the table
let table = document.querySelector('#displayTasks');
function loadTasks() {
    table.innerHTML = '';
    table.innerHTML = todos.map((todo, index)=> `
     <tr>
        <td>${todo.userId} </td>
        <td>${todo.id} </td>
        <td>${todo.title} </td>
        <td>${todo.completed ? 'Completed' : 'Pending'} </td>
        <td> 
            <button class="btn btn-secondary" id="show">Show</button>
            <button class="btn btn-primary" id="edit" onclick="editTask(${index})">Edit</button>
            <button class="btn btn-danger" id="delete" onclick="deleteTask(${index})" onclick="confirm('Are you sure?')">Delete</button>
        </td>
    </tr>
    `)
};

let button = document.querySelector('#addOrEdit');
let form = document.querySelector('#addTaskForm');
let title = document.querySelector('#title');
let statusSelect = document.querySelector('#status');
function editTask(index) {
    button.textContent = 'Edit Task';
    form.classList.remove('d-none');
    title.value = todos[index].title;
    statusSelect.value = todos[index].completed ? 1 : 2;
    
}



loadTasks();