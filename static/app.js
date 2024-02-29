const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#add-cupcake-form");
const $addCupcakeButton = $(".add-cupcake-button");
const $cupcakeIdInput = $(".cupcake-id");
const $cupcakeFlavorInput = $('.cupcake-flavor');
const $cupcakeSizeInput = $('.cupcake-size');
const $cupcakeRatingInput = $('.cupcake-rating');
const $cupcakeImageInput = $('.cupcake-image');
const $cupcakeIngredientInput = $('.cupcake-ingredients');
const $searchCupcakeForm = $('#search-cupcake-form');
const $ingredientForm = $('#ingredient-form');
const $ingredientList = $('.ingredient-list');
const $ingredientNameInput = $('.ingredient-name');
const $ingredientIdInput = $('.ingredient-id');

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
$cupcakeForm.submit(async function(event){
    event.preventDefault();
    console.log('cupcake form submitted');
    if ($cupcakeIdInput.val() === ''){
        newCupcake = gatherCupcakeData();
        await newCupcake.addCupcake();
    } else {
        cupcakeId = $cupcakeIdInput.val();
        cupcakeFlavor = $cupcakeFlavorInput.val();
        cupcakeImage = $cupcakeImageInput.val();
        cupcakeSize = $cupcakeSizeInput.val();
        cupcakeRating = $cupcakeRatingInput.val();
        cupcakeIngredients = $cupcakeIngredientInput.val();
        cupcakeData = {flavor: cupcakeFlavor, image: cupcakeImage, size: cupcakeSize, rating: cupcakeRating, ingredients: cupcakeIngredients};
        await Cupcake.updateCupcake(cupcakeId, cupcakeData);
    }
    
});

//cupcake click event listener
$cupcakeList.on('click', '.update-button', async function(event){
    let cupcakeId = $(event.target).closest('li').attr('id');
    console.log('cupcakeId = ', cupcakeId);
    returnArray = await Cupcake.getCupcake(cupcakeId);
    updateCupcake = returnArray[0];
    updateIngredients = returnArray[1];
    console.log(await Cupcake.getCupcake(cupcakeId));
    console.log('updateCupcake = ', updateCupcake);
    console.log('updateIngredients = ', updateIngredients);
    fillCupcakeForm(updateCupcake, updateIngredients);
})

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
    if ($ingredientIdInput.val() === ''){
        newIngredient = gatherIngredientData();
        await newIngredient.addIngredient();
    } else {
        ingredientId = $ingredientIdInput.val();
        ingredientName = $ingredientNameInput.val();
        ingredientData = {name: ingredientName}
        await Ingredient.updateIngredient(ingredientId, ingredientData);
    }

})

//ingredient click event listener
$ingredientList.click(function(event){
    let ingredientId = $(event.target).closest('div').attr('id');
    console.log('ingredientId = ', ingredientId);
    let ingredientName = $(event.target).closest('div').text();
    console.log('ingredientName = ', ingredientName);
    $ingredientIdInput.val(ingredientId);
    $ingredientNameInput.val(ingredientName);
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
        const $cupcakeLi = $(`<li id=${cupcake.id}><img src=${cupcake.image} class="img-thumbnail border-0" style="max-width:125px"> <b>${cupcake.flavor}</b><span class="cupcake-details">(${cupcake.size}, ${cupcake.rating} stars)</span><a href="#cupcake_form" class="btn btn-primary btn-small update-button" role=""button"><i class="fas fa-pencil"></i></a><button class="btn btn-danger btn-small delete-button"><b>X</b></button></li>`);
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
    const ingredients = $cupcakeIngredientInput.val();
    cupcakeData = {flavor: flavor, size: size, rating: rating, image: image, ingredients: ingredients};
    const newCupcake = new Cupcake(cupcakeData);
    console.log(newCupcake);
    return newCupcake;
}

//fill the cupcake form with details based on the cupcake to be updated
function fillCupcakeForm(cupcake, ingredients){
    $cupcakeIdInput.val(cupcake.id);
    $cupcakeFlavorInput.val(cupcake.flavor);
    $cupcakeFlavorInput.attr('class', 'form-control-plaintext');
    $cupcakeImageInput.val(cupcake.image);
    $cupcakeImageInput.attr('class', 'form-control-plaintext');
    $cupcakeSizeInput.val(cupcake.size);
    $cupcakeRatingInput.val(cupcake.rating);
    $cupcakeIngredientInput.val(ingredients);
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
        const $ingredientDiv = $(`<div class="col" style="cursor:pointer" id=${ingredient.id}>${ingredient.name}</div>`);
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