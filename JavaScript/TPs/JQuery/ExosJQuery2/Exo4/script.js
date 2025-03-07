    // native js version
// let diff = () => {
//     let d1 = new Date(document.getElementById("d1").value);
//     let d2 = new Date(document.getElementById("d2").value);
//     let diff = d2.getTime() - d1.getTime();
//     let days = Math.abs(Math.floor(diff / (1000 * 60 * 60 * 24)));
//     document.getElementById("result").innerHTML = `${days} days`;
// }



    // JQuery version
let diff = () => {
    let d1 = new Date($('#d1').val());
    let d2 = new Date($('#d2').val());
    let diff = d2.getTime() - d1.getTime();
    let days = Math.abs(Math.floor(diff / (1000 * 60 * 60 * 24)));
    $('#result').html(`${days} days`);
}

document.querySelector('#calcBtn').addEventListener('click', diff);