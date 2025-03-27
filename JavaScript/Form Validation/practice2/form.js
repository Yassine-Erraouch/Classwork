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


document.querySelector('#myForm').addEventListener('change', function (e) {
    e.preventDefault();
    if (isValid) {
        let nom = document.querySelector('#nom').value.trim();
        let prenom = document.querySelector('#prenom').value.trim();
        let email = document.querySelector('#email').value.trim();
        let genre = document.querySelector('input[name="genre"]:checked').value;
        let skills = [...document.querySelectorAll('input[name="skills"]:checked')].map(item => item.value).join(',');
        let commentaire = document.querySelector('#commentaire').value;
        let pays = document.querySelector('#pays').value;
        let mdp = document.querySelector('#mdp').value;

        document.querySelector('#resNom').textContent = nom;
        document.querySelector('#resPrenom').textContent = prenom;
        document.querySelector('#resEmail').textContent = email;
        document.querySelector('#resGenre').textContent = genre;
        document.querySelector('#resSkills').textContent = skills;
        document.querySelector('#resComment').textContent = commentaire;
        document.querySelector('#resPays').textContent = pays;
        document.querySelector('#resMdp').textContent = mdp;
    };
    

});

        