const cupcakesList = $('ul')
const addBtn = $('#addCupcakeBtn')

async function getAllCupcakes(){
    const response = await axios.get('/api/cupcakes');
    const cupcakes = response.data.cupcakes
    return cupcakes
}

async function loadCupcakes(){
    const cupcakes = await getAllCupcakes()
    for(cupcake of cupcakes){
        cupcakesList.append(
            `<li><img src=${cupcake.image}>${cupcake.flavor} ${cupcake.size} ${cupcake.rating} <button data-id=${cupcake.id}>X</button> </li>`
        )
    }
}

async function addCupcakeDB(){

    const form = document.getElementById('form')
    //Create a formEntries object that contains key:value pairs for each entry in the form
    const formData = new FormData(form)
    const formEntries = {}
    formData.forEach((value,key) => {
        if(key != 'csrf_token' && value != ''){
            formEntries[key] = value
        }
    })
    //Send a post request with data from the formEntries object
    const response = await axios.post('/api/cupcakes',{...formEntries})
    const cupcake = response.data.cupcake
    return cupcake
}

function addCupcakeHTML(cupcake){
    cupcakesList.append(
        `<li><img src=${cupcake.image}>${cupcake.flavor} ${cupcake.size} ${cupcake.rating} <button data-id=${cupcake.id}>X</button> </li>`
    )
}

async function deleteCupcake(id){
    response = await axios.delete(`/api/cupcakes/${id}`)
}

$(loadCupcakes)
addBtn.on('click',async ()=>{
    const cupcake = await addCupcakeDB();
    addCupcakeHTML(cupcake);
})
$('ul').on('click','button',async function(){
    id = $(this).data('id');
    await deleteCupcake(id);
    $(this).parent().remove();
})