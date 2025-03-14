//     // native JS version

//     // function to display student info in the table;
// let loadDisplay = () => {
//     document.querySelector('#studentsDisplay').innerHTML = students.map((student, i) => `
//     <tr>
//         <td>${student.cef} </td>
//         <td>${student.fullName} </td>
//         <td>${student.major} </td>
//         <td><img src="${student.photo}" alt=""></td>
//         <td>
//             <button id="editBtn" class='btn btn-secondary' onclick="editStudent(${i})">🖋️</button>
//             <button id="deleteBtn" class='btn btn-danger' onclick="deleteStudent(${i})">🗑️</button>
//         </td>
//     </tr>`).join('');
// }

// // getting the data from the json file
// let students;
// const getData = async () => {
//     const response = await fetch('students.json');
//     students = await response.json();
//     loadDisplay(); // display info after fetching it
// }
// let form = document.querySelector('#infoForm');

// document.querySelector("#addBtn").addEventListener('click', () => {
//     form.classList.remove('d-none');
// });

// document.querySelector("#cancelBtn").addEventListener('click', () => {
//     form.classList.add('d-none');
//     document.querySelector('#saveStudent').classList.remove('d-none');
//     document.querySelector('#saveChangesBtn').classList.add('d-none');
// })

// let saveStudent = () => {
//     let student = {
//         cef: document.querySelector('#cef').value,
//         fullName: document.querySelector('#fullName').value,
//         major: document.querySelector('#majorSelect ').value,
//         photo: document.querySelector('#studentPhoto').value
//     };

//     if (!student.cef || !student.fullName || !student.major) {
//         alert('All fields are required');
//         return;
//     }

//     if (students.find(stud => stud.cef == student.cef)) {
//         alert('This student already exists');
//     } else {
//         students.push(student);
//         alert('student added successfully');
//         form.classList.add('d-none');
//         loadDisplay();
//         document.querySelector('#fullName').value = '';
//         document.querySelector('#cef').value = '';
//         document.querySelector('#majorSelect').value = '';
//         document.querySelector('#studentPhoto').value = '';
//     }

   
// }


// let deleteStudent = (index) => {
//     if (confirm('Are you sure you want to remove this student?')) {
//         employees.splice(index, 1);
//         loadDisplay();
//     }
// }


// let editStudent = (index) => {
//     document.querySelector('#saveChangesBtn').classList.remove("d-none");
//     document.querySelector('#saveBtn').classList.add('d-none')
//     document.querySelector('#cef').setAttribute('readonly', true)
//     document.querySelector('#cef').value = students[index].cef;
//     document.querySelector('#fullName').value = students[index].fullName;
//     document.querySelector('#majorSelect').value = students[index].major;
//     document.querySelector('#studentPhoto').value = students[index].photo;
    
//     form.classList.remove('d-none');
//     document.querySelector('#saveStudent').classList.add('d-none');
//     document.querySelector('#saveChangesBtn').classList.remove('d-none');


// }

// let saveChanges = (index) => {
//     if (!document.querySelector('#cef').value || !document.querySelector('#fullName').value || !document.querySelector('#majorSelect').value) {
//         alert('All fields are required');
//         return;
//     } else {
//         students[index].cef = document.querySelector('#cef').value;
//         students[index].fullName = document.querySelector('#fullName').value;
//         students[index].major = document.querySelector('#majorSelect').value;
//         students[index].photo = document.querySelector('#studentPhoto').value;
//         // clearing the inputs
//         document.querySelector('#fullName').value = '';
//         document.querySelector('#cef').value = '';
//         document.querySelector('#majorSelect').value = '';
//         document.querySelector('#studentPhoto').value = '';
//         form.classList.add('d-none');
//         loadDisplay();

//         document.querySelector('#saveStudent').classList.remove('d-none');
//         document.querySelector('#saveChangesBtn').classList.add('d-none');
    
//     }
    

// }





// // what happens on load

// getData(); // data is fetched



// Native JS version

let students;
let editingIndex = -1;
const form = document.querySelector('#infoForm');

// Function to display students in the table
let loadDisplay = () => {
    document.querySelector('#studentsDisplay').innerHTML = students.map(student => `
    <tr>
        <td><input type="checkbox" class="selectStudent" data-cef="${student.cef}"></td>
        <td>${student.cef}</td>
        <td>${student.fullName}</td>
        <td>${student.major}</td>
        <td><img src="${student.photo}" alt=""></td>
        <td>
            <button class='btn btn-secondary' onclick="editStudent('${student.cef}')">🖋️</button>
            <button class='btn btn-danger' onclick="deleteStudent('${student.cef}')">🗑️</button>
        </td>
    </tr>`).join('');
};

