const $guessForm = $('#guessForm')
const $guessInput = $('#guessInput')

// submits http request to server with the form info
async function submitGuess(event){
    event.preventDefault();
    const guess = $guessInput.val();

    response = await getResponse(guess);

}

async function getResponse(word){
    return await axios.post('/',{guess:word});
}

function updatePage(response){

}

//clickeven handler for the submit button
$guessForm.on('submit',submitGuess);