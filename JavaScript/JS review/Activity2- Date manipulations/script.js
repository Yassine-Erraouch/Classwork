// function to get current date

// let getCurrentDate = () => {
//     let date = new Date();
//     console.log(date);
// }

// getCurrentDate();

// function to create a date object
// let createDateObject = (year, month , day) => {
//     let date = new Date(year, month -1, day +1);
//     console.log(date);
//     return date;
// }

// createDateObject(2025, 5, 20);

// function to convert date object into string;

// let convertToString = (date) => {
//    stringDate = date.toLocaleString();
//    console.log(stringDate);
// }
// date = new Date(2025, 5, 10);
// convertToString(date);



// function to convert string into date object

// let convertToDate = (string) => {
//     let date = new Date(string);
//     console.log(date);
// }

// convertToDate('2025-05-10');

// function to compare twod dates;

// let compareDates = (date1, date2)=>  {
//     if (date1 > date2) {
//         console.log(`${date1.toLocaleString()} is greater than ${date2.toLocaleString()}`);
//     } else if (date1 < date2) {
//         console.log(`${date1.toLocaleString()} is less than ${date2.toLocaleString()}`);
//     } else {
//         console.log(`${date1.toLocaleString()}  is equal to  ${date2.toLocaleString()}`);
//     }
// }

// let date1 = new Date(2025, 4, 9);
// let date2 = new Date(2025, 4, 9);
// compareDates(date1, date2);


// function to calculate difference between two dates

let calculateDifference = (date1, date2) => {
    let diffInYears = date1.getFullYear() - date2.getFullYear();
    let diffInMonths = date1.getMonth() - date2.getMonth();
    let diffInDays = date1.getDate() - date2.getDate();
   
    console.log(`the difference in years is ${diffInYears}. The difference in months is ${diffInMonths}. The difference in days is ${diffInDays}.`);
}

let date1 = new Date(2025, 4, 9);
let date2 = new Date(2026, 4, 9);
calculateDifference(date1, date2);


