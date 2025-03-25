// ---------------------------my attempt-------------------------------------
// // inputs
// let nameIn = document.querySelector("#name");
// let emailIn = document.querySelector("#email");
// let pwdIn = document.querySelector("#pwd");
// let age = document.querySelector("#age");
// let birthDateIn = document.querySelector("#birthDate");

// // the radio inputs to be figured out
// let countryIn = document.querySelector("#country");
// let hobbies = document.querySelectorAll("input[name:hobbies]:checked");


// // global validation variable;
// let isValid = true;


// // the regular expressions for each input;
// let nameEx = /^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$/;
// let emailEx = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
// let pwdEx = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!#$%&?]).{6,}$/;



// nameIn.addEventListener('change', ()=> {
//     if (!nameEx.test(nameIn.value)){
//         isValid = false;
//         document.querySelector('#nameError').innerHTML = `<i class="fa-solid fa-xmark"></i> le nom est invalide.`
//     } else {
//         document.querySelector('#nameValid').innerHTML = `<i class="fa-solid fa-check"></i> le nom est valide.`
//     }
// });

// emailIn.addEventListener


// ----------------------------------code copied from the version by the instructor---------------
const form = document.getElementById("myForm");

    form.addEventListener("change", function (event) {
        const target = event.target;
        if (target.id === "name") validateField(target, "nameError", value => value.trim().length >= 3, "Minimum 3 caractères");
        if (target.id === "email") validateField(target, "emailError", value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value), "Email invalide");
        if (target.name === "gender") validateRadio("genderError");
        if (target.name === "interests") validateCheckbox("interestsError");
        if (target.id === "message") validateField(target, "messageError", value => value.trim().length >= 10, "Minimum 10 caractères");
        if (target.id === "country") validateField(target, "countryError", value => value !== "", "Sélectionnez un pays");
        if (target.id === "file") validateFile(target, "fileError");
    });

    function validateField(input, errorId, condition, errorMessage) {
        const errorSpan = document.getElementById(errorId);
        if (condition(input.value)) {
            errorSpan.textContent = "✔ Valide";
            errorSpan.style.color = "green";
        } else {
            errorSpan.textContent = `✖ ${errorMessage}`;
            errorSpan.style.color = "red";
        }
    }

    function validateRadio(errorId) {
        const checked = document.querySelector('input[name="gender"]:checked');
        updateMessage(errorId, checked, "Sélectionnez un sexe");
    }

    function validateCheckbox(errorId) {
        const checked = document.querySelectorAll('input[name="interests"]:checked').length > 0;
        updateMessage(errorId, checked, "Sélectionnez au moins un centre d'intérêt");
    }

    function validateFile(input, errorId) {
        const file = input.files[0];
        const validExtensions = ["jpg", "jpeg", "png", "gif"];
        const isValid = file && validExtensions.includes(file.name.split('.').pop().toLowerCase());
        updateMessage(errorId, isValid, "Format invalide (jpg, jpeg, png, gif seulement)");
    }

    function updateMessage(errorId, isValid, errorMessage) {
        const errorSpan = document.getElementById(errorId);
        if (isValid) {
            errorSpan.textContent = "✔ Valide";
            errorSpan.style.color = "green";
        } else {
            errorSpan.textContent = `✖ ${errorMessage}`;
            errorSpan.style.color = "red";
        }
    }
   //gérer l'event submit
   //si tout va bien afficher les informations au niveau d'un div 