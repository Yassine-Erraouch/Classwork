    // native JS version

    // function to display student info in the table;
let loadDisplay = () => {
    document.querySelector('#studentsDisplay').innerHTML = students.map((student, i) => `
    <tr>
        <td>${student.cef} </td>
        <td>${student.fullName} </td>
        <td>${student.major} </td>
        <td><img src="${student.photo}" alt=""></td>
        <td>
            <button id="editBtn" class='btn btn-secondary' onclick="editStudent(${i})">🖋️</button>
            <button id="deleteBtn" class='btn btn-danger' onclick="deleteStudent(${i})">🗑️</button>
        </td>
    </tr>`).join('');
}

// getting the data from the json file
let students;
const getData = async () => {
    const response = await fetch('students.json');
    students = await response.json();
    loadDisplay(); // display info after fetching it
}
let form = document.querySelector('#infoForm');

document.querySelector("#addBtn").addEventListener('click', () => {
    form.classList.remove('d-none');
});

document.querySelector("#cancelBtn").addEventListener('click', () => {
    form.classList.add('d-none');
})

let saveStudent = () => {
    let student = {
        cef: document.querySelector('#cef').value,
        fullName: document.querySelector('#fullName').value,
        major: document.querySelector('#majorSelect ').value,
        photo: document.querySelector('#studentPhoto').value
    };

    if (!student.cef || !student.fullName || !student.major) {
        alert('All fields are required');
        return;
    }

    if (students.find(stud => stud.cef == student.cef)) {
        alert('This student already exists');
    } else {
        students.push(student);
        alert('student added successfully');
        form.classList.add('d-none');
        loadDisplay();
        document.querySelector('#fullName').value = '';
        document.querySelector('#cef').value = '';
        document.querySelector('#majorSelect').value = '';
        document.querySelector('#studentPhoto').value = '';
    }

   
}


let deleteStudent = (index) => {
    if (confirm('Are you sure you want to remove this student?')) {
        employees.splice(index, 1);
        loadDisplay();
    }
}


let editStudent = (index) => {
    document.querySelector('#saveChangesBtn').classList.remove("d-none");
    document.querySelector('#saveBtn').classList.add('d-none')
    document.querySelector('#cef').setAttribute('readonly', true)
    document.querySelector('#cef').value = students[index].cef;
    document.querySelector('#fullName').value = students[index].fullName;
    document.querySelector('#majorSelect').value = students[index].major;
    document.querySelector('#studentPhoto').value = students[index].photo;
    
    form.classList.remove('d-none');


}

let saveChanges = (index) => {
    if (!document.querySelector('#cef').value || !document.querySelector('#fullName').value || !document.querySelector('#majorSelect').value) {
        alert('All fields are required');
        return;
    } else {
        students[index].cef = document.querySelector('#cef').value;
        students[index].fullName = document.querySelector('#fullName').value;
        students[index].major = document.querySelector('#majorSelect').value;
        students[index].photo = document.querySelector('#studentPhoto').value;
        // clearing the inputs
        document.querySelector('#fullName').value = '';
        document.querySelector('#cef').value = '';
        document.querySelector('#majorSelect').value = '';
        document.querySelector('#studentPhoto').value = '';
        form.classList.add('d-none');
        loadDisplay();
    
    }
    

}





// what happens on load

getData(); // data is fetched
