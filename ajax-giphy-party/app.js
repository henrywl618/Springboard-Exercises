//const axios = require('axios').default;
const giphyAPIKey = 'ZaeawWciQX3HaEevh9Z9iSXjRXnCgsc1';

async function getGifURL(tag,api_key){
    const result = await axios.get('https://api.giphy.com/v1/gifs/random', {
        params:{
            api_key,
            tag,},
    });
    const url =result.data.data.images.fixed_width.url;
    return url
}

function appendImg(url){
    $('#imgContainer').append($(`<img src=${url}>`)); //Append a newly created image with the given url to the image container div
}

$('#searchBtn').on('click', async ()=>{
    const searchValue = $('#searchInput').val();
    const gifURL = await getGifURL(searchValue, giphyAPIKey);
    appendImg(gifURL);
})

$('#removeBtn').on('click', ()=>{
    $('#imgContainer').empty();
})