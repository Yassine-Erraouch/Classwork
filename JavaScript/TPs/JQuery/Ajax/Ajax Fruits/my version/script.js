$.ajax(
    {
        url:"http://localhost:3000/fruits",
        type: 'GET',
        dataType: 'json',
        success: function(data){
            fruits = data;
            console.log(fruits);


            // load the table
            displayFruits()
            function displayFruits() {
                let html = '';
                for (let fruit of fruits) {
                    html += `<tr>
                                <td>${fruit.codeF} </td>
                                <td>${fruit.name} </td>
                                <td>${fruit.price} </td>
                                <td><img src="${fruit.photo}" class="img-fluid w-25"> </td>
                                <td>
                                    <button class="btn btn-primary" id="editBtn" data-bs-toggle="modal" data-bs-target="#editModal">Edit</button>
                                    <button class="btn btn-danger" id="deleteBtn" onclick="deleteFruit(${fruit.codeF})">Delete</button>
                                </td>
                            </tr>`
                };
                $('#display').html(html);
            };

            

            function deleteFruit(codeF) {
                if (confirm('Are you sure you want to remove this fruit?')) {
                    let index = fruits.findIndex(fruit => fruit.codeF == codeF);
                    if (index !== -1) { // Ensure the fruit exists in the array
                        fruits.splice(index, 1);
                        displayFruits();
                    } else {
                        console.error('Fruit not found');
                    }
                }
            }

            let addFruit = () => {
                
            }




        }, error: function(error){
            console.log(error);
        }
    }
)




