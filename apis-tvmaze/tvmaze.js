"use strict";

const $showsList = $("#shows-list");
const $episodesArea = $("#episodes-area");
const $searchForm = $("#search-form");


/** Given a search term, search for tv shows that match that query.
 *
 *  Returns (promise) array of show objects: [show, show, ...].
 *    Each show object should contain exactly: {id, name, summary, image}
 *    (if no image URL given by API, put in a default image URL)
 */

async function getShowsByTerm(term) {
  // ADD: Remove placeholder & make request to TVMaze search shows API.
  const results =  await axios.get(' https://api.tvmaze.com/search/shows', {params:{q:term}});
  const showsArray = [];

  //get the id, name, summary, medium image url from the returned JSON, put it in an object and 
  //add it to the array to be returned.
  for(let element of results.data){
    showsArray.push({
      id : element.show.id,
      name : element.show.name,
      summary : element.show.summary,
      medium :element.show.image === null ? "https://tinyurl.com/tv-missing" : element.show.image.medium ,
    })
  }
  return showsArray;
}


/** Given list of shows, create markup for each and to DOM */

function populateShows(shows) {
  $showsList.empty();

  for (let show of shows) {
    const $show = $(
        `<div data-show-id="${show.id}" class="Show col-3 mb-4">
         <div class="card text-justify">
           <img 
              src=${show.medium} 
              alt="https://tinyurl.com/tv-missing" 
              class="card-img-top p-1">
           <div class="card-body row justify-content-center">
             <h5 class="text-primary text-center">${show.name}</h5>
             <div  class="px-3"><small>${show.summary}</small></div>
             <button name= "epBtn" class="btn btn-outline-light btn-sm Show-getEpisodes text-center col-6 ">
               Episodes
             </button>
           </div>
         </div>  
       </div>
      `);

    $showsList.append($show);  }
}


/** Handle search form submission: get shows from API and display.
 *    Hide episodes area (that only gets shown if they ask for episodes)
 */

async function searchForShowAndDisplay() {
  const term = $("#search-query").val();
  const shows = await getShowsByTerm(term);

  $episodesArea.hide();
  populateShows(shows);
}

$searchForm.on("submit", async function (evt) {
  evt.preventDefault();
  await searchForShowAndDisplay();
});


/** Given a show ID, get from API and return (promise) array of episodes:
 *      { id, name, season, number }
 */

async function getEpisodesOfShow(id) { 
  const results =  await axios.get(`https://api.tvmaze.com/shows/${id}/episodes`);
  const epArray = [];
  for(let {id,name,number,season} of results.data){
    epArray.push({
      id,
      name,
      number,
      season,
    })
  }
  return epArray;
}

/** Write a clear docstring for this function... */

function populateEpisodes(episodes) {
  const episodeList = $('#episodes-list')
  episodeList.empty();
  for(let episode of episodes){
    episodeList.append($(`<li>${episode.name}  (Season ${episode.season}  Number ${episode.number})</li>`));
  }
  $("#episodes-area").show();
    
}

$('body').on('click','button[name=epBtn]', async function(evt){
  console.log($(this).parent().parent().parent().data('showId'));
  const showID = $(this).parent().parent().parent().data('showId');
  const episodes = await getEpisodesOfShow(showID);
  populateEpisodes(episodes);
})