window.onload = function() {
  // Populate cities
  const cities = ['Casablanca', 'Rabat', 'Kenitra', 'Meknés', 'Fès', 'Oujda'];
  const departCity = document.getElementById('departCity');
  const arrivCity = document.getElementById('arrivCity');
  
  cities.forEach(city => {
      departCity.innerHTML += `<option value="${city}">${city}</option>`;
      arrivCity.innerHTML += `<option value="${city}">${city}</option>`;
  });
  // event listener for form validation
  document.getElementById('travelForm').addEventListener('submit', validerForm);
};

function clearInputs() {
  // Clear text inputs
  document.getElementById('fullName').value = '';
  document.getElementById('nbr').value = '';
  document.getElementById('cardNumber').value = '';
  document.getElementById('total').value = '';
  
  // Uncheck radio buttons
  document.getElementById('firstClass').checked = false;
  document.getElementById('secondClass').checked = false;
  document.getElementById('card').checked = false;
  document.getElementById('cash').checked = false;
  
  // Reset dropdowns to first option
  document.getElementById('departCity').selectedIndex = 0;
  document.getElementById('arrivCity').selectedIndex = 0;
}

function validerForm(e) {
  e.preventDefault();
  // Collect elements
  const elements = {
      fullName: document.getElementById('fullName').value.trim(),
      departCity: document.getElementById('departCity').value,
      arrivCity: document.getElementById('arrivCity').value,
      class: document.querySelector('input[name="class"]:checked'),
      nbr: parseInt(document.getElementById('nbr').value),
      payment: document.querySelector('input[name="payment"]:checked'),
      cardNumber: document.getElementById('cardNumber').value.trim()
  };

  // Validation checks
  let errors = [];
  
  if (!elements.fullName) errors.push("Nom complet est requis");
  if (!elements.departCity) errors.push("Ville de départ est requise");
  if (!elements.arrivCity) errors.push("Ville d'arrivée est requise");
  if (elements.departCity === elements.arrivCity) errors.push("Ville de départ et d'arrivée doivent être différentes");
  if (!elements.class) errors.push("Classe de confort est requise");
  if (!elements.nbr || elements.nbr <= 0) errors.push("Nombre de personnes invalide");
  if (!elements.payment) {
      errors.push("Méthode de paiement requise");
  } else if (elements.payment.id === 'card' && !elements.cardNumber) {
      errors.push("Numéro de carte requis");
  }

  if (errors.length > 0) {
      alert(errors.join('\n'));
      return false;
  }
  alert("Formulaire validé!");
  return true;
}

function calculer() {
  const prices = {
      'Kenitra': 30,
      'Rabat': 50,
      'Meknés': 90,
      'Fès': 120,
      'Oujda': 180
  };
  
  const arrival = document.getElementById('arrivCity').value;
  const isFirstClass = document.getElementById('firstClass').checked;
  const people = parseInt(document.getElementById('nbr').value);

  let price = prices[arrival] || 0;
  if (isFirstClass) price *= 2;
  
  document.getElementById('total').value = `${price * people} dhs`;
}

// Event listeners
document.getElementById('calcBtn').addEventListener('click', e => {
  e.preventDefault();
  calculer();
});

document.getElementById('clearBtn').addEventListener('click', e => {
  e.preventDefault();
  clearInputs();
});