// Fetch data from students.json
const getData = async () => {
    try {
        const response = await fetch('students.json');
        if (!response.ok) throw new Error('Failed to fetch students.json');
        students = await response.json();
        loadDisplay();
    } catch (error) {
        console.error(error);
        alert('Error loading student data. Please try again.');
    }
};

// Show form for adding a student
document.querySelector('#addBtn').addEventListener('click', () => {
    form.classList.remove('d-none');
    document.querySelector('#cef').removeAttribute('readonly');
    document.querySelector('#saveBtn').classList.remove('d-none');
    document.querySelector('#saveChangesBtn').classList.add('d-none');
    // Clear form fields
    document.querySelector('#cef').value = '';
    document.querySelector('#fullName').value = '';
    document.querySelector('#majorSelect').value = '';
    document.querySelector('#studentPhoto').value = '';
});

// Hide form on cancel
document.querySelector('#cancelBtn').addEventListener('click', () => {
    form.classList.add('d-none');
    document.querySelector('#saveBtn').classList.remove('d-none');
    document.querySelector('#saveChangesBtn').classList.add('d-none');
    document.querySelector('#cef').removeAttribute('readonly');
});

// Save a new student
let saveStudent = () => {
    let student = {
        cef: document.querySelector('#cef').value,
        fullName: document.querySelector('#fullName').value,
        major: document.querySelector('#majorSelect').value,
        photo: document.querySelector('#studentPhoto').value
    };

    if (!student.cef || !student.fullName || !student.major) {
        alert('All fields are required');
        return;
    }

    if (students.find(stud => stud.cef === student.cef)) {
        alert('This student already exists');
    } else {
        students.push(student);
        alert('Student added successfully');
        form.classList.add('d-none');
        loadDisplay();
    }
};

// Delete a single student by CEF
let deleteStudent = (cef) => {
    if (confirm('Are you sure you want to remove this student?')) {
        students = students.filter(student => student.cef !== cef);
        loadDisplay();
    }
};

// Edit a student by CEF
let editStudent = (cef) => {
    editingIndex = students.findIndex(stud => stud.cef === cef);
    if (editingIndex !== -1) {
        const student = students[editingIndex];
        document.querySelector('#cef').value = student.cef;
        document.querySelector('#fullName').value = student.fullName;
        document.querySelector('#majorSelect').value = student.major;
        document.querySelector('#studentPhoto').value = student.photo;
        document.querySelector('#cef').setAttribute('readonly', true);
        form.classList.remove('d-none');
        document.querySelector('#saveBtn').classList.add('d-none');
        document.querySelector('#saveChangesBtn').classList.remove('d-none');
    }
};

// Save changes to an edited student
let saveChanges = () => {
    if (editingIndex === -1) return;
    if (!document.querySelector('#cef').value || !document.querySelector('#fullName').value || !document.querySelector('#majorSelect').value) {
        alert('All fields are required');
        return;
    }
    students[editingIndex].fullName = document.querySelector('#fullName').value;
    students[editingIndex].major = document.querySelector('#majorSelect').value;
    students[editingIndex].photo = document.querySelector('#studentPhoto').value;
    form.classList.add('d-none');
    loadDisplay();
    document.querySelector('#saveBtn').classList.remove('d-none');
    document.querySelector('#saveChangesBtn').classList.add('d-none');
    editingIndex = -1;
};

// Select All checkbox functionality
document.querySelector('#selectAll').addEventListener('change', (e) => {
    const isChecked = e.target.checked;
    document.querySelectorAll('.selectStudent').forEach(checkbox => {
        checkbox.checked = isChecked;
    });
});

// Delete selected students
document.querySelector('#deleteSelectedBtn').addEventListener('click', () => {
    if (confirm('Are you sure you want to delete the selected students?')) {
        const cefsToDelete = [];
        document.querySelectorAll('.selectStudent:checked').forEach(checkbox => {
            cefsToDelete.push(checkbox.getAttribute('data-cef'));
        });
        students = students.filter(student => !cefsToDelete.includes(student.cef));
        loadDisplay();
        document.querySelector('#selectAll').checked = false;
    }
});

// Initialize on load
getData();  