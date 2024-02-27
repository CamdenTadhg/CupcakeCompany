const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#add-cupcake-form");
const $addCupcakeButton = $(".add-cupcake-button");
const $cupcakeFlavorInput = $('.cupcake-flavor');
const $cupcakeSizeInput = $('.cupcake-size');
const $cupcakeRatingInput = $('.cupcake-rating');
const $cupcakeImageInput = $('.cupcake-image');
const $searchCupcakeForm = $('#search-cupcake-form');

$(document).ready(cupcakesOnStart);

//cupcake searching event listener for submit
$searchCupcakeForm.submit(function(event){
    event.preventDefault();
    console.log('search form submitted');
    const searchTerm = $('.cupcake-search').val();
    searchResults = CupcakeList.searchCupcakes(searchTerm);
    displayCupcakes(searchResults);
})

//cupcake searching event listener for keypress
$searchCupcakeForm.keyup(function(){
    console.log('search character entered');
    const searchTerm = $('.cupcake-search').val();
    console.log(searchTerm);
    searchResults = CupcakeList.searchCupcakes(searchTerm);
    displayCupcakes(searchResults);
})

//cupcake adding event listener
$cupcakeForm.submit(function(event){
    event.preventDefault();
    console.log('cupcake form submitted');
    newCupcake = gatherCupcakeData();
    newCupcake.addCupcake();
});

//event listener for delete buttons on cupcake list
$cupcakeList.on('click', '.delete-button', function(event){
    Cupcake.deleteCupcake($(event.target).parent().attr('id'));
    console.log($(event.target).parent().attr('id'));
    $(this).closest('li').remove();

})

//initial function to show cupcakes on site load
async function cupcakesOnStart() {
    mainCupcakeList = await CupcakeList.getCupcakes();
    displayCupcakes(mainCupcakeList)
}

//display an instance of CupcakeList on the page
function displayCupcakes(array){
    console.log('entering display cupcakes')
    console.log(array);
    $cupcakeList.empty()
    for (let cupcake of array.cupcakes){
        console.log('starting for statement');
        const $cupcakeLi = $(`<li id=${cupcake.id}><a href="/cupcakes/${cupcake.id}"><img src=${cupcake.image} class="img-thumbnail border-0" style="max-width:125px"></a> <b>${cupcake.flavor}</b> (${cupcake.size}, ${cupcake.rating} stars) <button class="btn btn-primary btn-small update-button"><i class="fas fa-pencil"></i></button><button class="btn btn-danger btn-small delete-button"><b>X</b></button></li>`);
        $cupcakeLi.addClass('fs-3');
        $cupcakeList.append($cupcakeLi);
}}

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

