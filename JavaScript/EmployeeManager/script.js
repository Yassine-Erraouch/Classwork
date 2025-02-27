let employees = [];

const salaryScales = [
    {
      scale: "Échelle 6 – Entry-Level Teacher",
      levels: [
        { echelon: 1, indice: 300, baseSalary: 4500 },
        { echelon: 2, indice: 310, baseSalary: 4650 },
        { echelon: 3, indice: 320, baseSalary: 4800 },
        { echelon: 4, indice: 330, baseSalary: 4950 },
        { echelon: 5, indice: 340, baseSalary: 5100 },
        { echelon: 6, indice: 350, baseSalary: 5250 },
        { echelon: 7, indice: 360, baseSalary: 5400 },
        { echelon: 8, indice: 370, baseSalary: 5550 },
        { echelon: 9, indice: 380, baseSalary: 5700 },
        { echelon: 10, indice: 390, baseSalary: 5850 }
      ]
    },
    {
      scale: "Échelle 7 – Mid-Level Teacher",
      levels: [
        { echelon: 1, indice: 400, baseSalary: 6000 },
        { echelon: 2, indice: 410, baseSalary: 6150 },
        { echelon: 3, indice: 420, baseSalary: 6300 },
        { echelon: 4, indice: 430, baseSalary: 6450 },
        { echelon: 5, indice: 440, baseSalary: 6600 },
        { echelon: 6, indice: 450, baseSalary: 6750 },
        { echelon: 7, indice: 460, baseSalary: 6900 },
        { echelon: 8, indice: 470, baseSalary: 7050 },
        { echelon: 9, indice: 480, baseSalary: 7200 },
        { echelon: 10, indice: 490, baseSalary: 7350 }
      ]
    },
    {
      scale: "Échelle 8 – Experienced Teacher",
      levels: [
        { echelon: 1, indice: 500, baseSalary: 7500 },
        { echelon: 2, indice: 510, baseSalary: 7650 },
        { echelon: 3, indice: 520, baseSalary: 7800 },
        { echelon: 4, indice: 530, baseSalary: 7950 },
        { echelon: 5, indice: 540, baseSalary: 8100 },
        { echelon: 6, indice: 550, baseSalary: 8250 },
        { echelon: 7, indice: 560, baseSalary: 8400 },
        { echelon: 8, indice: 570, baseSalary: 8550 },
        { echelon: 9, indice: 580, baseSalary: 8700 },
        { echelon: 10, indice: 590, baseSalary: 8850 }
      ]
    },
    {
      scale: "Échelle 9 – Senior Teacher",
      levels: [
        { echelon: 1, indice: 600, baseSalary: 9000 },
        { echelon: 2, indice: 610, baseSalary: 9150 },
        { echelon: 3, indice: 620, baseSalary: 9300 },
        { echelon: 4, indice: 630, baseSalary: 9450 },
        { echelon: 5, indice: 640, baseSalary: 9600 },
        { echelon: 6, indice: 650, baseSalary: 9750 },
        { echelon: 7, indice: 660, baseSalary: 9900 },
        { echelon: 8, indice: 670, baseSalary: 10050 },
        { echelon: 9, indice: 680, baseSalary: 10200 },
        { echelon: 10, indice: 690, baseSalary: 10350 }
      ]
    },
    {
      scale: "Échelle 10 – Master Teacher",
      levels: [
        { echelon: 1, indice: 700, baseSalary: 10500 },
        { echelon: 2, indice: 710, baseSalary: 10650 },
        { echelon: 3, indice: 720, baseSalary: 10800 },
        { echelon: 4, indice: 730, baseSalary: 10950 },
        { echelon: 5, indice: 740, baseSalary: 11100 },
        { echelon: 6, indice: 750, baseSalary: 11250 },
        { echelon: 7, indice: 760, baseSalary: 11400 },
        { echelon: 8, indice: 770, baseSalary: 11550 },
        { echelon: 9, indice: 780, baseSalary: 11700 },
        { echelon: 10, indice: 790, baseSalary: 11850 },
      ]
    },
    {
      scale: "Échelle 11 – High-Level/Managerial Teaching Positions",
      levels: [
        { echelon: 1, indice: 800, baseSalary: 12000 },
        { echelon: 2, indice: 810, baseSalary: 12150 },
        { echelon: 3, indice: 820, baseSalary: 12300 },
        { echelon: 4, indice: 830, baseSalary: 12450 },
        { echelon: 5, indice: 840, baseSalary: 12600 },
        { echelon: 6, indice: 850, baseSalary: 12750 },
        { echelon: 7, indice: 860, baseSalary: 12900 },
        { echelon: 8, indice: 870, baseSalary: 13050 },
        { echelon: 9, indice: 880, baseSalary: 13200 },
        { echelon: 10, indice: 890, baseSalary: 13350 }
      ]
    }
  ];


//   fill selects
let fillSelects = () => {
    let echelonSelect = document.querySelector("#echelon");
    let echelleSelect = document.querySelector("#echelle");

    echelonSelect.innerHTML = "";
    echelleSelect.innerHTML = "";

    salaryScales.map((echelle) => {
        
    })
}
  