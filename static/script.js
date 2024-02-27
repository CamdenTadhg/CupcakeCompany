const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#add-cupcake-form");
const $addCupcakeButton = $(".add-cupcake-button");
const $cupcakeFlavorInput = $('.cupcake-flavor');
const $cupcakeSizeInput = $('.cupcake-size');
const $cupcakeRatingInput = $('.cupcake-rating');
const $cupcakeImageInput = $('.cupcake-image');
let cupcakeData = {};

$(document).ready(getCupcakes);

async function getCupcakes() {
    try{
        console.log('starting getCupcakes')
        const cupcakes = await axios.get('/api/cupcakes');
        for (cupcake of cupcakes.data.cupcakes){
            console.log('starting for statement');
            const $cupcakeLi = $(`<ul><img src=${cupcake.image} class="img-thumbnail border-0" style="max-width:125px"> <b>${cupcake.flavor}</b> (${cupcake.size}, ${cupcake.rating} stars)</ul>`);
            $cupcakeLi.addClass('fs-3');
            $cupcakeList.append($cupcakeLi);
        }
    } catch(error) {
        alert("No cupcakes found")
    }
};

$cupcakeForm.submit(function(event){
    event.preventDefault();
    console.log('cupcake form submitted');
    gatherCupcakeData();
    submitCupcakeForm();
});

function gatherCupcakeData() {
    console.log('starting gatherCupcakeData');
    const flavor = $cupcakeFlavorInput.val();
    const size = $cupcakeSizeInput.val();
    const rating = $cupcakeRatingInput.val();
    const image = $cupcakeImageInput.val();
    cupcakeData = {flavor: flavor, size: size, rating: rating, image: image};
    console.log(cupcakeData);
}

async function submitCupcakeForm() {
    try{
        console.log('starting submitCupcakeForm');
        const response = await axios.post('/api/cupcakes', cupcakeData)
        console.log(response);
        $cupcakeList.empty();
        getCupcakes();
        $cupcakeFlavorInput.val("");
        $cupcakeSizeInput.val("");
        $cupcakeRatingInput.val("");
        $cupcakeImageInput.val("");
    } catch(error) {
        alert("Form submission failed. Please try again")
    }
}