    // native js


let encrypt = () => {
    let text = document.querySelector("#text").value;
    let password = document.querySelector("#password").value;
    let encrypted = CryptoJS.AES.encrypt(text, password).toString();   
    document.querySelector("#result").innerHTML = encrypted;

};

let decrypt = () => {
    let text = document.querySelector("#text").value;
    let password = document.querySelector("#password").value;
    let decrypted = CryptoJS.AES.decrypt(text, password).toString(CryptoJS.enc.Utf8);   
    document.querySelector("#result").innerHTML = decrypted;
};

document.querySelector("#encrypt").addEventListener("click", encrypt);
document.querySelector("#decrypt").addEventListener("click", decrypt);
