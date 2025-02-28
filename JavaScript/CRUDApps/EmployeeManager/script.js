let displayInfo = () => {
    let empList = document.querySelector('#employeeList');
    let info = employees.map((emp, i) => 
        `<tr>
            <td class="">
                <div class=" w-25">
                     <img src="${emp.photo}" alt="photo indisponible" class="img-fluid">
                </div>
           </td>
            <td>${emp.id} </td>  
            <td>${emp.lname} </td>  
            <td>${emp.fname} </td> 
            <td>${emp.echelle}</td>   
            <td>${emp.echelon} </td>  
            <td> 
                <div class="d-flex gap-1">
                    <button class="btn btn-info" id="" onclick="view(${i})" data-bs-toggle="modal" data-bs-target="#infoModal"><i class="fa-solid fa-info"></i></button>
                    <button class="btn btn-primary" id="" onclick="edit(${i})"><i class="fa-solid fa-pen-to-square"></i></button>
                    <button class="btn btn-danger" id="" onclick="remove(${i})"><i class="fa-solid fa-trash-can"></i></button> 
                </div>
            </td>
        </tr>`).join('');
    empList.innerHTML = info;
};


let employees;
// function to fetch
const GetData=async()=>{
    const response=await fetch('employees.json');
    employees  =await response.json();
    displayInfo();
}
// fetch data
GetData();







echelleSelect = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'];
document.querySelector('#echelle').innerHTML += echelleSelect.map((ech)=> `<option value="${ech}">${ech}</option>`).join(''); 
document.querySelector('#echelon').innerHTML += echelleSelect.map((ech)=> `<option value="${ech}">${ech}</option>`).join(''); 


// show employee info

let view = (index)=> {

    let infoId = document.querySelector('#infoId');
    let infoLName = document.querySelector('#infoLName');
    let infoFName = document.querySelector('#infoFName');
    let infoEchelle = document.querySelector('#infoEchelle');
    let infoEchelon = document.querySelector('#infoEchelon');
    let infoImage = document.querySelector('#infoImage');

    // console.log(employees[index]);

    infoId.innerHTML = `${employees[index].id}`;
    infoLName.innerHTML = `${employees[index].lname}`;
    infoFName.innerHTML = `${employees[index].fname}`;
    infoEchelle.innerHTML = `${employees[index].echelle}`;
    infoEchelon.innerHTML = `${employees[index].echelon}`;
    infoImage.src = `${employees[index].photo}`;
};


// remove employee
let remove = (index) => {
    if (confirm('Êtes-vous sur de vouloir supprimer cet employé?')) {
        employees.splice(index, 1);
        displayInfo();
    }
}

// update employee info
let edit = (index) => {
    let addBtn = document.querySelector('#addBtn');
    addBtn.innerHTML = "Actualiser";
    let idInput = document.querySelector('#id');
    let lnameInput = document.querySelector('#lName');
    let fnameInput = document.querySelector('#fName');
    let echelleInput = document.querySelector('#echelle');
    let echelonInput = document.querySelector('#echelon');
    let photoInput = document.querySelector('#photo');

    idInput.value = employees[index].id;
    lnameInput.value = employees[index].lname;
    fnameInput.value = employees[index].fname;
    echelleInput.value = employees[index].echelle;
    echelonInput.value = employees[index].echelon;
    photoInput.value = employees[index].photo;

    const updateEmployee = () => {
        employees[index].id = idInput.value;
        employees[index].lname = lnameInput.value;
        employees[index].fname = fnameInput.value;
        employees[index].echelle = echelleInput.value;
        employees[index].echelon = echelonInput.value;
        employees[index].photo = photoInput.value || employees[index].photo;
        displayInfo();
    };


    addBtn.addEventListener('click', updateEmployee); // add new event listener
    addBtn.removeEventListener('click', updateEmployee); // remove previous event listener
    


}






