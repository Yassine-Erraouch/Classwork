    // native js
let encrypt = () => {
    let text = (document.querySelector("#text").value).toLowerCase();
    let shift = document.querySelector("#shift").value;
    if (isNaN(shift)) {
        alert('Please enter valid shift');
        document.querySelector("#shift").value = '';
        document.querySelector("#shift").focus();
    } else {
        let encrypted = '';
        let alphabet = 'abcdefghijklmnopqrstuvwxyz';
        for (let i = 0; i < text.length; i++) {
            let char = text[i];
            let index = alphabet.indexOf(char);
            if (index === -1) {
                encrypted += char;
            } else {
                let newIndex = (index + parseInt(shift)) % 26;
                encrypted += alphabet[newIndex];
            }
        }
        document.querySelector("#result").innerHTML = encrypted;
    }
};

document.querySelector("#encrypt").addEventListener("click", encrypt);
