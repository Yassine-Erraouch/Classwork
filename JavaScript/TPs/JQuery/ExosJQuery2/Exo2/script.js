    // native js version:

let calculate = () => {
    let payment;
    let amount = parseFloat(document.querySelector("#amount").value);
    let mRate = parseFloat(document.querySelector("#rate").value)/(12*100);
    let duration = parseFloat(document.querySelector("#duration").value);

        
     if (isNaN(amount) || isNaN(mRate) || isNaN(duration)) {
        alert('Please enter valid values');
        document.querySelector("#amount").value = '';
        document.querySelector("#rate").value = '';
        document.querySelector("#duration").value = '';
        document.querySelector("#amount").focus();
    } else {
        payment = (amount * mRate)/ (1- (1+ mRate)**(-duration*12));
        document.querySelector("#result").innerHTML = `${payment.toFixed(2)} €`;
    }
};


    // JQuery version

// let calculate = () => {
//     let payment;
    
//     let amount = $("#amount").val();
//     let mRate = $("#rate").val();
//     let duration = $("#duration").val();
    
//     if(isNaN(amount) || isNaN(mRate) || isNaN(duration)) {
//         alert('Please enter valid values');
//         $("#amount").val('');
//         $("#rate").val('');
//         $("#duration").val('');
//         $("#amount").focus();
//     } else {
//         let payment = (parseFloat(amount) * parseFloat(mRate)/(12*100))/ (1- (1+ parseFloat(mRate)/(12*100))**(-parseFloat(duration)*12));
//         $("#result").html(`${payment.toFixed(2)} €`);
//     }
// };

document.querySelector("#calculate").addEventListener("click", calculate);