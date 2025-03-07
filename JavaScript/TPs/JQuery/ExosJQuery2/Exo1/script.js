    // native js version


// let v1 = document.querySelector('#v1');
// let v2 = document.querySelector('#v2');
// let result = document.querySelector('#result');


// let add = () => {
//     try {
//         result.innerHTML = parseFloat(v1.value) + parseFloat(v2.value);
//         // test
//         console.log(result.value);
//     } catch (error) {
//         alert('Please enter valid values');
//         v1.value = '';
//         v2.value = '';
//         v1.focus();
//     }
// };

// let subtract = () => {
//     try {
//         result.innerHTML = parseFloat(v1.value) - parseFloat(v2.value);
//         // test
//         console.log(result.value);
//     } catch (error) {
//         alert('Please enter valid values');
//         v1.value = '';
//         v2.value = '';
//         v1.focus();
//     }
// }

// let multiply = () => {
//     try {
//         result.innerHTML = parseFloat(v1.value) * parseFloat(v2.value);

//         // test
//         console.log(result.value);
//     } catch (error) {
//         alert('Please enter valid values');
//         v1.value = '';
//         v2.value = '';
//         v1.focus();
//     }
// }

// let divide = () => {
//     try {
//         if (v2.value == 0) {
//             alert("Can't divide by 0");
//             throw new Error("Can't divide by 0");
//         }
//         result.value = parseFloat(v1.value) / parseFloat(v2.value);

//         // test
//         console.log(result.value);
//     } catch (error) {
//         alert('Please enter valid values');
//         v1.value = '';
//         v2.value = '';
//         v1.focus();
//     }
// }


    // JQuery version


let add = () =>  {
    try {
        $('#result').html(parseFloat($('#v1').val()) + parseFloat($('#v2').val()));
        console.log($('#result').val());
    } catch {
        alert('Please enter valid values');
        $('#v1').val('');
        $('#v2').val('');
        $('#v1').focus();
    }
};

let subtract = () => {
    try {
        $('#result').html(parseFloat($('#v1').val()) - parseFloat($('#v2').val()));
    } catch {
        alert('Please enter valid values');
        $('#v1').val('');
        $('#v2').val('');
        $('#v1').focus();
    }
};

let multiply = () => {
    try {
        $('#result').html(parseFloat($('#v1').val()) * parseFloat($('#v2').val()));
    }  catch {
        alert('Please enter valid values');
        $('#v1').val('');
        $('#v2').val('');
        $('#v1').focus();
    }
};
  
let divide = () => {
    try {
        if ($('#v2').val() == 0) {
            alert("Can't divide by 0");
            throw new Error("Can't divide by 0");
        }
        $('#result').html(parseFloat($('#v1').val()) / parseFloat($('#v2').val()));
    } catch {
        alert('Please enter valid values');
        $('#v1').val('');
        $('#v2').val('');
        $('#v1').focus();
    }
}

