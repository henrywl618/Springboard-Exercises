describe('API request tests',()=>{

    it('should get get data from the api', async ()=>{
        await expectAsync(getShowsByTerm('cars')).toBeResolved();
        await expectAsync(getEpisodesOfShow(532)).toBeResolved();
    })

    it('should return an array of objects', async ()=>{
        expect(await getShowsByTerm('cars')).toBeInstanceOf(Array);
        expect((await getShowsByTerm('cars')).length).toBeGreaterThan(0);
        expect((await getShowsByTerm('cars'))[0]).toBeInstanceOf(Object);
        
        expect(await getEpisodesOfShow(532)).toBeInstanceOf(Array);
        expect((await getEpisodesOfShow(532)).length).toBeGreaterThan(0);
        expect((await getEpisodesOfShow(532))[0]).toBeInstanceOf(Object);
    })

})

describe('DOM manipulation tests', ()=>{

    it('should append div cards of shows', async ()=>{
        const shows = await getShowsByTerm('cars');
        const $showsList = $('<div id="shows-list"></div>');
        populateShows(shows);
        expect($showsList.length).toBeGreaterThan(0);
    })

    it('should append li to a ul', async()=>{
        const episodes = await getEpisodesOfShow(532);
        const $episodeList = $('<ul id="episodes-list"></ul>');
        populateEpisodes(episodes);
        expect($episodeList.length).toBeGreaterThan(0);
    })
})


