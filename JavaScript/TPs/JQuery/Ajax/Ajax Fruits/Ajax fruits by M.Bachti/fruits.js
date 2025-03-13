let data=[];
let newFruit={nameFruit:"",PriceFruit:0,image:""};
let fruitToEdit=-1;



//coder la fonction handelChange
const handelChange=(e)=>{
    const {name,value} =e.target;
    newFruit[name]=value;
    console.log(newFruit);
}

//coder la fonction addFruit
const addOrEditFruit=()=>{
    for(let k in newFruit){
        if(newFruit[k]==="" || newFruit[k]===0) 
            throw new Error('Tous les champs sont obligatoires !!!');
    }
    if (fruitToEdit==-1){
        newFruit['codeFruit']=data.length>0?data.length:1;
        data.push(newFruit);
    } else {
        data[fruitToEdit]=newFruit;
    }
    //reset
    newFruit={nameFruit:"",PriceFruit:0,image:""};
    fruitToEdit=-1
    display(data);
    $('#name').val("");
    $('#price').val(0);
    $('#image').val("");
    //reset
    $('#addFruit').modal('hide');//show
}
  //coder la fonction display data
const display=(data)=>{
    $('.myTable tbody').empty();

    $(data).each(function(index,fruit){
        $(`<tr>
        <td>${fruit.codeFruit}</td>
        <td>${fruit.nameFruit}</td>
        <td>${fruit.PriceFruit}</td>
        <td><img src="${fruit.image}" width="60px" height="60px"/></td>
        <td><button class="btn btn-sm-danger" onclick="deleteF(${index})">Delete</button>&nbsp;&nbsp;
        <button class="btn btn-sm-info" onclick="editF(${index})">Edit</button></td>
        </tr>`).appendTo('.myTable tbody');
    });
} 
//coder la fonction deleteFruit
const deleteF=(index)=>{
if (window.confirm('voulez vous vraiment supprimer ?')) {
    data.splice(index,1);
    display(data);
}
};

//code la fonction edit
const editF=(index)=>{
    let fruit=data[index];
    fruitToEdit=index;
    $('#name').val(fruit.nameFruit);
    $('#price').val(fruit.PriceFruit);
    $('#image').val(fruit.image);
    $('#addFruit').modal('show');//show

    newFruit["codeFruit"]=fruit.codeFruit;
    newFruit["nameFruit"]=fruit.nameFruit;
    newFruit["PriceFruit"]=fruit.PriceFruit;
    newFruit["image"]=fruit.image;
}




$.ajax({
    url:"http://localhost:3003/fruits",
    method:"get",
    dataType:"json",
    success:function(response){
        data=response;
        display(data);
    },
    error:function(error){
    console.log(error);
    }
});
