
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
    `<option value='${item}'>${item}</option>`).join('');
});

// document.querySelector('#contSelect').innerHTML = countries.map((item)=> 
//     `<option value='${item}'>${item}</option>`).join('');



let data ;

// function to display fetched data
let displayData = () => {
    document.querySelector('#display').innerHTML = data.map((item)=> 
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
                        <button class="btn btn-primary" id="editBtn" onclick="edit()">Edit</button>
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
        console.log(data);
    },
    error: function(xhr, status, error) {
      // Handle errors here
    }
  });


let remove = (i) => {
    if (confirm("Êtes-vous sure vous voulez supprimer?")) {
        data.splice(i,1);
    }
}

let add = () => {
    let cont =  document.querySelector('#contSelect');
    let country = document.querySelector('#countryOptions');

    if (cont.value != "" && country.value.length>0) {
        alert('Veuillez selectionner un continent et un ou plusieurs pays');
        return;
    }

    let pays = [];
    for (let i = 0; i < country.value.length; i++) {
        pays.push(country.value[i]);
    }
}






