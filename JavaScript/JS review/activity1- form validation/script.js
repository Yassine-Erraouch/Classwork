// fetching values from the form after submit
let form = document.querySelector('#myForm');

// assigning variables to inputs;
let fullName = document.querySelector('#fullName');
let age = document.querySelector('#age');
let height = document.querySelector('#height');
let url = document.querySelector('#url');
let birthDate = document.querySelector('#birthDate');
let email = document.querySelector('#email');
let password = document.querySelector('#password');
let gender = document.querySelector('input[name="gender"]');
let address = document.querySelector('#address');
let hobbies = document.querySelectorAll('input[name="hobbies"]');
let photo = document.querySelector('#photo');

// assigning variable to the error spans;
let fullNameError = document.querySelector('#fullNameError');
let ageError = document.querySelector('#ageError');
let heightError = document.querySelector('#heightError');
let urlError = document.querySelector('#urlError');
let birthDateError = document.querySelector('#birthDateError');
let emailError = document.querySelector('#emailError');
let passwordError = document.querySelector('#passwordError');
let genderError = document.querySelector('#genderError');
let addressError = document.querySelector('#addressError');
let hobbiesError = document.querySelector('#hobbiesError');
let photoError = document.querySelector('#photoError');


form.addEventListener('submit', function (e)) {
    e.preventDefault();

    if (fullName.value === "" || !fullName.value.test(/[^a-zA-Z ]/)) {
        fullNameError.innerHTML = "Full Name must contain only letters and spaces";
    };


    if (age.value === "" || age.value > 120 || age.value < 0) {
        ageError.innerHTML = "Age must be between 0 and 120";
    };

    if ()
}

