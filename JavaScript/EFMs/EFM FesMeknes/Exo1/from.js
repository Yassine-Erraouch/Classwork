// inputs
let nameIn = document.querySelector('#fullName');
let departCityIn = document.querySelector('#departCity');
let arrivCityIn = document.querySelector('#arrivCity');
let comfortIn = document.getElementsByName('class');
let nrbIn = document.querySelector('#nbr');

let cities = [
  "Agadir",
  "Al Hoceima",
  "Azilal",
  "Beni Mellal",
  "Casablanca",
  "Chefchaouen",
  "El Jadida",
  "Essaouira",
  "Fes",
  "Kénitra",
  "Khouribga",
  "Larache",
  "Marrakech",
  "Meknes",
  "Mohammedia",
  "Nador",
  "Ouarzazate",
  "Oujda",
  "Rabat",
  "Safi",
  "Salé",
  "Settat",
  "Tanger",
  "Tétouan",
  "Zagora"
];

let cityCouples = [
  {
    departCity: "Casablanca",
    arrivCity: "Marrakech",
    firstClassPrice: 150,
    secondClassPrice: 100
  },
  {
    departCity: "Rabat",
    arrivCity: "Fes",
    firstClassPrice: 120,
    secondClassPrice: 80
  },
  {
    departCity: "Marrakech",
    arrivCity: "Agadir",
    firstClassPrice: 180,
    secondClassPrice: 120
  },
  {
    departCity: "Fes",
    arrivCity: "Tanger",
    firstClassPrice: 200,
    secondClassPrice: 150
  },
  {
    departCity: "Casablanca",
    arrivCity: "Rabat",
    firstClassPrice: 100,
    secondClassPrice: 60
  },
  {
    departCity: "Meknes",
    arrivCity: "Chefchaouen",
    firstClassPrice: 220,
    secondClassPrice: 180
  },
  {
    departCity: "Agadir",
    arrivCity: "Essaouira",
    firstClassPrice: 250,
    secondClassPrice: 200
  },
  {
    departCity: "Tanger",
    arrivCity: "Tétouan",
    firstClassPrice: 280,
    secondClassPrice: 220
  },
  {
    departCity: "Rabat",
    arrivCity: "Meknes",
    firstClassPrice: 180,
    secondClassPrice: 120
  },
  {
    departCity: "Fes",
    arrivCity: "Marrakech",
    firstClassPrice: 250,
    secondClassPrice: 200
  }
];
// fucntion to validate form.
let validerForm = () => {
    let nameEx = /^[A-z]{1}[a-z]{1,}\s[A-z]{1}[a-z]{1,}$/;

    if (!nameEx.test(nameIn.value)) {
        
    }

 
}


// function to calculate total
let calculer = () => {
    let 
}