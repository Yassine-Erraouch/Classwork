
// List of coutnries by continent
const countriesByContinent = {
    Afrique: ["Nigeria", "Éthiopie", "Égypte", "Afrique du Sud", "Kenya", "Algérie", "Maroc", "Ghana", "Angola", "Ouganda"],
    Asie: ["Chine", "Inde", "Indonésie", "Pakistan", "Bangladesh", "Japon", "Philippines", "Vietnam", "Turquie", "Iran"],
    Europe: ["Allemagne", "France", "Royaume-Uni", "Italie", "Espagne", "Ukraine", "Pologne", "Roumanie", "Pays-Bas", "Belgique"],
    Amériques: ["États-Unis", "Canada", "Mexique", "Guatemala", "Cuba", "Haïti", "République Dominicaine", "Honduras", "El Salvador", "Nicaragua", "Brésil", "Argentine", "Colombie", "Chili", "Pérou", "Venezuela", "Équateur", "Bolivie", "Paraguay", "Uruguay"],
    Océanie: ["Australie", "Papouasie-Nouvelle-Guinée", "Nouvelle-Zélande", "Fidji", "Îles Salomon", "Vanuatu", "Samoa", "Kiribati", "Tonga", "Micronésie"],
    Antarctique: ["Aucun"]
};

const continents = Object.keys(countriesByContinent);
document.querySelector('#contSelect').innerHTML += continents.map((item)=> 
    `<option value='${item}'>${item}</option>`).join('');

document.querySelector('#contSelect').addEventListener('change', (e) => {
    let continent = e.target.value;
    let countries = countriesByContinent[continent];
    document.querySelector('#countryOptions').innerHTML = countries.map((item)=> 
    `<div class="row">
        <div class="col-auto">
            <input type="checkbox" name="country" id="${item}" class="form-check country-check">
        </div>

        <div class="col">
            <label for="${item}" class="from-check" id="">${item}</label>
        </div>
    </div>`).join('');
});

// document.querySelector('#contSelect').innerHTML = countries.map((item)=> 
//     `<option value='${item}'>${item}</option>`).join('');



let data ;

// function to display fetched data
let displayData = () => {
    document.querySelector('#display').innerHTML = data.map((item, i    )=> 
                `<tr>
                    <td><input type="checkbox" name="" id="" class="check"></td>
                    <td>${item.code}</td>
                    <td>${item.nom}</td>
                    <td>
                        <ul>
                            ${item.pays.map(element => `<li>${element}</li>`).join('')}
                        </ul>
                    </td>
                    <td>
                        <button class="btn btn-primary" id="editBtn" onclick="edit()" data-bs-toggle="modal" data-bs-target="#addModal">Edit</button>
                        <button class="btn btn-danger" id="removeBtn" onclick="remove(${i})">Remove</button>
                    </td>
                </tr>`).join('');   
};





// fetching the data from the api
$.ajax({
    type: 'GET', 
    url: 'http://localhost:3000/countries',
    success: function(response) {
        data = response;
        displayData();
        
    },
    error: function(xhr, status, error) {
      // Handle errors here
    }
  });


let remove = (i) => {
    if (confirm("Êtes-vous sure vous voulez supprimer?")) {
        data.splice(i,1);
    }
    displayData();
}

let add = () => {
    let cont =  document.querySelector('#contSelect');
    let checks = document.querySelectorAll('.country-check');
    selectedCountries = [];

    console.log(typeof checks);


    // Iterating through checked countries
    for (let i= 0; i< checks.length; i++) {
        if (checks[i].checked == true) {
            selectedCountries.push(checks[i].value);
        }
    }

    console.log(cont.value);
    console.log(selectedCountries);
    if (cont.value == "" && selectedCountries.length<0) {
        alert('Veuillez selectionner un continent et un ou plusieurs pays');
        return;
    }

    
    data[cont.value] = selectedCountries; // updating the information in our data array 
    displayData(); // displaying the updated data
}


let edit = (i) => {
    let selectedCountries  = data[i]; 
    let globalCountries =  countriesByContinent[data[i].nom];

    document.querySelector('#contSelect').value = data[i].nom;

    document.querySelector('#contSelect').dispatchEvent(new Event("change"));

    console.log(selectedCountries, globalCountries);
    
    let options =  globalCountries.map((item, pos) => {
        `<input type="checkbox" value="${item}" ${selectedCountries.findIndex((p, i)=> {item == p}) > -1? "checked": ""}> &nbrsp; ${item} <br>`}).join('');
    
    document.querySelector('#countryOptions').innerHTML = options;

};
   






