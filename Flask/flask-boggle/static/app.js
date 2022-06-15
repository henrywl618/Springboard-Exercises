const $guessForm = $('#guessForm')
const $guessInput = $('#guessInput')
const $responseText = $('#response')
const $scoreDisplay = $('#score')

let score = 0
const guesses = new Set()

// submits http request to server with the form info
async function submitGuess(event){
    event.preventDefault();
    const guess = $guessInput.val();

    response = await getResponse(guess);
    updatePage(response);
    updateScore(response,guess);

    //empty the input field
    $guessForm.trigger('reset');

}

async function getResponse(word){
    return await axios.post('/',{guess:word});
}


function updatePage(response){
    $responseText.text(response.data.result);
}

//Update the score if the guess is not already been guessed and it is a word/on the board
function updateScore(response,guess){
    if(response.data.result === 'ok' && !guesses.has(guess)){
        guesses.add(guess);
        score += guess.length;
        $scoreDisplay.text(score);
    }
}

//clickevent handler for the submit button
$guessForm.on('submit',submitGuess);