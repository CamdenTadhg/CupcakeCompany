const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#add-cupcake-form");
const $addCupcakeButton = $(".add-cupcake-button");
const $cupcakeFlavorInput = $('.cupcake-flavor');
const $cupcakeSizeInput = $('.cupcake-size');
const $cupcakeRatingInput = $('.cupcake-rating');
const $cupcakeImageInput = $('.cupcake-image');
const $searchCupcakeForm = $('#search-cupcake-form');
let cupcakeData = {};
let cupcakes = {};

$(document).ready(storiesOnStart);

//cupcake searching event listener
$searchCupcakeForm.submit(function(event){
    event.preventDefault();
    console.log('search form submitted');
    searchResults = searchCupcakes();
    displayCupcakes(searchResults);
})

//cupcake adding event listener
$cupcakeForm.submit(function(event){
    event.preventDefault();
    console.log('cupcake form submitted');
    newCupcake = gatherCupcakeData();
    newCupcake.addCupcake();
});

//initial function to show cupcakes on site load
async function storiesOnStart() {
    mainCupcakeList = await CupcakeList.getCupcakes();
    displayCupcakes(mainCupcakeList)
}

//display an instance of CupcakeList on the page
function displayCupcakes(array){
    console.log('entering display cupcakes')
    console.log(array);
    $cupcakeList.empty()
    for (cupcake of array){
        console.log('starting for statement');
        const $cupcakeLi = $(`<ul><img src=${cupcake.image} class="img-thumbnail border-0" style="max-width:125px"> <b>${cupcake.flavor}</b> (${cupcake.size}, ${cupcake.rating} stars)</ul>`);
        $cupcakeLi.addClass('fs-3');
        $cupcakeList.append($cupcakeLi);
}}

//search for cupcakes matching an inputted search string
function searchCupcakes(){
    const searchTerm = $('.cupcake-search').val();
    const numericSearchTerm = parseInt(searchTerm);
    const cupcakeResults = [];
    for (cupcake of cupcakes.data.cupcakes){
        console.log('entering for cupcake of cupcakes');
        console.log(cupcake);
        for (key in cupcake){
            console.log('entering for key in cupcake');
            console.log(key);
            if (key === 'id' || key === 'rating'){
                console.log('entering numeric search');
                if (cupcake[key] === numericSearchTerm){
                    if (cupcakeResults.includes(cupcake) === false){
                        cupcakeResults.push(cupcake);
                        console.log('CUPCAKE ADDED');
                    }
                }
            }
            else if (isNaN(numericSearchTerm)){
                console.log('entering string search');
                if (cupcake[key].search(searchTerm) != -1){
                    if (cupcakeResults.includes(cupcake) === false){
                        cupcakeResults.push(cupcake);
                        console.log('CUPCAKE ADDED');
                    }
                }
            }
        }
    }
    console.log(cupcakeResults);
    return cupcakeResults;
}

//pull data from the new cupcake form and return it as a new instance of cupcake. 
function gatherCupcakeData() {
    console.log('starting gatherCupcakeData');
    const flavor = $cupcakeFlavorInput.val();
    const size = $cupcakeSizeInput.val();
    const rating = $cupcakeRatingInput.val();
    const image = $cupcakeImageInput.val();
    cupcakeData = {flavor: flavor, size: size, rating: rating, image: image};
    const newCupcake = new Cupcake(cupcakeData);
    console.log(newCupcake);
    return newCupcake;
}

