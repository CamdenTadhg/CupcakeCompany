const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#add-cupcake-form");
const $addCupcakeButton = $(".add-cupcake-button");
const $cupcakeFlavorInput = $('.cupcake-flavor');
const $cupcakeSizeInput = $('.cupcake-size');
const $cupcakeRatingInput = $('.cupcake-rating');
const $cupcakeImageInput = $('.cupcake-image');
const $searchCupcakeForm = $('#search-cupcake-form');
const $ingredientForm = $('#ingredient-form');
const $ingredientList = $('.ingredient-list');
const $ingredientNameInput = $('.ingredient-name');

$(document).ready(function(){
    cupcakesOnStart();
    ingredientsOnStart();
})

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
$cupcakeList.on('click', '.delete-button', async function(event){
    try {
        console.log('starting event listener');
        const cupcakeId = $(event.currentTarget).closest('li').attr('id');
        console.log(cupcakeId)
        await Cupcake.deleteCupcake(cupcakeId);
        $(this).closest('li').remove();
    } catch (error) {
        alert("Delete cupcake event listener failed. Please try again.")
    }
});

//ingredient adding event listener
$ingredientForm.submit(async function(event){
    event.preventDefault();
    console.log('ingredient form submitted');
    newIngredient = gatherIngredientData();
    newIngredient.addIngredient();
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
        const $cupcakeLi = $(`<li id=${cupcake.id}><img src=${cupcake.image} class="img-thumbnail border-0" style="max-width:125px"> <b>${cupcake.flavor}</b> <span class="cupcake-details">(${cupcake.size}, ${cupcake.rating} stars)</span><button class="btn btn-primary btn-small update-button" data-bs-toggle="modal" data-bs-target="update-modal"><i class="fas fa-pencil"></i></button><button class="btn btn-danger btn-small delete-button"><b>X</b></button></li>`);
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

//initial function to show ingredients on site load
async function ingredientsOnStart() {
    ingredientList = await IngredientList.getIngredients();
    displayIngredients(ingredientList)
}

//display an instance of IngredientList on the page
function displayIngredients(array){
    console.log('entering display ingredients')
    console.log(array);
    $ingredientList.empty()
    for (let ingredient of array.ingredients){
        console.log('starting for statement');
        const $ingredientDiv = $(`<div class="col" id=${ingredient.id}>${ingredient.name}</div>`);
        $ingredientDiv.addClass('fs-3');
        $ingredientList.append($ingredientDiv);
}}

function gatherIngredientData() {
    console.log('starting gatherIngredientData');
    const name = $ingredientNameInput.val();
    ingredientData = {name: name};
    const newIngredient = new Ingredient(ingredientData);
    console.log(newIngredient);
    return newIngredient;
}