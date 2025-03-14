let countries = [
    "Afrique du Sud",
    "Allemagne",
    "Australie",
    "Brésil",
    "Canada",
    "Chine",
    "Corée du Sud",
    "Egypte",
    "Etats-Unis",
    "France",
    "Inde",
    "Italie",
    "Japon",
    "Maroc",
    "Mexique",
    "Nouvelle-Zélande",
    "Russie",
    "Thaïlande",
    "Turquie",
    "Vietnam"
];

document.querySelector('#countryOptions').innerHTML = countries.map((item)=> 
    `<option value='${item}'>${item}</option>`).join('');



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
    let cont =  document.querySelector('#contInput');
    let country = document.querySelector('#countryOptions');

    if (cont!= "" && country.length>0) {
        
    }
}






