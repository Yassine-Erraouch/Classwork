let tasks;
$.ajax({
    url:"https://jsonplaceholder.typicode.com/todos",
    type: 'GET',
    dataType: 'json',
    success: function(data) {
        tasks = data;
        console.log(tasks);

        // display tasks;
        showTasks();








    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.log('Bruh!', textStatus, errorThrown);
    }
});



function showTasks() {
    if(tasks) {
        $("#display").html("");
    $.each(tasks, function(index, task) {
        $("#display").append(`
            <tr>
                <td>${task.id}</td>
                <td>${task.title}</td>
                <td>${task.completed}</td>
                <td>
                    <button class="btn btn-danger">Delete</button>
                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#taskModal">Edit</button>
                </td>
                
            </tr>
        `);
    });
    }
    
}