const form = document.querySelector('#myForm');
let isValid = true;



// fucntion to validate field
function validateField(input, errorId, condition, errorMessage) {
    const errorSpan = document.getElementById(errorId);
    if (condition(input.value)) {
        errorSpan.textContent = "✔ Valide";
        errorSpan.style.color = "green";
        isValid=true;
    } else {
        errorSpan.textContent = `✖ ${errorMessage}`;
        errorSpan.style.color = "red";
        isValid=false;
    }
}

// fucntion to validate radio
function validateRadio(errorId) {
    const checked = document.querySelector('input[name="genre"]:checked');
    updateMessage(errorId, checked, "Sélectionnez un sexe");
}

// function to validate checkbox;
function validateCheckbox(errorId) {
    const checked = document.querySelectorAll('input[name="skills"]:checked').length > 0;
    updateMessage(errorId, checked, "Sélectionnez au moins une skill");
}

// function to update error and success message
function updateMessage(errorId, isValid, errorMessage) {
    const errorSpan = document.getElementById(errorId);
    if (isValid) {
        errorSpan.textContent = "✔ Valide";
        errorSpan.style.color = "green";
        isValid=true;
    } else {
        errorSpan.textContent = `✖ ${errorMessage}`;
        errorSpan.style.color = "red";
        isValid=false;
    }
}

// event listener for each field checkbox and radio
form.addEventListener('change', function (event) {
    const target = event.target;
    if (target.id === "nom") validateField(target,"nomError", value => /^[A-Z]{3,}$/.test(value.trim()), "Minimum 3 cáractéres majuscules." );
    if (target.id === "prenom") validateField(target, "prenomError" , value => /^[A-Z]{1}[a-z]{2,}$/.test(value), "Prénom doit commencer par une lettre majuscule et avoir au moins 3 caractère.");
    if (target.id === "email") validateField(target, "emailError", value => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value), "Adresse Email invalide.");
    if (target.name === "genre") validateRadio("genreError");
    if (target.name === "skills") validateCheckbox("skillsError");
    if (target.id === "pays") validateField(target, "paysError", value => value !== "", "Vous devez sélectionner un pays" )
    if (target.id === "site") validateField (target, 'urlError', value => /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/.test(value), "adresse URL invalide.");
    if (target.id === "mdp") validateField (target, "mdpError", value => /^(?=.*[A-Za-z])(?=.*[!@#$%^&*()_+=-])[A-Za-z0-9!@#$%^&*()_+=-]{6,}$/.test(value), "mot doit avoir au moins 6 caractère et doit inclure les cháractère spéciaux");
    if(target.id === "commentaire") validateField(target, "commentError", value => value.trim().length >= 10, "message doit avoir 10 charactère au minimum.");

});

document.querySelector('#myForm').addEventListener('submit', function (e) {
    e.preventDefault();
    if (isValid) {
        let nom = document.querySelector('#nom').value.trim();
        let prenom = document.querySelector('#prenom').value.trim();
        let email = document.querySelector('#email').value.trim();
        let genre = document.querySelector('input[name="genre"]:checked')? document.querySelector('input[name="genre"]:checked').value : "";
        let skills = [...document.querySelectorAll('input[name="skills"]:checked')].map(item => item.value).join(',');
        let commentaire = document.querySelector('#commentaire').value;
        let pays = document.querySelector('#pays').value;
        let mdp = document.querySelector('#mdp').value;
        let url = document.querySelector('#site').value;

        document.querySelector('#resNom').textContent = nom;
        document.querySelector('#resPrenom').textContent = prenom;
        document.querySelector('#resEmail').textContent = email;
        document.querySelector('#resGenre').textContent = genre;
        document.querySelector('#resSkills').textContent = skills;
        document.querySelector('#resComment').textContent = commentaire;
        document.querySelector('#resPays').textContent = pays;
        document.querySelector('#resMdp').textContent = mdp;
        document.querySelector('#resSite').textContent = url;
    };
    document.querySelector('#myForm').reset();

});


        