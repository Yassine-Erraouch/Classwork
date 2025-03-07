    // native js version
// let toFahrenheit = () => {
//     let temp = document.querySelector("#temp").value;
//     if (isNaN(temp)) {
//         alert('Please enter valid temperature');
//         document.querySelector("#temp").value = '';
//         document.querySelector("#temp").focus();
//     } else {
//         document.querySelector("#result").innerHTML = `${(temp * 1.8 + 32).toFixed(2)}°F`;
//     }
// };

// let toCelsius = () => {
//     let temp = document.querySelector("#temp").value;
//     if (isNaN(temp)) {
//         alert('Please enter valid temperature');
//         document.querySelector("#temp").value = '';
//         document.querySelector("#temp").focus();
//     } else {
//         document.querySelector("#result").innerHTML = `${((temp - 32) * 5/9).toFixed(2)}°C`;
//     }
// };


    // JQuery version

let toFahrenheit = () => {
    let temp = $("#temp").val();
    if (isNaN(temp)) {
        alert('Please enter valid temperature');
        $("#temp").val('');
        $("#temp").focus();
    } else {
        $("#result").html(`${(temp * 1.8 + 32).toFixed(2)}°F`);
    }
};

let toCelsius = () => {
    let temp = $("#temp").val();
    if (isNaN(temp)) {
        alert('Please enter valid temperature');
        $("#temp").val('');
        $("#temp").focus();
    } else {
        $("#result").html(`${((temp - 32) * 5/9).toFixed(2)}°C`);
    }
};