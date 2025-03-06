let calories = {
    bread: 2.75,
    beef: 1.8,
    vegetables:0.4,
    banana: 116,
    apple:80,
    yogurt:140
}



$("input[type=checkbox]").on("click", function(){
    if($(this).is(":checked")){
        $(this).closest(".row").find("input[type=text]").prop("disabled", false);
    }else{
        $(this).closest(".row").find("input[type=text]").prop("disabled", true);
    }
});

$('#calculate').on("click", function(){
    if ($("input[type=text]").val() == "") {
        $('#result').val();
    } else {
        let total = parseInt($('#0').val()) * calories.
        console.log(total)
        console.log(total)
    }
})



